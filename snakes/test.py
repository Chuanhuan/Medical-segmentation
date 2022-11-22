import numpy as np
import snake as sn
import matplotlib.pyplot as plt


a1  = np.random.randint(0,10,size=(5,4))
print(a1)


a1_g = np.gradient(a1)
print(a1_g)

fx, fy = sn.create_external_edge_force_gradients_from_img(a1)
fx



t = np.arange(0, 2*np.pi, 0.1)
x = 120+50*np.cos(t)
y = 140+60*np.sin(t)


fig = plt.figure()
ax  = fig.add_subplot(111)
plt.scatter(x, y)
plt.show()


img = np.load('./img.npy')
plt.imshow(img)

alpha = 0.001
beta = 0.4
gamma = 100
iterations = 50

A = sn.create_A(alpha , beta, x.shape[0])