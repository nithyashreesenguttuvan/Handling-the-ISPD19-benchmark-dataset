import networkx as nx

def analyze_graph(G):
    # Calculate basic graph metrics
    num_nodes = len(G.nodes)
    num_edges = len(G.edges)
    avg_degree = sum(dict(G.degree()).values()) / num_nodes
    clustering_coefficient = nx.average_clustering(G)
    
    # Print graph metrics
    print(f'Number of nodes: {num_nodes}')
    print(f'Number of edges: {num_edges}')
    print(f'Average degree: {avg_degree:.2f}')
    print(f'Average clustering coefficient: {clustering_coefficient:.2f}')
    
    return {
        'num_nodes': num_nodes,
        'num_edges': num_edges,
        'avg_degree': avg_degree,
        'clustering_coefficient': clustering_coefficient
    }
