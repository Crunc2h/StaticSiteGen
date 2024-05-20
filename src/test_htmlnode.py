import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        dummy = self.__create_dummy(is_none=False)
        self.assertEqual(dummy.props_to_html(),
                         "".join([f" {key}=\"{value}\"" for key, value in dummy.props.items()]))
    


    def __create_dummy(self, is_none):
        if is_none:
            return HTMLNode()
        else:
            test_tag = "<a>"
            test_value = "This is a val"
            test_children = [HTMLNode(), HTMLNode()]
            test_props = {"href": "https://google.com"}
            return HTMLNode(tag=test_tag,
                            value=test_value,
                            children=test_children,
                            props=test_props)

if __name__ == "__main__":
    unittest.main()