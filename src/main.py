from textnode import TextNode
from textnode import TextType
from static_to_public import static_to_public
from generate_page import generate_page, generate_pages_recursive
import os
import sys

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
static_dir = os.path.join(project_root, "static")
docs_dir = os.path.join(project_root, "docs")
content_dir = os.path.join(project_root, "content")

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    test = TextNode("anchor", TextType.LINK , "website.com")
    print(test)
    static_to_public(static_dir, docs_dir)

    index_md_path = os.path.join(content_dir, "index.md")
    template_html_path = os.path.join(project_root, "template.html")
    output_html_path = os.path.join(docs_dir, "index.html")
    generate_pages_recursive(content_dir, template_html_path, docs_dir, basepath)




main()