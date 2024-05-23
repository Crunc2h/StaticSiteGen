import unittest
from src.functionality.text_node import TextNode
from src.functionality.text_types import TextType
from src.functionality.leaf_node import LeafNode


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
        
    def test_to_html(self):
        
        empty_raw_text_node = TextNode(text="", text_type=TextType.RAW_TEXT)
        non_empty_raw_text_node = TextNode(text="test", text_type=TextType.RAW_TEXT)
        bold_text_node = TextNode(text="test_bold", text_type=TextType.BOLD)
        italic_text_node = TextNode(text="test_italic", text_type=TextType.ITALIC)
        code_text_node = TextNode(text="test_code", text_type=TextType.CODE)
        link_text_node = TextNode(text="test_link", text_type=TextType.LINK, url="https://google.com")
        image_text_node = TextNode(text="test_image_alt_text", text_type=TextType.IMAGE, url="test_image_src_url")
        
        self.assertEqual(LeafNode(value=""), empty_raw_text_node.to_leaf_node())
        self.assertEqual(LeafNode(value="test"), non_empty_raw_text_node.to_leaf_node())
        self.assertEqual(LeafNode(tag="b", value="test_bold"), bold_text_node.to_leaf_node())
        self.assertEqual(LeafNode(tag="i", value="test_italic"), italic_text_node.to_leaf_node())
        self.assertEqual(LeafNode(tag="code", value="test_code"), code_text_node.to_leaf_node())
        self.assertEqual(LeafNode(tag="a", value="test_link", props={"href": "https://google.com"}), link_text_node.to_leaf_node())
        self.assertEqual(LeafNode(tag="img", value="", props={"src": "test_image_src_url",
                                                              "alt": "test_image_alt_text"}), image_text_node.to_leaf_node())

    
if __name__ == "__main__":
    unittest.main()