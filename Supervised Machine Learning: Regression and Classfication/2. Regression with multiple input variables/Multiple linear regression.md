[📝Multiple linear regression 내용정리](https://jiuuu.tistory.com/59)
<br></br>
## 💡Numpy 벡터화
### ✏️Vectors
#### [Abstract]  
 &nbsp; 벡터는 $\mathbf{x}$와 같이 소문자 bold체로 표시한다. 벡터는 수의 배열을 정리하며, 한 벡터 안의 요소는 type이 모두 같아야 한다. 수학에서 rank(행)이라고 불리는 것은 벡터에서 dimension이라고 표시될 수 있다. 참고로 수학에서는 인덱스가 1 ~ n(1부터 시작)으로 표시되지만, 컴퓨터에서는 0 ~ n-1 (0부터 시작)으로 표시된다.<br></br>

<b>[Numpy Arrays]</b>  
 &nbsp; 앞서 말했듯이 여기서 dimension은 벡터의 요소 수이자, 배열의 인덱스 수를 뜻한다. 1-D array에서 shape(n,)으로 표기되는 것은 n개의 요소를 가진 벡터를 뜻하게 되는 것이다. <br></br>

#### [Vector Creation]  

```python
import numpy as np

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
```
 - .shape은 몇 행 몇 열인지 반환  
 &nbsp; array([0,1,2]) -> (3,)
 &nbsp; array([0,1,2], [3,4,5]) -> (2,3)
 - .ndim은 몇 차원인지 반환  
 &nbsp; array([0,1,2]) -> 1
 &nbsp; array([0,1,2], [3,4,5]) -> 2
 - len(array)는 첫번째 차원의 개수 반환  

#### [Operations on Vectors]  
##### &nbsp; Indexing
 - Indexing : 배열 내의 자리로 해당 배열의 요소를 부르는 것  
```python
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
```  
  
##### &nbsp; Slicing
 - Slicing: 배열의 요소들에서 subset을 얻어내는 것 
 - (start : stop : step)  
```python
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
```

##### &nbsp; Single vector operations
```python
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
```   
##### &nbsp; Vector Vector element-wise operations
&nbsp; 배열끼리의 연산은 인덱스가 같은 요소들끼리 계산을 한다. 두 배열의 요소 개수가 맞지 않으면 error가 발생한다. 
```python
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
```

##### &nbsp; Scalar Vector operations
&nbsp; 벡터는 스칼라 값에 의해 값이 변경될 수 있다. 아래의 코드에서 스칼라는 벡터의 모든 요소들에 곱해진다.
```python
a=np.array([1,2,3,4])
b=5*a
print(f"a*5 : {b}")

'''
a*5 : [ 5 10 15 20]
'''
```

#### &nbsp; Vector Vector dot product
![image](https://github.com/jiuuu26/Artificial-Intelligence/assets/110098218/3ab2492b-706b-49f6-9899-b9687f2db563)

 &nbsp;dot product는 두 벡터의 차원이 같아야하며, 결과는 스칼라 값을 반환한다. 

```python
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
```

##### &nbsp; The Need for Speed: vector vs for loop
```python
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
```
&nbsp; 위 코드에서 볼 수 있듯이 벡터화는 속도를 굉장히 높여준다. 벡터화를 사용하면 하드웨어에서 병렬처리가 가능하기 때문이다. SIMD(Single Instruction Multiple Data) pipelines은 다중 계산을 병렬로 처리할 수 있게 한다. 이것은 머신러닝에서 데이터 셋의 크기가 매우 클 때 중요하다. 

<br></br>
### ✏️Matrices
#### [Abstract]
 &nbsp; 매트릭스는 2차원 배열이다. 벡터와 마찬가지로 매트릭스의 요소들은 모두 같은 type으로 구성되어 있다. 벡터는 소문자 bold체로 표현하는 반면, 매트릭스는 𝐗와 같은 대문자 bold체로 표현한다. 인덱스를 (1 ~ n)로 표현하는 수학과는 다르게 컴퓨터에서는 (0 ~ n-1)로 요소를 인덱싱한다.  
![image](https://github.com/jiuuu26/Artificial-Intelligence/assets/110098218/fc7930fe-a599-482d-baa5-16801d846f1f)
  
#### [Numpy Arrays]
&nbsp; matrices는 2차원(2-D)이며, index[m,n]을 가진다. m이 row(행)이고, n이 column(열)이다.

#### [Matrix Creation]
&nbsp; 1-D 벡터를 생성하는 함수로 2-D 또는 n-D 배열을 생성할 수 있다. 

```python
import numpy as np

# 0의 값으로 행렬 채우기
a=np.zeros((1,5))
print(f"a shape = {a.shape}, a= {a}")

a=np.zeros((2,1))
print(f"a shape = {a.shape}, a= {a}")

# 0-1 사이 랜덤 실수 값으로 행렬 채우기
a=np.random.random_sample((1,1))
print(f"a shape = {a.shape}, a= {a}")

'''
a shape = (1, 5), a= [[0. 0. 0. 0. 0.]]
a shape = (2, 1), a= [[0.]
                    [0.]]
a shape = (1, 1), a= [[0.61859012]]
'''
# 특정 값으로 행렬 생성
a=np.array([[5],[4],[3]])
print(f"a shape = {a.shape}, a= {a}")

a=np.array([[5],
            [4],
            [3]])
print(f"a shape = {a.shape}, a= {a}")

'''
a shape = (3, 1), a= [[5]
                     [4]
                     [3]]
a shape = (3, 1), a= [[5]
                     [4]
                     [3]]
'''
```

#### [Operations on Matrices]
##### Indexing
```python
# 인덱싱
a=np.arange(6).reshape(-1,2)
print(f"a.shape = {a.shape},\n a= {a}")
# 요소에 접근
print(f"a[2,0]shape = {a[2,0].shape}, a[2,0]= {a[2,0]}, type(a[2,0]) = {type(a[2,0])}")
# 행에 접근
print(f"a[2]shape = {a[2].shape}, a[2]= {a[2]}, type(a[2]) = {type(a[2])}")

'''
a.shape = (3, 2),
 a= [[0 1]
 [2 3]
 [4 5]]
a[2,0]shape = (), a[2,0]= 4, type(a[2,0]) = <class 'numpy.int32'>      
a[2]shape = (2,), a[2]= [4 5], type(a[2]) = <class 'numpy.ndarray'>   
'''
```

* reshape는 배열의 행과 열을 다시 지정할 때 사용한다. reshape(-1,2)에서 -1의 역할은 numpy 배열을 재구성할 때 해당 차원의 크기를 자동으로 계산해주는 것이다. 다른 차원의 크기와 남은 차원의 크기를 고려하여 자동으로 차원 크기를 계산해준다.  

##### Slicing
&nbsp; 벡터와 마찬가지로 slicing은 (start : stop : step) 값을 입력해주면 된다. 
```python
# 슬라이싱
a=np.arange(20).reshape(-1,10)
print(f"a = \n{a}")

print(f"a[0, 2:7:1] = {a[0, 2:7:1]}, a[0, 2:7:1].shape = {a[0, 2:7:1].shape}, a 1-D array")
print(f"a[:, 2:7:1] = {a[:, 2:7:1]}, a[:, 2:7:1].shape = {a[:, 2:7:1].shape}, a 2-D array")
print(f"a[:] = {a[:]}, a[:].shape = {a[:].shape}")
print(f"a[1,:] = {a[1,:]}, a[1,:].shape = {a[1,:].shape}, a 1-D array")
print(f"a[1] = {a[1]}, a[1].shape = {a[1].shape}, a 1-D array")

'''
a =
[[ 0  1  2  3  4  5  6  7  8  9]
 [10 11 12 13 14 15 16 17 18 19]]
a[0, 2:7:1] = [2 3 4 5 6], a[0, 2:7:1].shape = (5,), a 1-D array       
a[:, 2:7:1] = [[ 2  3  4  5  6]
 [12 13 14 15 16]], a[:, 2:7:1].shape = (2, 5), a 2-D array
a[:] = [[ 0  1  2  3  4  5  6  7  8  9]
 [10 11 12 13 14 15 16 17 18 19]], a[:].shape = (2, 10)
a[1,:] = [10 11 12 13 14 15 16 17 18 19], a[1,:].shape = (10,), a 1-D array
a[1] = [10 11 12 13 14 15 16 17 18 19], a[1].shape = (10,), a 1-D array
'''
```  
<br></br>
## 💡Multiple Variable Linear Regression

