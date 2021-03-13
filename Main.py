import cv2
import numpy as np
import talking_prog

# Definition of variables and lists
cap = cv2.VideoCapture(0)
thres = 0.5
nms_threshold = 0.2
font = cv2.FONT_HERSHEY_PLAIN # font
classNames = []  # list of objects which can be detected
classFiles = r'C:\Users\Electrical Dept\Downloads\MAKISATU\MAKISATU\Blind assistant\code\New Approach\coco.names'

# Reading the file
with open(classFiles, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n') # assigning into the ClassNames list
	
Colors = np.random.uniform(0, 255, size=(len(classNames), 3))

# locating the file of the model
MODEL_NAME = r'C:\Users\Electrical Dept\Downloads\MAKISATU\MAKISATU\Blind assistant\code\New Approach\ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weight = r'C:\Users\Electrical Dept\Downloads\MAKISATU\MAKISATU\Blind assistant\code\New Approach\frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weight, MODEL_NAME)
net.setInputSize(320, 320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

# loop
while True:
    success, img = cap.read()

    b, a, c = img.shape
    # allocating line coordinates
    left_coordinates = int( (a / 2) / 2)
    right_coordinates = int( (a / 2) + left_coordinates)

    #drawing vertical lines
    cv2.line(img, (left_coordinates, 0), (left_coordinates, b), (0, 255, 0), 5)
    cv2.line(img, (right_coordinates, 0), (right_coordinates, b), (0, 255, 0), 5)

    classIds, confs, bbox = net.detect(img,confThreshold=thres)
    bbox = list(bbox)
    confs = list(np.array(confs).reshape(1,-1)[0])
    confs = list(map(float,confs))
    #print(type(confs[0]))
    #print(confs)

    indices = cv2.dnn.NMSBoxes(bbox,confs,thres,nms_threshold)
    if len(classIds) != 0:
        for i in indices:
            i = i[0]
            box = bbox[i]
            confidence = str(round(confs[i]*100,2))
            color = Colors[classIds[i][0]-1]
            x,y,w,h = box[0],box[1],box[2],box[3]
            cv2.rectangle(img, (x,y), (x+w,y+h), color, thickness=2)
            cv2.putText(img, classNames[classIds[i][0]-1]+" "+confidence,(x+10,y+20),
                        font,1,color,2)
#             cv2.putText(img,str(round(confidence,2)),(box[0]+100,box[1]+30),
#                         font,1,colors[classId-1],2)
    cv2.imshow("Output",img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

