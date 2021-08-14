import os
import automatic
from record import RecordVideo
import time
import threading

RecordVideo()

def a():
    RecordVideo()
def b():
    while True:
        automatic.GoogleDriveUpload("/videos")
        time.sleep(30)

threading.Thread(target=a).start()
threading.Thread(target=b).start()