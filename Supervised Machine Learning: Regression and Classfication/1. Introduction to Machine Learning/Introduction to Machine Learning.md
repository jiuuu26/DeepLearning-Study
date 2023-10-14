[📝 Introduction to Machine Learning 내용 정리](https://jiuuu.tistory.com/58)
<br></br>
## 💡Matplotlib 산점도 그리기
 &nbsp; Matplotlib.pyplot 모듈은 스타일로 동작하는 함수의 모음으로, 함수를 사용해서 간편하게 그래프를 만들고 변화를 줄 수 있다.  
 &nbsp; 산점도(Scatter plot)는 두 변수 상관 관계를 직교 좌표계의 평면에 점으로 표현하는 그래프이다. plt.scatter(x,y)을 기본 형식으로 하여 사용하며, 점의 색과 크기를 각각 c와 s로 다음과 같이 표현할 수 있다. plt.scatter(x, y, s=area, c=colors). 더하여 marker를 가지고 산점도의 모양을 정해줄 수도 있다. marker='x'로 하면 X로 표시되고, marker='o'를 하면 O로 표시된다.  
 &nbsp; matplot 라이브러리의 title, xlabel, ylabel로 그래프의 이름, x좌표, y좌표를 지정해줄 수 있으며 show()함수를 사용하여 산점도를 나타낼 수 있다.

```python
# Scatter function

x_train=np.array([1.0,2.0])
y_train=np.array([300.0, 500.0])

plt.scatter(x_train, y_train, marker='x', c='r', label='Actual Values')
plt.title("Housing Prices")
plt.ylabel("Price (in 1000s of dollars)")
plt.xlabel("Size(1000 sqft)")

```
## 💡Matplotlib 선 그리기
 &nbsp; plt.plot(x,y)을 기본 형식으로 하여 사용하며, scatter와 마찬가지로 c를 사용하여 색을 정해줄 수 있다. label로 선의 이름을 정할 수도 있으며 이는 legend() 함수로 그래프 범례를 표시할 수 있다. 
 
```python
# Model function

w=100
b=100

def compute_model_output(x,w,b):
    m=x.shape[0]
    f_wb=np.zeros(m)
    for i in range(m):
        f_wb[i]=w*x[i]+b

    return f_wb

tmp_f_wb=compute_model_output(x_train, w, b)

plt.plot(x_train, tmp_f_wb, c='b', label='Our prediction')
plt.legend()
plt.show()
```
