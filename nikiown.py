import face_recognition as fr
#fr is wrapper for dlib working on hog and svm
import cv2
#opencv

import numpy as np #self explanatory
import os #to find paths,make output file
import csv

target_row='dominant 1'

with open("./result.csv","r") as file:
    csvreader=csv.DictReader(file)
    for row in csvreader:
        if target_row in row:
            value=row[target_row]
            #print(value)

value=value[1:7]
#print (value)

rgb_skin= tuple(int(value[i:i+2],16) for i in (0, 2, 4))
print ("Your skin tone is:", str(rgb_skin))
x=rgb_skin

if rgb_skin[0]>82 and rgb_skin[0]<240:
    undertone='warm'
else:
    undertone='cool'

if rgb_skin[1]>43 and rgb_skin[1]<208:
    undertone='warm'
else:
    undertone='cool'

if rgb_skin[2]>28 and rgb_skin[2]<185:
    undertone='warm'
else:
    undertone='cool'

#test_image='./test/test.jpg'
test_image='./skintone/test.jpeg'
image=cv2.imread(test_image)

face_locations=fr.face_locations(image)
face_encodings=fr.face_encodings(image,face_locations)

for(top,right,bottom,left),face_encoding in zip(face_locations,face_encodings):


    #cv2.rectangle(image,(left,top),(right,bottom),(0,0,0))
    cv2.rectangle(image,(left,top-15),(right,top),(0,0,0),cv2.FILLED)
    font=cv2.FONT_HERSHEY_PLAIN
    cv2.putText(image,undertone+ ' undertone',(left+6,top-6),font,1.0,(255,255,255),1)


cv2.imshow('Result',image)
cv2.imwrite('./output.jpg',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
