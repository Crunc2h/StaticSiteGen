from text_node import TextNode
from parent_node import ParentNode
from leaf_node import LeafNode
from html_node import HTMLNode
from inline_text_node import InlineTextNode
from text_types import TextType
import re




test = InlineTextNode.text_to_text_nodes(text)
for t in test:
    print(t)
"""
print(InlineTextNode.split_nodes_delimiter([TextNode(text=text,text_type=TextType.RAW_TEXT)], "**", TextType.BOLD))
"""