from pathlib import Path

def discover_tests(directory):
    path = Path(directory)
    if not path.exists():
        return []

    return sorted(str(p) for p in path.rglob("test_*.py"))
