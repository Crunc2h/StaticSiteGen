import unittest
from block_markdown import BlockMarkdown

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        test= """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items"""

        self.assertEqual(BlockMarkdown.markdown_to_blocks(test),
                         ["This is **bolded** paragraph",
                          "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                          "* This is a list\n* with items"])
if __name__ == "__main__":
    unittest.main()