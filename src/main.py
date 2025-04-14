from textnode import TextNode
from textnode import TextType
from static_to_public import static_to_public
from generate_page import generate_page, generate_pages_recursive
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
static_dir = os.path.join(project_root, "static")
public_dir = os.path.join(project_root, "public")
content_dir = os.path.join(project_root, "content")

def main():
    test = TextNode("anchor", TextType.LINK , "website.com")
    print(test)
    static_to_public(static_dir, public_dir)

    index_md_path = os.path.join(content_dir, "index.md")
    template_html_path = os.path.join(project_root, "template.html")
    output_html_path = os.path.join(public_dir, "index.html")
    generate_pages_recursive(content_dir, template_html_path, public_dir)


main()