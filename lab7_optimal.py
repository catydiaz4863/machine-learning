import numpy as np
a_b = np.array([12.52,25.2])
data = np.array([[2,81],[4,93],[6,91],[8,97]])
x = data[:,0]
y = data[:,1]

mse = sum(((a_b[0] * x + a_b[1])-y)**2)/4
#12,25
print(mse)
