'''
비디오에서 수집한 영상 이어 붙이기
'''

import cv2 as cv
import sys
import numpy as np

cap=cv.VideoCapture(0,cv.CAP_DSHOW)

if not cap.isOpened():
    sys.exit("카메라 연결 실패")

frames=[]   # 영상을 저장할 리스트 frames
while True:
    ret,frame=cap.read()

    if not ret:
        print("프레임 획득에 실패하여 루프를 나갑니다.")
        break

    cv.imshow("Video display",frame)

    key=cv.waitKey(1)
    # c가 입력되면 리스트에 프레임 추가
    if key == ord('c'):
        frames.append(frame)
    elif key == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

# 리스트에 프레임이 추가되었다면
if len(frames)>0:
    imgs=frames[0]
    for i in range(1,min(4,len(frames))):   # 최대 3프레임까지 이어 붙임
        imgs=np.hstack((imgs,frames[i]))

    cv.imshow("collected images",imgs)

    cv.waitKey()
    cv.destroyAllWindows()

# 리스트 요소 개수
print(len(frames))
# 저장된 첫 번째 영상의 배열 모양 (480, 640, 3)
print(frames[0].shape)
# 3장의 영상을 이어 붙인 이미지는 numpy.ndarray형
print(type(imgs))
# 3장의 이미지를 이어 붙인 이미지의 배열 모양 (480, 1920(640*3), 3)
print(imgs.shape)