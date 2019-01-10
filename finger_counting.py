import cv2
import numpy as np 


image_1 = cv2.imread('images/hand1.png',1)
image_1 = np.array(image_1)
img_hsv = cv2.cvtColor(image_1,cv2.COLOR_BGR2HSV)
img_hsv_1 = img_hsv.transpose((2,0,1))
# print(img_hsv_1.shape)
mask = np.zeros((image_1.shape[0],image_1.shape[1]),np.uint8)

H = img_hsv_1[0]

print(img_hsv.shape)
mask = cv2.inRange(img_hsv,np.array([0,10,0]),np.array([100,170,255]))
# mask = cv2.inRange()

mask = cv2.erode(mask,None,iterations = 3)
mask = cv2.dilate(mask,None,iterations = 4)

cv2.imshow('mask',mask)
# cv2.imshow('mask_1',mask_V)
# cv2.imshow('mask_2',mask_H)
num_hand, markers = cv2.connectedComponents(mask)
this_mask = []
for num in range(num_hand-1):
	hand_mask = np.zeros((mask.shape[0],mask.shape[1]),np.uint8)
	hand_mask[markers == num+1] = 255
	index = np.array(np.where(hand_mask==255))

	pos_y = index[0].min()
	pos_x = index[1].min()

	Trong_tam = (int(np.sum([i for i in index[1] ])/len(index[1])),int(np.sum([i for i in index[0] ])/len(index[0])))

	mask_1 = cv2.erode(hand_mask,None,iterations = 20)
	mask_1 = cv2.dilate(mask_1,None,iterations = 40)

	finger_mask = hand_mask-mask_1
	cv2.imshow('ngon',finger_mask)
	finger_mask[finger_mask != 255] = 0

	num_finger,makers = cv2.connectedComponents(finger_mask)
	for num in range(num_finger-1):
		index = np.where(makers==num+1)
		Trong_tam_ngon = ((int(np.sum([i for i in index[1] ])/len(index[1])),int(np.sum([i for i in index[0] ])/len(index[0]))))
		cv2.circle(image_1,Trong_tam_ngon,10,[255,0,0],-1)

	cv2.circle(image_1,Trong_tam,20,[0,255,0],-1)
	cv2.putText(image_1,str(num_finger-1),(pos_x,100),cv2.FONT_HERSHEY_COMPLEX,1,[0,0,255],1)


cv2.imshow('count',image_1)
cv2.waitKey()

