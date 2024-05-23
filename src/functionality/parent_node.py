from src.functionality.html_node import HTMLNode


class ParentNode(HTMLNode):
    
    def __init__(self, 
                 children, 
                 tag=None, 
                 props=None):
        
        if children is None:
            raise ValueError("No children passed to the parent html node!")
        
        super().__init__(tag=tag,
                         children=children,
                         props=props)
        
    def to_html(self):
        
        if self.tag is None:
            raise ValueError("Tag is required for parent html nodes!")
        else:
            nested_html = f"<{self.tag}{self.props_to_html()}>"
            for child in self.children:
                nested_html += child.to_html()
            nested_html += f"</{self.tag}>"
            return nested_html




            