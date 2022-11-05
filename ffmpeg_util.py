import ffmpeg


class FFMPEGUtil:
    @staticmethod
    def merge(file_name_list, output_dir, output_file_name):
        in_files=[]
        for file_name in file_name_list:
            in_file = ffmpeg.input(file_name)
            in_files.append(in_file["v"])
            in_files.append(in_file["a"])

        joined = ffmpeg.concat(*in_files, v=1, a=1).node
        video = joined[0]
        audio = joined[1]
        try:
            ffmpeg.output(audio, video, output_dir + "/" + output_file_name).overwrite_output().run()
        except Exception as e:
            print(e)
            return {"success": False, "message": str(e)}
        return {"success": True}

if __name__=="__main__":
    ffmpeg_util = FFMPEGUtil()
    lst = ["/home/payam/workspace/movie-util/data/avatar-the-way-of-water-trailer-1_h1080p.mov", "/home/payam/workspace/movie-util/data/avatar-the-way-of-water-trailer-3_h1080p.mov"]
    res = ffmpeg_util.merge(lst, "/home/payam/workspace/movie-util/output", "avatar-trailers.mov")
    print(res)