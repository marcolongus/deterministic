import numpy as np
import matplotlib.pyplot as plt

data = "data/episize.txt"

epidemicSize = np.loadtxt(data, usecols=0)
initImmune   = np.linspace(0,149,150)

plt.title("Epidemic size vs diff. initial conditions")
plt.xlim(0,150)
plt.ylim(0,epidemicSize.max()+5)
plt.xlabel("Immunuzation")
plt.ylabel("Epi. Size")
plt.plot(initImmune, epidemicSize)
plt.scatter(initImmune, epidemicSize)
plt.savefig("network/episize.png")
plt.show()