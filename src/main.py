from text_node import TextNode
from parent_node import ParentNode
from leaf_node import LeafNode
from html_node import HTMLNode
from inline_text_node import InlineTextNode
from text_types import TextType
from block_markdown import BlockMarkdown
import re



from block_types import BlockTypes


md = """Headlines are simply done with hash chars like this:

# First Level Headline
![an image](https://pinterest.dase.com) with a surprise [link](https://surprise.com)

## Second *Level* Headline

### Third Level **Headline**

#### Fourth Level Headline

##### `Fifth Level` Headline
[image]a broken image link)

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

print(BlockMarkdown.markdown_to_html(md))





