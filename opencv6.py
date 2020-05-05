import cv2
#for image code

face_cascd = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# img = cv2.imread('Shooting-1.jpg')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# faces = face_cascd.detectMultiScale(gray,1.1,4)

# for (x,y,w,h) in faces:
# 	cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

# cv2.imshow('frame',img)
# cv2.waitKey()


#for video code

face_cascd = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
while cap.isOpened():
	_,img = cap.read()

	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	faces = face_cascd.detectMultiScale(gray,1.1,4)

	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

	cv2.imshow('frame',img)
	if cv2.waitKey(1)& 0xFF==ord('q'):
		break
	
cap.release()