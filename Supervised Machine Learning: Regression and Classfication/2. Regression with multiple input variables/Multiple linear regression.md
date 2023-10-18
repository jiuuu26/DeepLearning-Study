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

   
