import cv2 as cv
import numpy as np

video = cv.VideoCapture("video.mp4")
image = cv.imread("img.png")

while True:
  ret, frame = video.read()
  frame=cv.resize(frame, (640,480))
  image= cv.resize(image, (640,480))
  hsv= cv.cvtColor(frame, cv.COLOR_BGR2HSV)
  
  l_g=np.array([32,94,132])
  u_g=np.array([179,255,255])
  mask=cv.inRange(hsv, l_g,u_g)
  res=cv.bitwise_and(frame,frame, mask=mask)
  f=frame-res
  g_screen=np.where(f==0, image, f)
  #cv.imshow("Frame", frame)
  #cv.imshow("mask",mask)
  #cv.imshow("RES", res)
  #cv.imshow("f",f)
  cv.imshow("Screen", g_screen)
  k=cv.waitKey(1)
  if  k == ord('q'):
   break
  
video.release()
cv.destroyAllWindows()
