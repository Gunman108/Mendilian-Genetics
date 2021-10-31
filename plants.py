import numpy as np 
import cv2

im = cv2.imread("f1_03.jpeg")

im = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

im = cv2.resize(im, (0,0),fx = 0.5, fy = 0.5)

lbound2 = np.array([50,80,0])
ubound2 = np.array([200,200,200])

lbound = np.array([0,80,0])
ubound = np.array([200,200,200])

# lbound2 = np.array([0,0,0])
# ubound2 = np.array([100,255,60])

mask1 = cv2.inRange(im, lbound, ubound)
mask2 = cv2.inRange(im, lbound2, ubound2)

# mask2 = cv2.inRange(im, lbound2, ubound2)



nlbound = np.array([0,0,0])
nubound = np.array([255,255,255])


# nmask = cv2.inRange(newim,)


cv2.imshow("1", im)
cv2.imshow("2", mask1)
cv2.imshow("3", mask2)

area = np.sum(mask1 == 255)  
cyan = np.sum(mask2 == 255)

percent = cyan/area

print(cyan)
print(area)
print(percent)

cv2.waitKey(0)