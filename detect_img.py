import cv2
import numpy as np
def func():
   gray_img = cv2.imread('./images/center.png',cv2.IMREAD_GRAYSCALE)
   cv2.imshow('gray',gray_img)


   rect_img = cv2.rectangle(gray_img, (150,543),(199,604),(0,0,255),3)
   rect_img = cv2.rectangle(gray_img, (381,540),(437,602),(0,0,255),3)

   cv2.imshow('rect',rect_img)

   left_img = gray_img[150:199, 543:604]
   right_img = gray_img[381:437, 540:602]

   if np.all(left_img <90):
      print('Right')
      pass
   if np.all(right_img < 90):
      print('left')
      pass

   cv2.waitKey(0)


if __name__ == '__main__':
   func()
   pass
     
