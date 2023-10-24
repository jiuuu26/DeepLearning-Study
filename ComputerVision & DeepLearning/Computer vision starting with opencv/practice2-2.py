'''
영상 파일 읽고 윈도우에 디스플레이 하기 
'''

import cv2 as cv
import sys

# 영상 읽기
img=cv.imread("resource/soccer.jpg")

# 이미지 파일을 찾을 수 없으면 exit 함수로 프로그램 종료
if img is None:
    sys.exit("파일을 찾을 수 없습니다.")

# 윈도우에 영상 표시
cv.imshow("Image Display",img)

# 윈도우에 표시되는 시간 지정
cv.waitKey()

# 윈도우 닫기
cv.destroyAllWindows()

print(type(img))    #<class 'numpy.ndarray'>
print(img.shape)    #(1080, 1920, 3) <- 3차원 배열

#(0,0), (0,1)의 화소 조사
print(img[0,0,0],img[0,0,1],img[0,0,2])
print(img[0,1,0],img[0,1,1],img[0,1,2])


