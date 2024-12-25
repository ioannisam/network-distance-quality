import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from distance_quality import distance_quality_function, adj
from utils import plot_graph

G = {
    'n': 4,
    'edges': [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
}
clusters = [[0, 1, 2, 3]]
print("Connected: YES\nClusters: 1\n")
print("\nDistance Quality Function Q_d: {:.2f}".format(distance_quality_function(G, clusters)))

A = adj(G['edges'], G['n'])
plot_graph(A)