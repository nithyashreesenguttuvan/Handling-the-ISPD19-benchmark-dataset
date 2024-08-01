from preprocess import load_ispd_data
from visualization import visualize_graph

def main():
    base_dir = 'data'
    G, cell_info, guides = load_ispd_data(base_dir)
    visualize_graph(G)

if __name__ == '__main__':
    main()
