'''
영상에 도형 그리고 글씨 쓰기
'''

import cv2 as cv
import sys

img=cv.imread("resource/soccer.jpg")

if img is None:
    sys.exit("파일을 찾을 수 없습니다.")


cv.rectangle(img,(451,185),(620,378),(0,255,0),2)
cv.putText(img,"KangIn",(451,175),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)

cv.imwrite("kangin_rectangle.jpg",img)

cv.imshow("Draw", img)

cv.waitKey()
cv.destroyAllWindows()

