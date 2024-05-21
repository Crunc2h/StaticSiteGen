from text_types import TextType
from leaf_node import LeafNode

class TextNode:
    def __init__(self, 
                 text,
                 text_type,
                 url=None):
        if text_type.lower() not in TextType.TYPES:
            raise ValueError(f"Text type {text_type.lower()} is not supported.")
        self.text_type = text_type.lower()
        self.text = text if text != None else ""
        self.url = url

    def __eq__(self, other):
        return (self.text == other.text 
                and self.text_type == other.text_type 
                and self.url == other.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    def to_html(self):
        if self.text_type == TextType.RAW_TEXT:
            return LeafNode(value=self.text).to_html()
        elif self.text_type == TextType.BOLD:
            return LeafNode(tag="b", value=self.text).to_html()
        elif self.text_type == TextType.ITALIC:
            return LeafNode(tag="i", value=self.text).to_html()
        elif self.text_type == TextType.CODE:
            return LeafNode(tag="code", value=self.text).to_html()
        elif self.text_type == TextType.LINK:
            return LeafNode(tag="a", value=self.text, props={"href": self.url}).to_html()
        else:
            return LeafNode(tag="img", value="", props={"src": self.url,
                                                        "alt": self.text}).to_html()
    
    
                    



