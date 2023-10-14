import numpy as np
import matplotlib.pyplot as plt

# Scatter function

x_train=np.array([1.0,2.0])
y_train=np.array([300.0, 500.0])

plt.scatter(x_train, y_train, marker='x', c='r', label='Actual Values')
plt.title("Housing Prices")
plt.ylabel("Price (in 1000s of dollars)")
plt.xlabel("Size(1000 sqft)")


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
