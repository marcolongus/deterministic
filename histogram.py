import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = np.random.rand(10)

x = plt.hist(data)

print(x[0])

plt.show()