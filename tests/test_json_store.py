import unittest
import tempfile
from pathlib import Path
import json

from json_store import read_json, write_json, update_json, increment_counter


class TestJsonStore(unittest.TestCase):
    def test_write_and_read(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "test.json"
            write_json(p, {"a": 1})
            data = read_json(p)
            self.assertEqual(data, {"a": 1})

    def test_update_json(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "test.json"
            write_json(p, {"a": 1, "b": 2})
            updated = update_json(p, {"b": 3, "c": 4})
            self.assertEqual(updated["b"], 3)
            self.assertEqual(updated["c"], 4)

    def test_increment_counter(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "test.json"
            write_json(p, {"counter": 5})
            inc = increment_counter(p)
            self.assertEqual(inc["counter"], 6)

    def test_increment_counter_missing(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "test.json"
            # file doesn't exist yet
            inc = increment_counter(p)
            self.assertEqual(inc["counter"], 1)


if __name__ == "__main__":
    unittest.main()
