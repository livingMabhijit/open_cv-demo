import cv2
import numpy as np
image_clr = cv2.imread('lena.jpg',0)
cv2.imshow('preview_image',image_clr)
key = cv2.waitKey(0)
if key ==27:
	#on ESC button window willl be destroyd
	cv2.destroyAllWindows()
elif key==ord('s'):
	#write the transformed image on press of 'S'
	cv2.imwrite('gray_lena.jpg',image_clr)
	cv2.destroyAllWindows()



