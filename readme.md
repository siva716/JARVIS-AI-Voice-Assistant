# 🤖 JARVIS AI Voice Assistant

### A Python-Based Intelligent Desktop AI Assistant

JARVIS is a Python-based AI voice assistant designed to provide natural voice interaction, intelligent responses, computer automation, and task assistance through a modular desktop application.

The project combines AI services, voice interaction, system automation, persistent memory, and a graphical user interface into a single personal assistant platform.

---

## ✨ Features

* 🎙️ **Voice Interaction** — Interact with JARVIS using natural voice commands.
* 🧠 **AI-Powered Responses** — Generate intelligent responses using integrated AI services.
* 🖥️ **Desktop Automation** — Perform supported computer and system-level actions.
* 📂 **File & Application Handling** — Work with files and launch supported applications.
* 🔎 **AI Tool Integration** — Extend JARVIS with modular actions and tools.
* 💾 **Persistent Memory** — Store and retrieve relevant information across interactions.
* ⌨️ **Hybrid Interaction** — Support both voice and text-based interaction.
* 🎨 **Graphical User Interface** — Desktop interface for interacting with the assistant.
* 🔐 **API Key Protection** — API credentials are kept outside the public repository.
* 🧩 **Modular Architecture** — Separate modules for agents, actions, memory, configuration, and core functionality.

---

## 🛠️ Technology Stack

| Technology       | Purpose                                |
| ---------------- | -------------------------------------- |
| Python           | Core application development           |
| AI / LLM APIs    | Intelligent responses and reasoning    |
| Voice Processing | Voice input and interaction            |
| GUI              | Desktop user interface                 |
| JSON             | Configuration and API settings         |
| Git & GitHub     | Version control and project management |

---

## 📁 Project Structure

```text
JARVIS_FINAL_CORRECTED/
│
├── actions/                  # System and assistant actions
├── agent/                    # AI agent and decision-making logic
├── config/                   # Configuration and API key templates
├── core/                     # Core assistant functionality
├── memory/                   # Persistent memory components
│
├── face.png                  # Assistant visual asset
├── main.py                   # Application entry point
├── ui.py                     # Graphical user interface
├── or_client.py              # OpenRouter integration
├── genai_compat.py           # Generative AI compatibility layer
│
├── requirements.txt          # Python dependencies
├── setup.py                  # Package setup
├── readme.md                 # Project documentation
│
├── verify_genai_import.py    # AI module verification
└── verify_main_import.py     # Main module verification
```

---

## ⚙️ Requirements

Before running JARVIS, make sure you have:

* Windows / macOS / Linux
* Python 3.12+
* Microphone for voice interaction
* Internet connection for cloud AI services
* Required API credentials

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/siva716/JARVIS-AI-Voice-Assistant.git
cd JARVIS-AI-Voice-Assistant
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows CMD:**

```cmd
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 API Configuration

For security, real API credentials should **never be committed to GitHub**.

A template configuration is provided:

```text
config/api_keys.example.json
```

Create your local API configuration:

```text
config/api_keys.json
```

Add your required API credentials according to the example configuration.

> ⚠️ Never publish real API keys, passwords, tokens, or other secrets to GitHub.

---

## ▶️ Running JARVIS

After completing the installation and configuration:

```bash
python main.py
```

---

## 🧪 Verification

The repository includes verification scripts that can be used to check important modules before running the application.

```bash
python verify_genai_import.py
```

```bash
python verify_main_import.py
```

---

## 🧠 Architecture

JARVIS follows a modular architecture:

```text
                    ┌──────────────────┐
                    │      User        │
                    │ Voice / Text     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │       UI         │
                    │     ui.py        │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │   Main Engine    │
                    │     main.py      │
                    └────────┬─────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
        ┌──────────┐   ┌──────────┐   ┌──────────┐
        │  Agent   │   │ Actions  │   │  Memory  │
        └────┬─────┘   └────┬─────┘   └────┬─────┘
             │              │              │
             └──────────────┼──────────────┘
                            ▼
                    ┌──────────────────┐
                    │   AI Services    │
                    │ Gemini / APIs    │
                    └──────────────────┘
```

---

## 🔒 Security

The project uses a `.gitignore` configuration to prevent sensitive and unnecessary files from being committed.

The following types of files are excluded:

```text
.venv/
__pycache__/
*.pyc
.env
config/api_keys.json
```

Never commit:

* API keys
* Access tokens
* Passwords
* Private credentials
* Personal secrets

---

## 🚧 Future Improvements

Planned improvements include:

* Advanced multi-agent task planning
* More desktop automation capabilities
* Improved long-term memory
* Better voice recognition and response latency
* Additional AI model integrations
* Enhanced system monitoring
* Improved cross-platform compatibility
* More advanced visual interaction
* Better error handling and logging
* Containerized deployment and CI/CD support

---

## 👨‍💻 Author

**Sivaneshwaran R**

Computer Science & Engineering

GitHub:
https://github.com/siva716

---

## ⭐ Project

If you find this project interesting, consider starring the repository and following the development journey.

**JARVIS AI Voice Assistant** — an ongoing project focused on building a practical, modular, AI-powered desktop assistant.
