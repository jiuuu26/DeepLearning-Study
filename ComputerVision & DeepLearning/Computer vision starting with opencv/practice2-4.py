'''
웹 캠에서 비디오 읽기
'''

import cv2 as cv
import sys

# 웹 캠과의 연결 시도
cap=cv.VideoCapture(0,cv.CAP_DSHOW)

# 웹 캠과 연결 실패시 cap에 False 저장
if not cap.isOpened():
    sys.exit("카메라 연결 실패")

while True:
    # read 함수를 호출한 순간의 프레임 획득
    ret, frame=cap.read()

    # 프레임 획득 실패시
    if not ret:
        print("프레임 획득에 실패하여 루프를 나갑니다.")
        break

    cv.imshow("Video display",frame)

    # 1ms 동안 키 입력 기다림
    key=cv.waitKey(1)

    # 'q' 입력하면 영상 종료
    if key==ord('q'):
        break

# 카메라와 연결 해제
cap.release()
cv.destroyAllWindows()