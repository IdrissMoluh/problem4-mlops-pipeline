# Problem 4 : MLOps Inference API

This project demonstrates the deployment of an MLOps pipeline for training and inference using the Iris dataset and KNN classifier.

## Project Overview

The project involves:
- Training a machine learning model on the Iris dataset.
- Deploying an inference API using the trained model.
- Visualizing results using UMAP for dimensionality reduction.

## UMAP Visualization

We used UMAP to project the high-dimensional Iris dataset into 2D space. Below is the UMAP plot of the Iris dataset, showing clusters of different species:

![UMAP Visualization](public/index.html)

This visualization helps to understand how the species in the Iris dataset are grouped based on their feature measurements.

## Getting Started

### Step 1: Set Up Virtual Environment

First, make sure you're using a virtual environment to install dependencies and run the project. If you haven’t already created a virtual environment, you can do so by running the following commands:

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

Or, on Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Install Dependencies

Once the virtual environment is activated, install the required packages:

```bash
pip install umap-learn pandas plotly
```

### Step 3: Generate the UMAP Visualization

To generate the UMAP plot yourself, you can run the `visualize.py` script:

```bash
python visualize.py
```

This will save the UMAP plot as an HTML file at `public/index.html`.

### Step 4: View the UMAP Visualization

Open the generated `public/index.html` file in your browser to view the UMAP plot.

```
C:\Users\14255\Documents\Georgetow University\Fourth or Fall Semester 2024\DSAN_6700\Assignments\A1 BIS\Problem4\problem4-mlops-pipeline\public\index.html
```

### Conclusion

This MLOps pipeline example demonstrates how to set up an inference API, train a model, and visualize the results. Feel free to explore the code and modify it for your own use cases!
```

### Key Changes:
- **Removed references to `poetry`** and replaced them with instructions for using a virtual environment (`venv`).
- **Added steps for setting up and activating the virtual environment**.
- **Clarified the steps for installing dependencies and running the visualization script**.

You can now add this updated content to your `README.md` file.

### Final Steps:
1. **Update your `README.md`** with the content above.
2. **Commit and push the changes** to your GitHub repository:
   ```bash
   git add README.md
   git commit -m "Updated README with UMAP visualization and virtual environment setup"
   git push
   ```

