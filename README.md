# Handling-the-ISPD19-benchmark-dataset

## Project Structure

ispd19_project/

│

├── data/

│   ├── ispd19_sample.input.lef

│   ├── ispd19_sample.input.def

│   └── ispd19_sample.input.guide

│

├── src/

│   ├── __init__.py

│   ├── preprocess.py

│   ├── visualization.py

│   └── main.py

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
  - `main.py`: Main script to run the preprocessing and visualization.
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
