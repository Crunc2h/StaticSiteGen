from src.functionality.block_types import BlockTypes
from src.functionality.parent_node import ParentNode
from src.functionality.inline_markdown import InlineMarkdown


class BlockMarkdown:

    def extract_title_from_blocks(blocks):
        for block in blocks:
            for line in block:
                print(line)
                if line[0] == '#' and line[1] == ' ':
                    return line[1::]
        raise ValueError("No header found in the markdown file!")


    def markdown_to_html(md_text):
        
        blocks = BlockMarkdown.markdown_to_blocks(md_text)
        title = BlockMarkdown.extract_title_from_blocks(blocks)
        content = ParentNode(tag="div",
                             children=[BlockMarkdown.block_to_html_switch(block, BlockMarkdown.block_to_block_type(block)) for block in blocks])
        
        return content.to_html(), title

    def block_to_html_switch(block, block_type):
        
        if block_type == BlockTypes.PARAGRAPH:
            return BlockMarkdown.paragraph_to_html(block)
        elif block_type == BlockTypes.HEADING:
            return BlockMarkdown.heading_to_html(block)
        elif block_type == BlockTypes.CODE:
            return BlockMarkdown.code_to_html(block)
        elif block_type == BlockTypes.QUOTE:
            return BlockMarkdown.quote_to_html(block)
        elif block_type == BlockTypes.ORDERED_LIST:
            return BlockMarkdown.ordered_list_to_html(block)
        else:
            return BlockMarkdown.unordered_list_to_html(block)

    def heading_to_html(heading_block):
        
        heading_num = sum([1 for i in range(6) if heading_block[0][i] == '#'])
        heading_block[0] = heading_block[0][heading_num::]
        
        text = ' '.join(heading_block)
        text_nodes = InlineMarkdown.text_to_text_nodes(text)
        leaf_nodes = [text_node.to_leaf_node() for text_node in text_nodes]
        
        return ParentNode(tag=f"h{heading_num}",
                          children=leaf_nodes)

    def quote_to_html(quote_block):
        
        text = ' '.join([line.lstrip('>') for line in quote_block])
        text_nodes = InlineMarkdown.text_to_text_nodes(text)
        leaf_nodes = [text_node.to_leaf_node() for text_node in text_nodes]
        
        return ParentNode(tag="blockquote",
                          children=leaf_nodes)

    def unordered_list_to_html(uo_block):
        
        block_children = []
        for line in uo_block:
            text_nodes = InlineMarkdown.text_to_text_nodes(line[2::])
            leaf_nodes = [text_node.to_leaf_node() for text_node in text_nodes]
            
            block_children.append(ParentNode(tag="li",
                                             children=leaf_nodes))
        return ParentNode(tag="ul",
                          children=block_children)
    
    def ordered_list_to_html(o_block):
        
        block_children = []
        for line in o_block:
            text_nodes = InlineMarkdown.text_to_text_nodes(line[3::])
            leaf_nodes = [text_node.to_leaf_node() for text_node in text_nodes]
            
            block_children.append(ParentNode(tag="li",
                                             children=leaf_nodes))
        return ParentNode(tag="ol",
                          children=block_children)
        
    def code_to_html(code_block):
        
        text = ''.join(code_block)
        filtered_text = text[4:-3]
        
        text_nodes = InlineMarkdown.text_to_text_nodes(filtered_text)
        leaf_nodes = [text_node.to_leaf_node() for text_node in text_nodes]
        
        code_parent_node = ParentNode(tag="code",
                                      children=leaf_nodes)
        
        return ParentNode(tag="pre",
                          children=[code_parent_node])
    
    def paragraph_to_html(paragraph_block):
        
        text = ' '.join(paragraph_block)
        text_nodes = InlineMarkdown.text_to_text_nodes(text)
        leaf_nodes = [text_node.to_leaf_node() for text_node in text_nodes]
        
        return ParentNode(tag="p",
                          children=leaf_nodes)

    
    def block_to_block_type(block):
        
        found_types = [
            BlockMarkdown.__is_header(block),
            BlockMarkdown.__is_code(block),
            BlockMarkdown.__is_quote(block),
            BlockMarkdown.__is_unordered_list(block),
            BlockMarkdown.__is_ordered_list(block)
        ]
           
        if sum([1 for b_type in found_types if b_type == True]) > 1:
            raise ValueError("Invalid markdown, cannot mix types of lines within a block!")
        
        return BlockTypes.PARAGRAPH if any(found_types) is False else BlockTypes.BLOCK_TYPES[found_types.index(True)]
    
    def markdown_to_blocks(markdown):
        
        blocks = markdown.split("\n\n")
        blocks = [block.split('\n') for block in blocks if block.strip() != ""]
        return blocks
    
    def __is_header(block):
        
        for i in range(1, 7):
            if len(block[0]) >= i + 1:
                if (i * '#' + ' ') in block[0][:i+1]:
                    return True
        
        return False
    
    def __is_code(block):
        
        if (len(block[0]) >= 3 
        and len(block[-1]) >= 3
        and block[0][0:3] == "```" 
        and block[-1][-3::] == "```"):
            return True
        
        return False

    def __is_quote(block):
        
        for line in block:
            if line.startswith(">") is False:
                return False
        
        return True

    def __is_unordered_list(block):
        
        for line in block:
            if ((len(line) >= 2) 
                and (line[0] == "*" or line[0] == "-") 
                and (line[1] == " ")):
                continue
            return False 
        
        return True
    
    def __is_ordered_list(block):
        
        for i in range(len(block)):
            line = "".join(map(BlockMarkdown.__filter_ordered_list_char, block[i]))
            
            if (
            len(line[0:line.find(".")]) > 0
            and all(map(lambda letter: letter.isnumeric(), line[0:line.find(".")])) 
            and int(line[0:line.find(".")]) == i + 1
            and line[line.find(".") + 1] == " "
            ):
                continue
            return False
        
        return True
    
    def __filter_ordered_list_char(chr):
        
        if chr.isnumeric() or chr == "." or chr == " ":
            return chr
        return "*"
