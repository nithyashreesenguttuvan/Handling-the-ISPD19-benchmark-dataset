import matplotlib.pyplot as plt
import networkx as nx

def visualize_graph(G):
    pos = nx.spring_layout(G)  # Position using a force-directed layout
    nx.draw(G, pos, with_labels=True, node_size=50)
    plt.show()
