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

    @staticmethod
    def get_urls(file_path):
        with open(file_path, 'r') as f:
            url_list = f.read().splitlines()
        return url_list

    @staticmethod
    def get_file_name(url):
        if url:
            filename, ext = (url.split('/')[-1].split('.'))
            return filename, ext
        return None, None

if __name__=="__main__":
    file_util = FileUtil()
    lst = file_util.get_urls("/home/payam/workspace/movie-util/input/avatar_trailers.txt")
    print(lst)