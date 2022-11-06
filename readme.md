#### Python movie editor
1. install ffmpeg
```
sudo apt install ffmpeg
```

2. Check installation by running the following command
```shell
ffmpeg
```

3. Merge all the videos in a folder
```shell
for f in *.mov ; do echo file \'$f\' >> list.txt; done && ffmpeg -f concat -safe 0 -i list.txt -c copy stitched-video.mov && rm list.txt
```

```python
import os
os.system('ffmpeg -f concat -safe 0 -i ./data/list.txt -c copy stitched-video.mov && rm ./data/list.txt')
```

# References
- https://pypi.org/project/ffmpeg-python/
- https://github.com/kkroening/ffmpeg-python
- https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
- https://www.geeksforgeeks.org/python-how-to-sort-a-list-of-strings/
- https://developers.google.com/youtube/v3/guides/uploading_a_video
- https://www.programcreek.com/python/example/117480/ffmpeg.input
- https://stackoverflow.com/questions/37748105/how-to-use-progressbar-module-with-urlretrieve
- https://janakiev.com/blog/python-shell-commands/
- https://stackoverflow.com/questions/15233340/getting-rid-of-n-when-using-readlines