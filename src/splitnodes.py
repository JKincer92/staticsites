from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        extracted_images = extract_markdown_images(node.text)
        remaining_text = node.text
        
        if not extracted_images:
            new_nodes.append(node)
            continue
        
        for image_alt, image_link in extracted_images:
            before_text, remaining_text = remaining_text.split(f"![{image_alt}]({image_link})", 1)
            
            if len(before_text) > 0:
                new_nodes.append(TextNode(before_text, TextType.TEXT))
            
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
    
        if len(remaining_text) > 0:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes
        
            

                    


def split_nodes_link(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        extracted_links = extract_markdown_links(node.text)
        remaining_text = node.text
        
        if not extracted_links:
            new_nodes.append(node)
            continue
        
        for href, link in extracted_links:
            before_text, remaining_text = remaining_text.split(f"[{href}]({link})", 1)
            
            if len(before_text) > 0:
                new_nodes.append(TextNode(before_text, TextType.TEXT))
            
            new_nodes.append(TextNode(href, TextType.LINK, link))
    
        if len(remaining_text) > 0:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    
    return new_nodes