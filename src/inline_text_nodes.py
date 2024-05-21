from text_node import TextNode
from text_types import TextType


class InlineTextNodes:
    
    def split_nodes_delimiter(old_nodes, delimiter, target_text_type):
        final_nodes = []
        for node in old_nodes:
            if node.text_type != TextType.RAW_TEXT:
                final_nodes.append(node)
            else:
                text_pieces = node.text.split(delimiter)
                if len(text_pieces) % 2 == 0:
                    raise ValueError(f"Closing delimiter \'{delimiter}\' not found, invalid md syntax.")
                else:
                    for i in range(len(text_pieces)):
                        if text_pieces[i] == "":
                            continue
                        elif i % 2 == 0:
                            final_nodes.append(TextNode(text=text_pieces[i],
                                                        text_type=TextType.RAW_TEXT))
                        else:
                            final_nodes.append(TextNode(text=text_pieces[i],
                                                        text_type=target_text_type))
        return final_nodes