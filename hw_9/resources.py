from pathlib import Path


def resources_path(file_name):
    import tests
    return str(
        Path(tests.__file__).parent.joinpath(f'resources/{file_name}').absolute()
    )
