"""JSON Schema syntax and required metadata tests."""

import json
import unittest

from mathbook.project import ROOT


class SchemaTests(unittest.TestCase):
    def test_all_schemas_are_draft_2020_12_objects(self) -> None:
        paths = sorted((ROOT / "schemas").glob("*.schema.json"))
        self.assertEqual(len(paths), 5)
        for path in paths:
            schema = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
            self.assertEqual(schema["type"], "object")
            self.assertIn("required", schema)
            self.assertIn("properties", schema)

    def test_schemas_cover_location_confidence_and_review(self) -> None:
        for path in sorted((ROOT / "schemas").glob("*.schema.json")):
            text = path.read_text(encoding="utf-8")
            self.assertIn("confidence", text)
            self.assertIn("review_status", text)
        text_block = json.loads((ROOT / "schemas/text-block.schema.json").read_text(encoding="utf-8"))
        self.assertIn("source_location", text_block["properties"])


if __name__ == "__main__":
    unittest.main()

