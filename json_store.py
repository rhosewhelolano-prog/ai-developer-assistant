import json
from pathlib import Path


def read_json(path):
    p = Path(path)
    if not p.exists():
        return None
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path, data):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def update_json(path, updates: dict):
    """Load JSON from `path`, merge `updates` at top level, and save."""
    data = read_json(path) or {}
    if not isinstance(data, dict):
        raise ValueError("update_json expects a JSON object at the root")
    data.update(updates)
    write_json(path, data)
    return data


def increment_counter(path, key="counter"):
    data = read_json(path) or {}
    if not isinstance(data, dict):
        raise ValueError("increment_counter expects a JSON object at the root")
    data[key] = int(data.get(key, 0)) + 1
    write_json(path, data)
    return data


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    default_path = Path(__file__).resolve().parent / "data" / "sample_data.json"

    parser = argparse.ArgumentParser(description="Simple JSON store CLI")
    parser.add_argument("action", choices=["write", "read", "update", "increment"], help="Action to perform")
    parser.add_argument("--path", default=str(default_path), help="Path to JSON file")
    parser.add_argument("--data", help="JSON string for write or update (e.g. '{\"k\":1}')")
    parser.add_argument("--key", default="counter", help="Key for increment action")

    args = parser.parse_args()
    path = args.path

    if args.action == "write":
        if not args.data:
            print("Provide --data with a JSON object to write")
        else:
            write_json(path, json.loads(args.data))
            print("Wrote:", read_json(path))
    elif args.action == "read":
        print(read_json(path))
    elif args.action == "update":
        if not args.data:
            print("Provide --data with a JSON object to update")
        else:
            updated = update_json(path, json.loads(args.data))
            print("Updated:", updated)
    elif args.action == "increment":
        incremented = increment_counter(path, key=args.key)
        print("Incremented:", incremented)