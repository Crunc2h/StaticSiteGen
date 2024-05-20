import unittest
from textnode import TextNode


class TestTExtNode(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(TextNode(text="This is a text node", text_type="bold"),
                         TextNode(text="This is a text node", text_type="bold"))
        self.assertEqual(TextNode(text="This is a text node", text_type="bold", url="This is a url"),
                         TextNode(text="This is a text node", text_type="bold", url="This is a url"))
        self.assertNotEqual(TextNode(text="This is a text node", text_type="bold"),
                            TextNode(text="This is a text node", text_type="italic"))
        self.assertNotEqual(TextNode(text="This is a text node", text_type="bold"),
                            TextNode(text="This is a text node", text_type="bold", url="This is a url"))
        self.assertNotEqual(TextNode(text="This is not a text node", text_type="bold"),
                            TextNode(text="This is a text node", text_type="italic"))
    
if __name__ == "__main__":
    unittest.main()