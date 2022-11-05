import os
#os.system('ffmpeg -f concat -safe 0 -i ./data/list.txt -c copy stitched-video.mov && rm ./data/list.txt')

class BashUtil:

    @staticmethod
    def create_file_list(dir_path, file_ext):
        cmd = f"for f in {dir_path}/*.{file_ext} ; do echo file $f >> {dir_path}/list.txt; done"
        os.system(cmd)

    @staticmethod
    def merge(list_file_path, output_file_name):
        cmd = f"ffmpeg -f concat -safe 0 -i {list_file_path}/list.txt -c copy {list_file_path}/../output/{output_file_name}"
        os.system(cmd)

if __name__=="__main__":
    bash_util = BashUtil()
    # bash_util.create_file_list("/home/payam/workspace/movie-util/data", "mov")
    bash_util.merge("/home/payam/workspace/movie-util/data", "avatar-trailers.mov")