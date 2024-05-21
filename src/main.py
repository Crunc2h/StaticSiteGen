from text_node import TextNode
from parent_node import ParentNode
from leaf_node import LeafNode
from html_node import HTMLNode
from inline_text_node import InlineTextNode
from text_types import TextType
import re


text = """This is text with an\
![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)\
and\
![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png) AAAAND\
[this is def link](https://google.com)"""
test = TextNode(text=text, text_type=TextType.RAW_TEXT)










for image in InlineTextNode.split_nodes_image([test]):
    print(image)

print("-------")

for link in InlineTextNode.split_nodes_link([test]):
    print(link)
