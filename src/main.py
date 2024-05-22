from text_node import TextNode
from parent_node import ParentNode
from leaf_node import LeafNode
from html_node import HTMLNode
from inline_text_node import InlineTextNode
from text_types import TextType
from block_markdown import BlockMarkdown
import re



from block_types import BlockTypes


block = [
    "``` asfasg",
    ">    asdfa",
    "> asfsa```"
]

print(BlockMarkdown.block_to_block_type(block))





