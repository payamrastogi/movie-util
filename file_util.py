import os

class FileUtil:
    @staticmethod
    def get_file_names(dir_path, file_extension):
        file_name_list = []
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file.endswith("." + file_extension):
                    file_name_list.append(os.path.join(root, file))
        file_name_list.sort()
        return file_name_list