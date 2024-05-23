import os
import shutil


class FileUtil:

    def get_file_paths(src_dir_name):
        paths = []
        for path in os.listdir(src_dir_name):
            abs_path = os.path.join(src_dir_name, path)
            if os.path.isfile(abs_path):
                paths.append(abs_path)
            else:
                if os.path.isdir(abs_path):
                    paths.extend(FileUtil.get_file_paths(abs_path))
        
        return paths

    def get_subdirectory_from_file_path(file_path, root_path):
        return '/' + '/'.join(file_path.split(root_path)[1].split('/')[:-1])

    def copy_files_to_dest(src_dir_name, dst_dir_name):
        
        if os.path.exists(src_dir_name) is False:
            raise NameError("No such directory.")
        
        file_paths = FileUtil.get_file_paths(src_dir_name)

        if os.path.exists(dst_dir_name):
            shutil.rmtree(dst_dir_name)
        
        os.mkdir(dst_dir_name)
        
        subdirectories = set([FileUtil.get_subdirectory_from_file_path(file_path, src_dir_name) for file_path in file_paths])
        for subdirectory in subdirectories:
            
            abs_sub_path = dst_dir_name + subdirectory
            if os.path.exists(abs_sub_path) is False:
                os.mkdir(abs_sub_path)

        for path in file_paths:  
            file_path_from_dst_dir = '/' + '/'.join((dst_dir_name + path.split(src_dir_name)[1]).split('/')[1:-1])
            shutil.copy(path, file_path_from_dst_dir)