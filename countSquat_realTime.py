# import libraries
import os
import json
import cv2

# execute OpenPoseDemo.exe
# os.system('execute_op.bat')

# creating lists and variables for later use
midHip = []
y_list = []

squat = 0
neg_count = 0
pos_count = 0
lookfor_neg = True
lookfor_pos = False

# parsing json data
seriesNum = '0'
while True:
    for i in range(12 - len(seriesNum)): # adding extra 0 until there is 12 digits
        seriesNum = "0" + seriesNum
    fileName = seriesNum + '_' + 'keypoints' + '.json' # form the file name
    path = 'camera_output/' + fileName
    if os.path.isfile(path): # check if file exists
        fhandler = open(path)
        data = json.loads(fhandler.read())
        if data['people'] != []: # doc on the json data https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/output.md
            if data['people'][0]['pose_keypoints_2d'][3] > 0:
                y = (data['people'][0]['pose_keypoints_2d'][2]) 
                midHip.append(y)        
        # advance the serial number for 1
        intNum = int(seriesNum)
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
        print("you have done",squat,"squats")

    key = cv2.waitKey(1) & 0xFF # if press q stop the program
    if key == ord("q"):
        os.system('cmd /c "taskkill /IM OpenPoseDemo.exe /f"')
        break

