import os 
import pytube # pip install pytube 
from pytube.cli import on_progress 
url = "유튜브 링크" 
yt = pytube.YouTube(url, on_progress_callback=on_progress) 
print(yt.streams) 
save_dir = "./" # 저장경로 
yt.streams.filter(progressive=True, file_extension="mp4")\
    #  .order_by("resolution")\ 
    #  .desc()\ 
    #  .first()\ .
    #  download(save_dir)

# 출처: https://eehoeskrap.tistory.com/519 [Enough is not enough]