import google.genai as genai
from google.genai import types

_client: genai.client.Client | None = None


def configure(
    api_key: str,
    *,
    enterprise=None,
    vertexai=None,
    credentials=None,
    project=None,
    location=None,
    debug_config=None,
    http_options=None,
):
    global _client
    _client = genai.client.Client(
        api_key=api_key,
        enterprise=enterprise,
        vertexai=vertexai,
        credentials=credentials,
        project=project,
        location=location,
        debug_config=debug_config,
        http_options=http_options,
    )
    return _client


def _ensure_client():
    if _client is None:
        raise RuntimeError("GenAI client is not configured. Call configure(api_key=...) first.")
    return _client


def _content_to_parts(item):
    if isinstance(item, list):
        parts = []
        for sub in item:
            parts.extend(_content_to_parts(sub))
        return parts
    if isinstance(item, str):
        return [types.Part(text=item)]
    return [item]


def _build_contents(contents):
    if contents is None:
        return []
    return _content_to_parts(contents)


def _build_config(system_instruction=None, config=None):
    """Merge an optional caller-supplied config with the model's
    system_instruction. The google-genai SDK expects system_instruction to
    live on GenerateContentConfig (or an equivalent dict), NOT as a role
    on a content Part -- Part has no 'role' field and passing one raises
    a pydantic ValidationError.
    """
    if config is None:
        if system_instruction:
            return types.GenerateContentConfig(system_instruction=system_instruction)
        return None

    if isinstance(config, dict):
        if system_instruction and "system_instruction" not in config:
            config = {**config, "system_instruction": system_instruction}
        return config

    # Assume it's already a GenerateContentConfig (or compatible) instance.
    if system_instruction and getattr(config, "system_instruction", None) is None:
        try:
            config.system_instruction = system_instruction
        except Exception:
            pass
    return config


class _GenaiResponse:
    def __init__(self, response):
        self._response = response

    @property
    def text(self) -> str:
        if not getattr(self._response, "candidates", None):
            return ""
        candidate = self._response.candidates[0]
        if not getattr(candidate, "content", None):
            return ""
        parts = getattr(candidate.content, "parts", [])
        text_parts = [getattr(part, "text", "") or "" for part in parts]
        return "".join(text_parts).strip()

    def __getattr__(self, name):
        return getattr(self._response, name)


class GenerativeModel:
    def __init__(self, model_name, system_instruction=None, **kwargs):
        self.model_name = model_name
        self.system_instruction = system_instruction
        self.kwargs = kwargs

    def generate_content(self, contents, **kwargs):
        client = _ensure_client()
        request_contents = _build_contents(contents)
        config = _build_config(self.system_instruction, kwargs.get("config"))
        response = client.models.generate_content(
            model=self.model_name,
            contents=request_contents,
            config=config,
        )
        return _GenaiResponse(response)


def Client(*args, **kwargs):
    return genai.client.Client(*args, **kwargs)
