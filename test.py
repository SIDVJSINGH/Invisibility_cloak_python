import cv2 as cv
import numpy as np

video = cv.VideoCapture("video.mp4")
image = cv.imread("img.png")

while True:
  ret, frame = video.read() #while agr false hua to ret ho jaega vrna frame=video.read hoga matlab read ho jaega
  frame=cv.resize(frame, (640,480)) #video size is not known so we change both image and video size and make them same
  image= cv.resize(image, (640,480))
  hsv= cv.cvtColor(frame, cv.COLOR_BGR2HSV) #hsv ko lae hai
  
  l_g=np.array([32,94,132]) #these are trial and tested value jo result dengi shi dengi
  u_g=np.array([179,255,255])
  mask=cv.inRange(hsv, l_g,u_g) #mask ko hsv limits dia hai
  res=cv.bitwise_and(frame,frame, mask=mask) #and between frame and mask
  f=frame-res #subtract kia hai so hat result shi aae verna background aa rha tha aur person black tha
  g_screen=np.where(f==0, image, f) #jha f==0 hai vha image put kr do aur jha nhi hai vha f hi rehne do
  #cv.imshow("Frame", frame)
  #cv.imshow("mask",mask)
  #cv.imshow("RES", res)
  #cv.imshow("f",f)
  cv.imshow("Screen", g_screen)
  k=cv.waitKey(1) #1 key ka input lega
  if  k == ord('q'): #agr vo key 'q' hua to break kr dega verna chalta rhega
   break
  
video.release()
cv.destroyAllWindows()
