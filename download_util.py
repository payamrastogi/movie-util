import urllib.request

class DownloadUtil:

    @staticmethod
    def download_file(url, file_name):
        urllib.request.urlretrieve(url, file_name)

if __name__=="__main__":
    downloadUtil = DownloadUtil()
    downloadUtil.download_file("https://movietrailers.apple.com/movies/fox/avatar-the-way-of-water/avatar-the-way-of-water-trailer-3_h1080p.mov", "./avatar.mov")


