import unittest
from text_types import TextType
from inline_text_node import InlineTextNode
from text_node import TextNode
class TestInlineTextNode(unittest.TestCase):
    
    def test_split_nodes_delimiter(self):
        test_nodes = [TextNode(text="This is a test node with `python ./main.sh` code inside.",
                               text_type=TextType.RAW_TEXT),
                      TextNode(text="This is just a normal text node.", 
                               text_type=TextType.RAW_TEXT),
                      TextNode(text="This text node has **bold** words in it.",
                               text_type=TextType.RAW_TEXT)]
        self.assertEqual([TextNode(text="This is a test node with ", 
                                   text_type=TextType.RAW_TEXT),
                          TextNode(text="python ./main.sh", 
                                   text_type=TextType.CODE),
                          TextNode(text=" code inside.", 
                                   text_type=TextType.RAW_TEXT),
                          TextNode(text="This is just a normal text node.", 
                                   text_type=TextType.RAW_TEXT),
                          TextNode(text="This text node has **bold** words in it.", 
                                   text_type=TextType.RAW_TEXT)], InlineTextNode.split_nodes_delimiter(test_nodes, 
                                                                                                       "`", 
                                                                                                       TextType.CODE))
    
    def test_extract_markdown_images(self):
        test_empty = ""
        test_null = None
        test_img_text = """This is text with an\
![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)\
and\
![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"""
        self.assertRaises(TypeError, InlineTextNode.extract_markdown_images, test_null)
        self.assertEqual([], InlineTextNode.extract_markdown_images(test_empty)),
        self.assertEqual([("image",
                           "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                          ("another",
                           "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")],
                           InlineTextNode.extract_markdown_images(test_img_text))
    
    def test_extract_markdown_links(self):
        test_empty = ""
        test_null = None
        test_link_text = """This is text with a\
[link](https://www.example.com)\
and\
[another](https://www.example.com/another)"""
        self.assertRaises(TypeError, InlineTextNode.extract_markdown_links, test_null)
        self.assertEqual([], InlineTextNode.extract_markdown_links(test_empty)),
        self.assertEqual([("link",
                           "https://www.example.com"),
                          ("another",
                           "https://www.example.com/another")],
                           InlineTextNode.extract_markdown_links(test_link_text))