import numpy as np
import networkx as nx

def extract_features(G):
    features = {}
    features['num_nodes'] = len(G.nodes)
    features['num_edges'] = len(G.edges)
    features['avg_degree'] = np.mean([degree for _, degree in G.degree()])
    features['avg_clustering'] = nx.average_clustering(G)
    features['density'] = nx.density(G)
    
    # Node-level features
    degrees = np.array([degree for _, degree in G.degree()])
    features['degree_mean'] = np.mean(degrees)
    features['degree_std'] = np.std(degrees)
    
    return features
