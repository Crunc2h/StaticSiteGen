import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_init(self):
        self.assertRaises(ValueError, LeafNode, None)
    
    def test_to_html(self):
        self.assertEqual(LeafNode(value="test").to_html(), "test")
        self.assertEqual(LeafNode(tag="a",
                                  value="test",
                                  props={"href": "https://google.com"}).to_html(), "<a href=\"https://google.com\">test</a>")
        
if __name__ == "__main__":
    unittest.main()