import os
import time

STREAM_KEY = "drwc-z7mz-pm90-1h0h-bjqd"

cmd = f"ffmpeg -re -stream_loop -1 -i video.mp4 -c:v copy -c:a aac -b:a 160k -f flv rtmp://a.rtmp.youtube.com/live2/{STREAM_KEY}"

while True:
    os.system(cmd)
    time.sleep(5)
