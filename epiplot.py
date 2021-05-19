import numpy as np
import matplotlib.pyplot as plt

data = "data/epid.txt"

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



#hacer un append de los array de forma que se vea cómo mueren las curvas. 
plt.xlabel("Time")
plt.ylabel("Population")
plt.ylim(0,infected.max()+1)

for i in range(148):
	tamaño     = tiempo[l[i]:l[i+1]].size	
	tiempo_n   = np.zeros(shape=tamaño + 1)
	infected_n = np.zeros(shape=tamaño + 1)
	tiempo_n[0:tamaño]   = tiempo[l[i]:l[i+1]] 
	tiempo_n[tamaño]     = tiempo_n[tamaño-1]+1

	infected_n[0:tamaño] = infected[l[i]:l[i+1]]
	infected_n[tamaño]   = 0
	#plt.plot(tiempo[l[i]:l[i+1]], infected[l[i]:l[i+1]], label="%i" %i)
	plt.plot(tiempo_n, infected_n, label="%i" %i)

plt.savefig("network/i_vs_t.png")
#plt.legend()
plt.show()





