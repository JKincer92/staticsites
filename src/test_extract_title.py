import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    
    def test_extract_title(self):
        markdown = "# test heading"
        self.assertEqual(extract_title(markdown), "test heading")

    def test_extract_title_exception(self):
        markdown = "$ not a heading"
        with self.assertRaises(Exception):
            extract_title(markdown)

    def test_extract_title_document(self):
        markdown = "#not a heading\n# h1 heading\n## h2 heading\n ### h3 heading"
        self.assertEqual(extract_title(markdown), "h1 heading")