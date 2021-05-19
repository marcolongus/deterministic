import numpy as np
import matplotlib.pyplot as plt

data  = "data/epid.txt"

healthy    = np.loadtxt(data, usecols = 0)
infected   = np.loadtxt(data, usecols = 1)
refractary = np.loadtxt(data, usecols = 2)

time       = np.loadtxt(data, usecols = 3)

plt.show()
