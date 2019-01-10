# Finger_Counting
Count number of fingers in the image

![Alt text](Images/hand1.png?raw=true "Hand no.1")

![Alt text](Images/hand2.png?raw=true "Hand no.2")

# Algorithm
- Step1. Read input image.
- Step2. Convert image to HSV color space and use H channel for skin-color detection.
- Step3. Segment out areas with skin color value (mask = cv2.inRange(img_hsv,np.array([0,10,0]),np.array([100,170,255]))).
![Alt text](Images/HSV_THRESHOLD.PNG?raw=true "HANDS_THRESHOLDING")
- Step4. Use erosion and delation to erase small components.
- Step5. Find centroid of each hand.
- Step6. Do erosion until just fingers are left.
![Alt text](Images/finger.png?raw=true "finger")
- Step7. Count number of fingers and find centroid of each finger.

# Output
![Alt text](Images/output.png?raw=true "output")

# Dependencies
- opencv
- numpy
