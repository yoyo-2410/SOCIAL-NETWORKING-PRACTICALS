# pip install pandas networkx matplotlib

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

G = nx.from_pandas_edgelist(
    pd.read_csv("http://snap.stanford.edu/data/facebook_combined.txt.gz",
                compression='gzip', sep=' ', names=['n1', 'n2']),'n1', 'n2')

print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())

nx.draw(G, node_size=5, edge_color='gray')
plt.show()
