import re
from src.functionality.text_node import TextNode
from src.functionality.text_types import TextType


class InlineMarkdown:

    REGX_IMAGE = r"!\[(.*?)\]\((.*?)\)"
    REGX_LINK = r"(?<!!)\[(.*?)\]\((.*?)\)"
    
    TEXT_DELIMITERS = [("**", TextType.BOLD),
                       ("*", TextType.ITALIC),
                       ("`", TextType.CODE)]

    def text_to_text_nodes(text):
        
        root = TextNode(text=text, text_type=TextType.RAW_TEXT)
        all_nodes = [root]
        
        for delimiter, text_type in InlineMarkdown.TEXT_DELIMITERS:
            all_nodes = InlineMarkdown.split_nodes_delimiter(all_nodes, delimiter, text_type)
        
        all_nodes = InlineMarkdown.split_nodes_image(all_nodes)
        all_nodes = InlineMarkdown.split_nodes_link(all_nodes)

        return all_nodes
        
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
    
    def split_nodes_image(old_nodes):
        
        new_nodes = []
        for node in old_nodes:
            if node.text_type != TextType.RAW_TEXT:
                new_nodes.append(node)
                continue
            
            original_text = node.text
            image_contents = InlineMarkdown.extract_markdown_images(original_text)
            
            if len(image_contents) == 0:
                new_nodes.append(node)
                continue
            else:
                for image_content in image_contents:
                    content_string = f"![{image_content[0]}]({image_content[1]})"
                    sections = original_text.split(content_string, 1)
                    
                    if len(sections) != 2:
                        raise ValueError("Invalid markdown, image section not closed")
                    
                    if sections[0] != "":
                        new_nodes.append(TextNode(text=sections[0],
                                                  text_type=TextType.RAW_TEXT))
                    
                    new_nodes.append(TextNode(text=image_content[0],
                                              text_type=TextType.IMAGE,
                                              url=image_content[1]))
                    original_text = sections[1]
                
                if original_text != "":
                    new_nodes.append(TextNode(text=original_text,
                                              text_type=TextType.RAW_TEXT))
        
        return new_nodes
    
    def split_nodes_link(old_nodes):
        
        new_nodes = []
        for node in old_nodes:
            if node.text_type != TextType.RAW_TEXT:
                new_nodes.append(node)
                continue
            
            original_text = node.text
            link_contents = InlineMarkdown.extract_markdown_links(original_text)
            
            if len(link_contents) == 0:
                new_nodes.append(node)
                continue
            else:
                for link_content in link_contents:
                    content_string = f"[{link_content[0]}]({link_content[1]})"
                    sections = original_text.split(content_string, 1)
                    
                    if len(sections) != 2:
                        raise ValueError("Invalid markdown, link section not closed")
                    
                    if sections[0] != "":
                        new_nodes.append(TextNode(text=sections[0],
                                                  text_type=TextType.RAW_TEXT))
                    
                    new_nodes.append(TextNode(text=link_content[0],
                                              text_type=TextType.LINK,
                                              url=link_content[1]))
                    original_text = sections[1]
                
                if original_text != "":
                    new_nodes.append(TextNode(text=original_text,
                                              text_type=TextType.RAW_TEXT))
        return new_nodes
    
    def extract_markdown_images(text):
        return re.findall(InlineMarkdown.REGX_IMAGE, text)
    
    def extract_markdown_links(text):
        return re.findall(InlineMarkdown.REGX_LINK, text)