import numpy as np
import time

# 0으로 1차원 배열 채우기
a=np.zeros(4)
print(f"np.zeros(4) : a={a}, a shape={a.shape}, a data type= {a.dtype}")
a=np.zeros((4,))
print(f"np.zeros(4,) : a={a}, a shape={a.shape}, a data type= {a.dtype}")
# 0-1 사이의 랜덤 값 4개로 배열 채우기 
a=np.random.random_sample(4)
print(f"np.random.random_sample(4) : a={a}, a shape={a.shape}, a data type= {a.dtype}")

'''
np.zeros(4) :   a = [0. 0. 0. 0.], a shape = (4,), a data type = float64
np.zeros(4,) :  a = [0. 0. 0. 0.], a shape = (4,), a data type = float64
np.random.random_sample(4): a = [0.70018832 0.16900018 0.74652737 0.28218562], a shape = (4,), a data type = float64
'''
# 0-3 정수로 배열 채우기
a=np.arange(4.)
print(f"np.arange(4) : a={a}, a shape={a.shape}, a data type= {a.dtype}")
# 0-1 사이 실수 랜덤 값 4개로 배열 채우기
a=np.random.rand(4)
print(f"np.random.rand(4) : a={a}, a shape={a.shape}, a data type= {a.dtype}")

'''
np.arange(4) : a=[0. 1. 2. 3.], a shape=(4,), a data type= float64    
np.random.rand(4) : a=[0.410572   0.32599046 0.11060213 0.68701873], a shape=(4,), a data type= float64
'''
# 특정한 값으로 배열 채우기
a=np.array([5,4,3,2])
print(f"np.array([5,4,3,2]) : a={a}, a shape={a.shape}, a data type= {a.dtype}")
a=np.array([5.,4,3,2])
print(f"np.array([5.,4,3,2]) : a={a}, a shape={a.shape}, a data type= {a.dtype}")

'''
np.array([5,4,3,2]) : a=[5 4 3 2], a shape=(4,), a data type= int32   
np.array([5.,4,3,2]) : a=[5. 4. 3. 2.], a shape=(4,), a data type= float64
'''

# Indexing
# 1차원, 10개의 요소 가진 배열 생성
a=np.arange(10)
print(a)

# 요소에 접근
print(f"a[2].shape: {a[2].shape}, a[2]={a[2]}")

# 마지막 요소에 접근. 음수 인덱스는 끝에서부터 시작
print(f"a[-1] = {a[-1]}")

# 벡터의 범위에 벗어난 인덱스를 입력하면 에러 발생
try:
    c=a[10]
except Exception as e:
    print("The error message you'll see is:")
    print(e)

# Slicing
# 1차원, 10개의 요소 가진 배열 생성
a=np.arange(10)
print(f"a    = {a}")

# 2~6까지의 요소들 출력
c=a[2:7:1]
print(f"a[2:7:1] = {c}")

# 2~6까지 2step으로 출력
c=a[2:7:2]
print(f"a[2:7:2] = {c}")

# 3~ 요소들 출력
c=a[3:]
print(f"a[3:]    = {c}")

# ~2까지의 요소들 출력
c=a[:3]
print(f"a[:3]   = {c}")

# 모든 요소 출력
c=a[:]
print(f"a[:]     = {c}") 

# vector operation
a=np.array([1,2,3,4])
print(f"a       : {a}")

# 배열 a의 요소들 모두 음수화
b=-a
print(f"b = -a   : {b}")

# 배열의 모든 요소 합계
b=np.sum(a)
print(f"b=np.sum(a) : {b}")

# 배열 요소들의 평균
b=np.mean(a)
print(f"b=np.mean(a) : {b}")

# 배열의 모든 요소에 제곱
b=a**2
print(f"b = a**2    : {b}")

'''
a       : [1 2 3 4]
b = -a   : [-1 -2 -3 -4]
b=np.sum(a) : 10
b=np.mean(a) : 2.5
b = a**2    : [ 1  4  9 16]
'''

# vector element-wise operation (벡터 간 원소끼리의 계산)
a=np.array([1,2,3,4])
b=np.array([-1,-2,-3,-4])
print(f"a + b = {a+b}")

# 두 배열의 요소 개수가 맞지 않을 때
c=np.array([1,2])
try:
    d=a+c
except Exception as e:
    print("The error message you'll see is: ")
    print(e)

'''
a + b = [0 0 0 0]
The error message you'll see is:
operands could not be broadcast together with shapes (4,) (2,)     
'''

a=np.array([1,2,3,4])
b=5*a
print(f"a*5 : {b}")

'''
a*5 : [ 5 10 15 20]
'''

# 반복문을 사용한 두 벡터 간의 곱
def my_dot(a,b):
    x=0
    for i in range (a.shape[0]):
        x=x+a[i]*b[i]
    return x

# 1차원 배열로 테스트
a=np.array([1,2,3,4])
b=np.array([-1,4,3,2])
print(f"my_dot(a,b) = {my_dot(a,b)}")

'''
my_dot(a,b) = 24
'''

# np.dot 사용
c=np.dot(a,b)
print(f"numpy 1차원 np.dot(a,b) = {c}, np.dot(a,b).shape = {c.shape}")
c=np.dot(b,a)
print(f"numpy 1차원 np.dot(b,a) = {c}, np.dot(b,a).shape = {c.shape}")

'''
numpy 1차원 np.dot(a,b) = 24, np.dot(a,b).shape = ()
numpy 1차원 np.dot(b,a) = 24, np.dot(b,a).shape = ()
'''

# vector vs for loop 속도 비교
np.random.seed(1)
# 매우 큰 배열 생성
a=np.random.rand(10000000)
b=np.random.rand(10000000)

tic=time.time()
c=np.dot(a,b)
toc=time.time()
print(f"np.dot(a,b) = {c: .4f}")    #소수점 4자리까지 출력
print(f"벡터화 버전 시간: {1000*(toc-tic):.4f}ms")

tic=time.time()
c=my_dot(a,b)
toc=time.time()
print(f"my_dot(a,b) = {c: .4f}")  
print(f"for 루프 버전 시간: {1000*(toc-tic):.4f}ms")

# 메모리에서 큰 배열 제거
del(a)
del(b)

'''
np.dot(a,b) =  2501072.5817
벡터화 버전 시간: 7.9291ms
my_dot(a,b) =  2501072.5817
for 루프 버전 시간: 2994.1206ms
'''
