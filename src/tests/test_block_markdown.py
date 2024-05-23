import unittest
from src.conversion.block_markdown import BlockMarkdown

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        case_= """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items"""

        self.assertEqual(BlockMarkdown.markdown_to_blocks(case_),
                         [["This is **bolded** paragraph"],
                          ["This is another paragraph with *italic* text and `code` here",
                          "This is the same paragraph on a new line"],
                          ["* This is a list",
                          "* with items"]])

    def test_markdown_to_html(self):
        
        case_1_test = """Headlines are simply done with hash chars like this:

# First Level Headline
![an image](https://pinterest.dase.com) with a surprise [link](https://surprise.com)

## Second *Level* Headline

### Third Level **Headline**

#### Fourth Level Headline

##### `Fifth Level` Headline

###### Sixth Level Headline

For an unordered list use a dash

- like
- this
- nested
- list

Or use one asterix

* like
* this

For an ordered list use whatever number you want and add a dot:

1. like
2. this"""
        case_1_res = """<div><p>Headlines are simply done with hash chars like this:</p><h1> First Level Headline <img src="https://pinterest.dase.com" alt="an image"></img> with a surprise <a href="https://surprise.com">link</a></h1><h2> Second <i>Level</i> Headline</h2><h3> Third Level <b>Headline</b></h3><h4> Fourth Level Headline</h4><h5> <code>Fifth Level</code> Headline</h5><h6> Sixth Level Headline</h6><p>For an unordered list use a dash</p><ul><li>like</li><li>this</li><li>nested</li><li>list</li></ul><p>Or use one asterix</p><ul><li>like</li><li>this</li></ul><p>For an ordered list use whatever number you want and add a dot:</p><ol><li> like</li><li> this</li></ol></div>
"""
        
        self.maxDiff = None
        self.assertEqual(case_1_res, BlockMarkdown.markdown_to_html(case_1_test))



if __name__ == "__main__":
    unittest.main()