from src.functionality.html_node import HTMLNode


class LeafNode(HTMLNode):
    
    def __init__(self, 
                 value, 
                 tag=None, 
                 props=None):
        
        if value is None:
            raise ValueError("No value passed to the leaf html node!")
        
        super().__init__(tag=tag, 
                         value=value, 
                         props=props)

    def to_html(self):
        
        if self.tag is None:
            return self.value if self.value != None else ""
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __eq__(self, other):
        return (self.value == other.value 
                and self.tag == other.tag
                and self.props == other.props)