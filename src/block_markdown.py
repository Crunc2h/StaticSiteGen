from block_types import BlockTypes

class BlockMarkdown:

    def markdown_to_blocks(markdown):
        
        blocks = markdown.split("\n\n")
        blocks = [block.strip() for block in blocks if block.strip() != ""]
        return blocks
    
    def block_to_block_type(block):
        found_types = [
            BlockMarkdown.is_header(block),
            BlockMarkdown.is_code(block),
            BlockMarkdown.is_quote(block),
            BlockMarkdown.is_unordered_list(block),
            BlockMarkdown.is_ordered_list(block)
        ]
           
        if sum([1 for b_type in found_types if b_type == True]) > 1:
            raise ValueError("Invalid markdown, cannot mix types of lines within a block!")
        
        return BlockTypes.PARAGRAPH if any(found_types) is False else BlockTypes.BLOCK_TYPES[found_types.index(True)]
    
    def block_to_html():
        pass
    
    def is_header(block):
        for i in range(1, 7):
            if len(block[0]) >= i + 1:
                if (i * '#' + ' ') in block[0][:i+1]:
                    return True
        return False
    
    def is_code(block):
        if (len(block[0]) >= 3 
        and len(block[-1]) >= 3
        and block[0][0:3] == "```" 
        and block[-1][-3::] == "```"):
            return True
        return False

    def is_quote(block):
        for line in block:
            if line.startswith(">") is False:
                return False
        return True

    def is_unordered_list(block):
        for line in block:
            if len(line) >= 2:
                if line[0] == "*" or line[0] == "-":
                    if line[1] == " ":
                        continue
            return False 
        return True
    
    def is_ordered_list(block):
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
