import unittest
from parent_node import ParentNode
from leaf_node import LeafNode


class TestParentNode(unittest.TestCase):
    def test_parent_node(self):
        leaf_1 = LeafNode(value="lnode", 
                          tag="p1")
        leaf_2 = LeafNode(value="lnode", 
                          tag="p2", 
                          props={"class": "layer_1"})
        leaf_3 = LeafNode(value="")
        parent_1 = ParentNode(tag="h1", children=[leaf_1, leaf_2, leaf_3])
        self.assertEqual(parent_1.to_html(),
                         """<h1>\
<p1>lnode</p1>\
<p2 class=\"layer_1\">lnode</p2>\
</h1>""")
        
        parent_2 = ParentNode(tag="h2", children=[leaf_1], props={"class": "parent_l1"})
        parent_3 = ParentNode(tag="h3", children=[leaf_3], props={"class": "parent_l2"})
        parent_4 = ParentNode(tag="h4", children=[parent_3], props={"class": "parent_l1"})
        parent_5 = ParentNode(tag="h1", children=[parent_2, parent_4, leaf_1], props={"class": "parent_l0"})
        self.assertEqual(parent_5.to_html(),
                         """<h1 class=\"parent_l0\">\
<h2 class=\"parent_l1\">\
<p1>lnode</p1>\
</h2>\
<h4 class=\"parent_l1\">\
<h3 class=\"parent_l2\">\
</h3>\
</h4>\
<p1>lnode</p1>\
</h1>""")

if __name__ == "__main__":
    unittest.main()



