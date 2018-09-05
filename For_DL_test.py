import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
ax = Axes3D(plt.figure())

x = np.arange(-3, 3, 0.05)
X, Y = np.meshgrid(x, x)
Dis = np.sqrt(X ** 2 + Y ** 2)
Z = np.cos(Dis)

ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = plt.get_cmap('rainbow'))
ax.contour(X, Y, Z, offset = -2, cmap = 'rainbow')
ax.set_zlim(-1.5, 1.5)

plt.show()