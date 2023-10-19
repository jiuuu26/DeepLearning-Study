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
