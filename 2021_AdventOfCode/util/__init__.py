def read_file(file: str) -> list[str]:
    lines = []
    with open(file) as f:
        lines = f.readlines()
    return lines
