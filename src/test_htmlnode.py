import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        self.assertEqual(HTMLNode().props_to_html(), None)
        self.assertEqual(HTMLNode(props={"href": "https://google.com"}).props_to_html(), 
                         " href=\"https://google.com\"")


if __name__ == "__main__":
    unittest.main()