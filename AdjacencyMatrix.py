# Plot graph from adjacency matrix

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


matrix = np.array([[0,0,0,1,0]
                   ,[0,0,0,1,1]
                   ,[0,1,0,0,1]
                   ,[1,1,0,0,1]
                   ,[0,1,1,1,0]])

G = nx.from_numpy_array(matrix)

nx.draw(G, with_labels=True)
plt.show()