import matplotlib.pyplot as plt
from scatter_squares import randomwalk
rw = randomwalk()
rw.fill_walk()
plt.scatter(rw.x_values,rw.y_values,s = 15)
plt.show()