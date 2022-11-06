from file_util import FileUtil
from download_util import DownloadUtil
from bash_util import BashUtil

class Main:
    def __init__(self):
        self.file_util = FileUtil()
        self.download_util = DownloadUtil()
        self.bash_util = BashUtil()

    def download_and_merge(self, movie_name, file_path, file_ext):
        url_list = self.file_util.get_urls(file_path)
        if url_list:
            for url in url_list:
                file_name,ext = self.file_util.get_file_name(url)
                if file_name:
                    file_name_location = f"/home/payam/workspace/movie-util/data/{movie_name}/{file_name}.{ext}"
                    self.download_util.download_file(url, file_name_location)
            self.bash_util.create_file_list(f"/home/payam/workspace/movie-util/data/{movie_name}", file_ext)
            self.bash_util.merge(f"/home/payam/workspace/movie-util/data/{movie_name}", f"{movie_name}.{file_ext}")

if __name__=="__main__":
    main = Main()
    main.download_and_merge("avatar-2022", "/home/payam/workspace/movie-util/input/avatar_trailers.txt", "mov")