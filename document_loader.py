import json
from pathlib import Path
from typing import Any


def load_documents(folder: str | Path = "documents") -> list[dict[str, Any]]:
    """Load all JSON files from a folder and return list of document dictionaries."""
    docs_dir = Path(folder)
    if not docs_dir.exists():
        return []

    documents: list[dict[str, Any]] = []

    for json_path in sorted(docs_dir.glob("*.json")):
        with json_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, dict):
            payload = {
                "title": data.get("title", json_path.stem.replace("_", " ").title()),
                "content": data.get("content", data),
                "file": json_path.name,
                "path": str(json_path),
            }
            documents.append(payload)
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    documents.append({
                        "title": item.get("title", json_path.stem.replace("_", " ").title()),
                        "content": item.get("content", item),
                        "file": json_path.name,
                        "path": str(json_path),
                    })
                else:
                    documents.append({
                        "title": json_path.stem.replace("_", " ").title(),
                        "content": item,
                        "file": json_path.name,
                        "path": str(json_path),
                    })
        else:
            documents.append({
                "title": json_path.stem.replace("_", " ").title(),
                "content": data,
                "file": json_path.name,
                "path": str(json_path),
            })

    return documents


if __name__ == "__main__":
    docs = load_documents()
    if not docs:
        print("No JSON documents found in the documents/ folder.")
    else:
        for doc in docs:
            print(f"Title: {doc.get('title', 'Untitled')}")
            print(f"Content: {doc.get('content', '')}")
            print(f"File: {doc.get('file', '')}")
            print('-' * 40)
