#Animación de la epidemia a través de agentes.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
from tqdm import tqdm,trange
import os

colores    = ['blue','red', 'green']
archivo    = "data/animacion.txt"
N          = 200
L          = 70

nsteps     = np.loadtxt(archivo, usecols=0).size/N
loop_range = int(nsteps)
n_simul    = -1
tiempo     = np.loadtxt(archivo, usecols=2)

print("Arrays cargados. \n"),
make_folder = True
selector    = 17

fig, ax    = plt.subplots()
for i in range(loop_range):
	if tiempo[N*i] == 0: 
		n_simul+=1
		print("n_simul",n_simul)
		
	if n_simul==selector:
		if make_folder:
			os.mkdir("video/video%i" %n_simul)
			make_folder = False			
		x      = np.loadtxt(archivo, usecols=0, skiprows=N*i, max_rows=N)
		y      = np.loadtxt(archivo, usecols=1, skiprows=N*i, max_rows=N)
		estado = np.loadtxt(archivo, usecols=3, skiprows=N*i, max_rows=N, dtype=int)
			
		plt.cla()
		plt.title("Agent system")
		plt.xlabel("x coordinate")
		plt.ylabel("y coordinate")
		plt.axis('square')
		plt.grid()
		plt.xlim(-1,L+1)
		plt.ylim(-1,L+1)

		population_count = np.array([0,0,0],dtype=int)
		for j in range(N):
			circ = patches.Circle((x[j],y[j]), 1, alpha=0.7, fc= colores[estado[j]])
			ax.add_patch(circ)
			if estado[j] == 0:
				population_count[0]+=1
			if estado[j] == 1:
				population_count[1]+=1
			if estado[j] == 2:
				population_count[2]+=1

		legend_elements = [ Line2D([0], [0], marker='o', color='w', label='%i' %population_count[0], markerfacecolor='b', markersize=10),
					    	    Line2D([0], [0], marker='o', color='w', label='%i' %population_count[1], markerfacecolor='r', markersize=10),
					    		Line2D([0], [0], marker='o', color='w', label='%i' %population_count[2], markerfacecolor='g', markersize=10) ]

		plt.legend(handles=legend_elements, bbox_to_anchor=(1.05, 1), loc='upper left')
		plt.savefig("video/video%i/pic%.4i.png" %(n_simul,i), dpi=150)


