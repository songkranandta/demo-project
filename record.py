from os import name
import cv2
import calendar
import sched,time

ts = calendar.timegm(time.gmtime())
cap = cv2.VideoCapture('rtsp://192.168.1.140:8554/unicast')
width = 1920
height = 1080
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

s = sched.scheduler(time.time, time.sleep)
record_status = True 
fourcc=cv2.VideoWriter_fourcc(*'XVID')
name = ts
out=cv2.VideoWriter('videos/Video_'+str(name)+'.avi',fourcc,25.0,(1920,1080))
time_stamp_static = ts




def write_video_name(message):
        f = open("recording_video.txt", "w")
        f.write(message)
        f.close()

class RecordVideo:
    write_video_name('Video_'+str(name)+'.avi')
    def record_interupts(self,sec):
        global time_stamp_static 
        global record_status
        if(time_stamp_static+sec <= calendar.timegm(time.gmtime())): 
            time_stamp_static = calendar.timegm(time.gmtime()); 
            record_status = False 
            print("interruts")

    def write_video_name(self,message):
        f = open("recording_video.txt", "a")
        f.write(message)
        f.close()       
    def __init__(self):
    
        global record_status
        global out
        while(cap.isOpened()):
            ret, frame = cap.read()
            if(ret==True):
                self.record_interupts(30) 
                if(record_status == True):
                    cv2.imshow('Camera_2',frame)
                    out.write(frame)
                else:
                    write_video_name('Video_'+str(calendar.timegm(time.gmtime()))+'.avi')

                    out=cv2.VideoWriter('videos/Video_'+str(calendar.timegm(time.gmtime()))+'.avi',fourcc,25.0,(int(cap.get(3)), int(cap.get(4))))
                    record_status = True 
                if(cv2.waitKey(1) & 0xFF == ord('q')):
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()
