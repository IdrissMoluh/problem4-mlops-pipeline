import plotly.express as px
from sklearn.datasets import load_iris
from umap import UMAP
import os

def main():
    # Load the Iris data
    iris = load_iris()
    umap_2d = UMAP()
    # Fit UMAP to Iris data
    umap_2d.fit(iris.data)
    projections = umap_2d.transform(iris.data)
    
    # Plot the projections with the Iris target as color
    fig = px.scatter(
        projections,
        x=0,
        y=1,
        color=iris.target.astype(str),
        labels={"color": "iris"}
    )
    
    # Ensure the public directory exists
    if not os.path.exists("public"):
        os.makedirs("public")
    
    # Save the plot as an HTML file
    try:
        fig.write_html("public/index.html")
        print("Plot successfully saved as public/index.html")
    except Exception as e:
        print(f"Error saving plot: {e}")

if __name__ == "__main__":
    main()


