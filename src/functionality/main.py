from functionality.block_markdown import BlockMarkdown


md = """Headlines are simply done with hash chars like this:

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

print(BlockMarkdown.markdown_to_html(md))





