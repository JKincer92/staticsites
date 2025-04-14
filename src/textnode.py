from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode
from extract_markdown import extract_markdown_images, extract_markdown_links

class TextType(Enum):
    TEXT = "text"
    BOLD = "*bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)    
       
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "",{'src': text_node.url, 'alt': text_node.text})
    else:
        raise ValueError(f"Invalid TextType: {text_node.text_type}")
    
def text_to_textnodes(text):
    from splitnodes import split_nodes_link, split_nodes_delimiter, split_nodes_image
    text_nodes = [TextNode(text, TextType.TEXT)]
    text_nodes = split_nodes_delimiter(text_nodes, "**", TextType.BOLD)
    text_nodes = split_nodes_delimiter(text_nodes, "_", TextType.ITALIC)
    text_nodes = split_nodes_delimiter(text_nodes, "`", TextType.CODE)
    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes)
    return text_nodes
