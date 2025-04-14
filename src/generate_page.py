import os
import shutil
from pathlib import Path
from markdown_blocks import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as markdown_file:
        read_markdown = markdown_file.read()

    with open(template_path, 'r') as template_file:
        read_template = template_file.read()

    html_string = markdown_to_html_node(read_markdown).to_html()
    page_title = extract_title(read_markdown)
    final_content = read_template.replace('{{ Title }}', page_title)
    final_content = final_content.replace('{{ Content }}', html_string)
    final_content = final_content.replace('href="/', f'href="{basepath}')
    final_content = final_content.replace('src="/', f'src="{basepath}')

    with open(dest_path, 'w') as file:
        file.write(final_content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):

    for item in Path(dir_path_content).iterdir():
        if item.is_dir():
            dest_dir = Path(dest_dir_path) / item.name
            dest_dir.mkdir(parents=True, exist_ok=True)
            generate_pages_recursive(item, template_path, dest_dir, basepath)
        elif item.suffix == ".md":
            dest_file = Path(dest_dir_path) / (item.stem + ".html")
            generate_page(item, template_path, dest_file, basepath)


        


    
