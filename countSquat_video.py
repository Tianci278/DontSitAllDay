# import libraries
import os
import json

# making list for each point
midHip = []

# parsing json data
seriesNum = '0'
while True:
    for i in range(12 - len(seriesNum)): # adding extra 0 until there is 12 digits
        seriesNum = "0" + seriesNum
    fileName = 'input3' + '_' + seriesNum + '_' + 'keypoints' + '.json' # form the file name
    path = 'output3/' + fileName
    if os.path.isfile(path): # check if file exists
        data = open(path)
        data = json.loads(data.read())
        if data['people'] != []:
            if data['people'][0]['pose_keypoints_2d'][26] > 0:
                xy = (data['people'][0]['pose_keypoints_2d'][24], data['people'][0]['pose_keypoints_2d'][25]) # put x and y coordinate in a tuple
                midHip.append(xy)
    else:
        print("all files scanned")
        break
    intNum = int(seriesNum)
    intNum = intNum + 1
    seriesNum = str(intNum)

# calculate difference between digits
x_list = []
y_list = []
index = 1
for x,y in midHip:
    try:
        x_diff = x - midHip[index][0]
        y_diff = y - midHip[index][1]
    except:
        print("all calculation done")
    x_list.append(int(x_diff))
    y_list.append(int(y_diff))
    index += 1

# count squat
squat = 0
neg_count = 0
pos_count = 0
lookfor_neg = True
lookfor_pos = False
for y in y_list:
    if lookfor_neg is True:
        if y < 0:
            neg_count += 1
        else:
            neg_count = 0
        if neg_count == 7:
            lookfor_neg = False
            lookfor_pos = True
            neg_count = 0
    if lookfor_pos is True:
        if y > 0:
            pos_count += 1
        else:
            pos_count = 0
        if pos_count == 7:
            lookfor_neg = True
            lookfor_pos = False
            pos_count = 0
            squat += 1
print("you have done", squat, "squat.")
        
            
    
# force quit OpenPoseDemo.exe
# os.system('cmd /c "taskkill /IM OpenPoseDemo.exe /f"')
