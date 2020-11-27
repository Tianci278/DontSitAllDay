'''Every an hour, this program will force you to do 30 squats within 10 mins, failed to do so will sleep this computer'''

# import libraries
import os
import json
import subprocess as sp
import time
import shutil

waitTime = 0 # seconds, the interval time between the program forces you to do squats
numOfSquats = 10 # number of squats you have to do to prevent the computer from sleeping
finishWithin = 10 # minutes, you have to finish the squats within the time


def countSquat(n,f):
    # creating lists and variables for later use
    midHip = []
    y_list = []
    
    squat = 0
    neg_count = 0
    pos_count = 0
    lookfor_neg = True
    lookfor_pos = False
    seriesNum = '0'
    
    while True:
        # parsing json data while after new json file is generated
        for i in range(12 - len(seriesNum)): # adding extra 0 until there is 12 digits
            seriesNum = "0" + seriesNum
        fileName = seriesNum + '_' + 'keypoints' + '.json' # form the file name
        path = 'camera_output/' + fileName
        if os.path.isfile(path): # check if file exists
            try: # the handler might open an empty file I dont know why, try & except are here to prevent error meg.
                fhandler = open(path)
            except:
                continue
            data = json.loads(fhandler.read())
            if data['people'] != []: # doc on the json data https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/output.md
                if data['people'][0]['pose_keypoints_2d'][26] > 0:
                    y = (data['people'][0]['pose_keypoints_2d'][25]) 
                    midHip.append(y)        
            intNum = int(seriesNum) # advance the serial number for 1
            intNum = intNum + 1
            seriesNum = str(intNum)
    
            # calculate difference between digits
            if len(midHip) >= 2:
                diff = midHip[-1] - midHip[-2]
                y_list.append(diff)
    
            # counting 7 conexcutive negative number then counting 7 conexcutive positive number then it is one squat
            if y_list != []:
                if lookfor_neg is True:
                    if y_list[-1] < 0:
                        neg_count += 1
                    else:
                        neg_count = 0
                    if neg_count == 5:
                        lookfor_neg = False
                        lookfor_pos = True
                        neg_count = 0
                if lookfor_pos is True:
                    if y_list[-1] > 0:
                        pos_count += 1
                    else:
                        pos_count = 0
                    if pos_count == 5:
                        lookfor_neg = True
                        lookfor_pos = False
                        pos_count = 0
                        squat += 1
                        
        # when t times squats are done, return True and break out the loop
        if n == squat: 
            fhandler.close()
            break
        
# main function

# go back to parental directory
os.chdir('..')                        

time.sleep(waitTime)
# execute OpenPoseDemo.exe as it will detect and export body joints json data in folder camera_output
sp.Popen("execute_op.bat")
countSquat(numOfSquats,finishWithin)
print('success!')
os.system('taskkill /IM "OpenPoseDemo.exe" /F')
shutil.rmtree('camera_output')
