from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt

data = "data/epid.txt"

ax = plt.axes(projection='3d')

# Data for a three-dimensional line
xline = np.loadtxt(data, usecols= 0)
yline = np.loadtxt(data, usecols= 1)
zline = np.loadtxt(data, usecols= 2)


ax.set_xlabel("Healthy")
ax.set_ylabel("Infected")
ax.set_zlabel("Refract")

print(zline.size, xline.size, yline.size)
#ax.plot3D(xline, yline, zline, 'gray')

max_rows = 3500
# Data for three-dimensional scattered points
xdata = np.loadtxt(data, usecols= 0, max_rows = max_rows)
ydata = np.loadtxt(data, usecols= 1, max_rows = max_rows)
zdata = np.loadtxt(data, usecols= 2, max_rows = max_rows)

ax.scatter3D(xdata, ydata, zdata, c=zdata)
plt.show()
plt.cla()


ax = plt.axes(projection='3d')
ax.scatter3D(xdata, ydata, 0, c=zdata, cmap="Blues")
ax.scatter3D(xdata, 0, zdata, c=zdata, cmap="Greens")
ax.scatter3D(0, ydata, zdata, c=zdata, cmap="Reds")
plt.show()

#plt.contour(xdata, ydata, zdata, colors='black');