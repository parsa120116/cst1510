from pathlib import Path


def print_path_report(path_text):
    """Print the absolute path, parent, name, stem and suffix of a path."""
    path = Path(path_text).expanduser().resolve()
    print(f"Absolute path: {path}")
    print(f"Parent: {path.parent}")
    print(f"Name: {path.name}")
    print(f"Stem: {path.stem}")
    print(f"Suffix: {path.suffix}")


path_text = input("Enter a file or directory path: ").strip()
print_path_report(path_text)
