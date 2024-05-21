


class HTMLNode:
    def __init__(self,
                 tag=None,
                 value=None,
                 children=None,
                 props=None):
        (self.tag, self.value, 
        self.children, self.props) = tag, value, children, props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props != None:
            props_as_html = ""
            for key, value in self.props.items():
                props_as_html += f" {key}=\"{value}\""
            return props_as_html
        else:
            return ""
    
    def __repr__(self):
        return f"""HTMLNode({self.tag},
        {self.value},
        {self.children},
        {self.props})"""
