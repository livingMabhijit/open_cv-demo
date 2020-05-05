import cv2
import numpy as np
image_clr = cv2.imread('Shooting-1.jpg',1)
# image_clr = cv2.line(image_clr,(0,0),(255,255),(147,96,44),4)
# image_clr = cv2.arrowedLine(image_clr,(0,255),(255,255),(147,96,44),4)
image_clr = cv2.rectangle(image_clr,(330,0),(380,128),(255,0,0),5)#last parameter '-1' it will fill with the color
#image_clr = cv2.circle(image_clr,(330,0),(380,128),(255,0,0),5)
cv2.imshow('preview_image',image_clr)
cv2.waitKey(0)
cv2.destroyAllWindows()
