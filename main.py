import os
import shutil
import time
from src.functionality.block_markdown import BlockMarkdown

ROOT_DIR = "/home/_lghtbringer/workspace/github.com/Crunc2h/SSiteGen/"
PUBLIC_DIR = ROOT_DIR + "public/"
CONTENT_DIR = ROOT_DIR + "content/"
TEMPLATE_PATH= ROOT_DIR + "template.html"



def get_file_paths(src_dir_name):
    paths = []
    for path in os.listdir(src_dir_name):
        abs_path = os.path.join(src_dir_name, path)
        if os.path.isfile(abs_path):
            paths.append(abs_path)
        else:
            if os.path.isdir(abs_path):
                paths.extend(get_file_paths(abs_path))
    
    return paths

def get_subdirectory_from_file_path(file_path, root_path):
    return '/' + '/'.join(file_path.split(root_path)[1].split('/')[:-1])

def copy_files_to_dest(src_dir_name, dst_dir_name):
    
    if os.path.exists(src_dir_name) is False:
        raise NameError("No such directory.")
    
    file_paths = get_file_paths(src_dir_name)

    if os.path.exists(dst_dir_name):
        shutil.rmtree(dst_dir_name)
    
    os.mkdir(dst_dir_name)
    
    subdirectories = set([get_subdirectory_from_file_path(file_path, src_dir_name) for file_path in file_paths])
    for subdirectory in subdirectories:
        
        abs_sub_path = dst_dir_name + subdirectory
        if os.path.exists(abs_sub_path) is False:
            os.mkdir(abs_sub_path)

    for path in file_paths:  
        file_path_from_dst_dir = '/' + '/'.join((dst_dir_name + path.split(src_dir_name)[1]).split('/')[1:-1])
        shutil.copy(path, file_path_from_dst_dir)


def generate_page(template_path, from_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as content_file:
        with open(template_path) as template_file:
            with open(dest_path, "w+t") as dest_file:
                content_md = content_file.read()
                template = template_file.read()
                content_html, title = BlockMarkdown.markdown_to_html(content_md)
                res_str = template.replace(r"{{ Content }}", content_html).replace(r"{{ Title }}", title)
                dest_file.write(res_str)


def generate_content():
    copy_files_to_dest(src_dir_name=CONTENT_DIR,
                       dst_dir_name=PUBLIC_DIR)
    markdown_file_paths = [file_path for file_path in get_file_paths(CONTENT_DIR) if file_path[-2::] == "md"]
    print(markdown_file_paths)
    for md_file_path in markdown_file_paths:
        dst_path = (PUBLIC_DIR + md_file_path.split(CONTENT_DIR)[1][:-3:] + ".html")
        print(dst_path)
        print("=======")
        generate_page(from_path=md_file_path,
                      dest_path=dst_path,
                      template_path=TEMPLATE_PATH)


generate_content()

