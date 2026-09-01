import warnings

warnings.simplefilter('always')

with warnings.catch_warnings(record=True) as w:
    import actions.file_processor as fp
    print('imported', fp.__file__)
    for warn in w:
        print('WARNING:', warn.message)
