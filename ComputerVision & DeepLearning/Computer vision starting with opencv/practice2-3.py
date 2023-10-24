'''
영상 색상 변환하고 크기 축소하기
'''

import cv2 as cv
import sys

img=cv.imread('resource/soccer.jpg')

if img is None:
    sys.exit("파일을 찾을 수 없습니다.")

# 컬러 이미지를 명암 이미지로 변경
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# 이미지의 크기 조정
gray_small=cv.resize(gray,dsize=(0,0),fx=0.7, fy=0.7)

# 이미지 파일에 저장
cv.imwrite('soccer_gray.jpg', gray)
cv.imwrite('soccer_gray_small.jpg', gray_small)

cv.imshow('Color image', img)
cv.imshow('Gray image', gray)
cv.imshow('Gray image small', gray_small)

cv.waitKey()
cv.destroyAllWindows()
