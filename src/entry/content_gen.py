from util.path_config import (PUBLIC_DIR,
                                  CONTENT_DIR,
                                  TEMPLATE_PATH)
from util.file_util import FileUtil
from conversion.block_markdown import BlockMarkdown



class ContentGen:
    

    def generate_content():
        FileUtil.copy_files_to_dest(src_dir_name=CONTENT_DIR,
                        dst_dir_name=PUBLIC_DIR)
        markdown_file_paths = [file_path for file_path in FileUtil.get_file_paths(CONTENT_DIR) if file_path[-2::] == "md"]

        for md_file_path in markdown_file_paths:
            dst_path = (PUBLIC_DIR + md_file_path.split(CONTENT_DIR)[1][:-3:] + ".html")

            ContentGen.generate_page(from_path=md_file_path,
                        dest_path=dst_path,
                        template_path=TEMPLATE_PATH)
            
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