import numpy as np
import matplotlib.pyplot as plt
import snake as sn

img = np.load('./snakes/img.npy')

t = np.arange(0, 2*np.pi, 0.1)
x = 120+50*np.cos(t)
y = 140+60*np.sin(t)

alpha = 0.001
beta = 0.4
gamma = 100
iterations = 50

# fx and fy are callable functions
fx, fy = sn.create_external_edge_force_gradients_from_img( img )

snakes = sn.iterate_snake(
    x = x,
    y = y,
    a = alpha,
    b = beta,
    fx = fx,
    fy = fy,
    gamma = gamma,
    n_iters = iterations,
    return_all = True
)


fig = plt.figure()
ax  = fig.add_subplot(111)
ax.imshow(img, cmap=plt.cm.gray)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(0,img.shape[1])
ax.set_ylim(img.shape[0],0)
ax.plot(np.r_[x,x[0]], np.r_[y,y[0]], c=(0,1,0), lw=2)

for i, snake in enumerate(snakes):
    if i % 10 == 0:
        ax.plot(np.r_[snake[0], snake[0][0]], np.r_[snake[1], snake[1][0]], c=(0,0,1), lw=2)

# Plot the last one a different color.
ax.plot(np.r_[snakes[-1][0], snakes[-1][0][0]], np.r_[snakes[-1][1], snakes[-1][1][0]], c=(1,0,0), lw=2)
plt.savefig('foo.png')

plt.show()
