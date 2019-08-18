# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 23:10:59 2019

@author: User
"""

import os
import cv2
import numpy as np

#os.chdir('G:\VIP CUP\Task-1\Activity Recognition(To train)\data')  #if you use spyder then set the path of the file

def adjust_gamma(image, gamma):
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
        for i in np.arange(0, 256)]).astype("uint8")
    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)


def video_from_dir(dir):
    temp=os.listdir(dir)
    video=[]
    for i in temp:
        if(i.endswith('.MP4')):
            video.append(i)
    return video


cur=os.getcwd()
cls_list_dir=os.path.join(cur,'noob')   #enter the name whatever the name of video parent_directory is instead of the string
cls_list=os.listdir(os.path.join(cur,'noob'))   #enter the name whatever the name of video parent_directory is instead of the string

new=os.path.join(cur,'Gamma_Corrected')

try: 
    os.makedirs(new, exist_ok = True) 
    #print("Directory '%s' created successfully" %directory) 
except OSError as error: 
    print("Directory '%s' can not be created")
#os.makedirs(new)
#cur=os.path.join(cur,'Gamma_Corrected')
cur=new
#for i,clas in enumerate(cls_list):
for i in range(len(cls_list)):
    print(cls_list[i])
    path=os.path.join(cur,cls_list[i])
    #os.makedirs(path)
    try: 
        os.makedirs(path, exist_ok = True) 
    #print("Directory '%s' created successfully" %directory) 
    except OSError as error: 
        print("Directory '%s' can not be created")
    
    sub_cls_dir=os.path.join(cls_list_dir,cls_list[i])
    sub_cls_list=os.listdir(sub_cls_dir)  #1_21_chat .....
    video=video_from_dir(sub_cls_dir)   ##1_21_chat
    for xy in range(len(video)):
        print(video[xy])
        #class_id=[[]]
        #name.append(video[xy])
        capture = cv2.VideoCapture(os.path.join(sub_cls_dir,video[xy]))
        fps = capture.get(cv2.CAP_PROP_FPS)
        size = (
        int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        )
        codec = cv2.VideoWriter_fourcc(*'MP4V')
        
        os.chdir(os.path.join(cur,cls_list[i]))
        output = cv2.VideoWriter(video[xy], codec, fps, size)
        ret, frame = capture.read()
        while(ret):
            img_processed =adjust_gamma(frame,1.25)
            if(fps>100):
                img_processed=cv2.flip(img_processed,-1)
            output.write(img_processed)
            #cv2.imshow('frame',img_processed)
            if cv2.waitKey(0) & 0xFF == ord('q'):
                break
            ret, frame = capture.read()
        capture.release()
        output.release()
        cv2.destroyAllWindows()
