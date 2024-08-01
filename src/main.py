from preprocess import load_ispd_data
from visualization import visualize_graph
from graph_analysis import analyze_graph
from feature_extraction import extract_features
from model_training import train_model

def main():
    base_dirs = ['/content/sample_data/instance1', '/content/sample_data/instance2',  '/content/sample_data/instance3',  '/content/sample_data/instance4']  # List of directories for multiple instances
    all_features = []
    all_labels = []

    for base_dir in base_dirs:
        G, cell_info, guides = load_ispd_data(base_dir)
        
        # Visualize the graph
        visualize_graph(G)
        
        # Analyze the graph
        metrics = analyze_graph(G)
        
        # Extract features
        features = extract_features(G)
        all_features.append(features)
        
        # Example label assignment based on instance
        labels = [0]  # Modify as needed
        all_labels.extend(labels)
    
    # Train a machine learning model
    if all_features:
        model = train_model(all_features, all_labels)
    
    # Print extracted features
    print("Extracted Features:")
    print(all_features)

if __name__ == '__main__':
    main()
