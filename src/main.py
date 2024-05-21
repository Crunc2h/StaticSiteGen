from text_node import TextNode
from parent_node import ParentNode
from leaf_node import LeafNode
from html_node import HTMLNode
import re


text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
regx= r"!\[(.*?)\]\((.*?)\)"
test = re.findall(regx, "")
print(test)
regx_2 = r"\[(.*?)\]\((.*?)\)"
text_2 = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
test_2 = re.findall(regx_2, text_2)