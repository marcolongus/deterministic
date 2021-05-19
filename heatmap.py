import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = "epid.txt"
epid_count = np.loadtxt(data, usecols=4)
healthy    = np.loadtxt(data, usecols=0)
infected   = np.loadtxt(data, usecols=1)
refractary = np.loadtxt(data, usecols=2)
tiempo     = np.loadtxt(data, usecols=3)

n = 1
l = []
for i, element in enumerate(epid_count):
	if element == n:
		l.append(i)
		n+=1
l2 = []
for i,element in enumerate(l):
	try:
		l2.append(l[i+1]-l[i])
	except:
		break


heat_grid = np.zeros(shape=(100,500))
bins      = np.linspace(0,200,201)
g_index   = 0
for time in range(0,5000,10):
	column = []
	for i in range(149):
		try:
			column.append(infected[l[i]+time])
		except:
			continue
	histogram = plt.hist(column, bins, density=True)
	heat_grid[:,g_index] = histogram[0][0:100]
	print(histogram[0][0:10]),print()
	g_index+=1


#print(heat_grid)
#uniform_data = np.random.rand(10,12)
sns.heatmap(heat_grid, vmin=0, vmax=1,annot=False)
plt.show()