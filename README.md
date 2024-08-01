# Handling-the-ISPD19-benchmark-dataset

## Project Structure

ispd19_project/

│

├── data/instance1

│   ├── ispd19_sample.input.lef

│   ├── ispd19_sample.input.def

│   └── ispd19_sample.input.guide

├── data/instance2

│   ├── ispd19_sample.input.lef

│   ├── ispd19_sample.input.def

│   └── ispd19_sample.input.guide

│
.
.
.

├── src/

│   ├── __init__.py

│   ├── preprocess.py

│   ├── visualization.py

│   ├── graph_analysis.py

│   ├── feature_extraction.py

│   ├── model_training.py

│   └── main.py

│   ├── example_usage.py

│

├── requirements.txt

└── README.md

# ISPD19 Benchmark Dataset Project

This project handles the ISPD19 benchmark dataset, including LEF, DEF, and Guide files. It includes code for preprocessing and visualizing the dataset.

## Project Structure

- `data/`: Contains dataset files.
- `src/`: Source code directory.
  - `preprocess.py`: Contains functions to parse LEF, DEF, and Guide files.
  - `visualization.py`: Contains functions for visualizing the graph.
  - `graph_analysis.py`: Contains functions for graphical analysis
  - `feature_extraction`: Contains functions to extract features from the graph
  - `model_training.py`: Contains functions to train the model for Random Classifier
  - `example_usage.py`: Contains codewrok on example usage of extracting the data and converting it to a graph
  - `main.py`: Main script to run the entire code and obtain results about the graph data.
- `requirements.txt`: Python dependencies.
- `README.md`: Project documentation.

## Setup

1. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

2. Place your dataset files in the `data/` directory.

3. Run the main script:
    ```bash
    python src/main.py
    ```
