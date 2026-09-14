import json

from document_loader import load_documents


def test_load_documents_reads_json_files(tmp_path):
    docs_dir = tmp_path / "documents"
    docs_dir.mkdir()

    (docs_dir / "one.json").write_text(json.dumps({"title": "One", "content": "Alpha"}), encoding="utf-8")
    (docs_dir / "two.json").write_text(json.dumps({"title": "Two", "content": "Beta"}), encoding="utf-8")

    docs = load_documents(docs_dir)

    assert len(docs) == 2
    assert docs[0]["title"] == "One"
    assert docs[0]["content"] == "Alpha"
    assert docs[1]["title"] == "Two"
    assert docs[1]["content"] == "Beta"


def test_load_documents_missing_folder_returns_empty_list():
    docs = load_documents("does_not_exist")
    assert docs == []
