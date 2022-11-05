import progressbar
import urllib.request

class DownloadUtil:

    @staticmethod
    def show_progress_bar(pbar, block_num, block_size, total_size):
        if pbar is None:
            pbar = progressbar.ProgressBar(maxval=total_size)
            pbar.start()

        downloaded = block_num * block_size
        if downloaded < total_size:
            pbar.update(downloaded)
        else:
            pbar.finish()

    def download_file(self, url, file_name, show_progress=False):
        if show_progress:
            urllib.request.urlretrieve(url, file_name, self.show_progress_bar)
        else:
            urllib.request.urlretrieve(url, file_name)

if __name__=="__main__":
    downloadUtil = DownloadUtil()
    downloadUtil.download_file("https://movietrailers.apple.com/movies/fox/avatar-the-way-of-water/avatar-the-way-of-water-trailer-3_h1080p.mov", "./avatar.mov")


