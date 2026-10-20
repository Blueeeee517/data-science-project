import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

os.makedirs("visualizations", exist_ok=True)

iris = load_iris(as_frame=True)
df = iris.frame
df["species"] = df["target"].map(dict(enumerate(iris.target_names)))

# Visualization 1
plt.figure()
plt.scatter(df["sepal length (cm)"], df["sepal width (cm)"], c=df["target"])
plt.xlabel("Sepal length (cm)")
plt.ylabel("Sepal width (cm)")
plt.title("Iris sepal measurements")
plt.savefig("visualizations/sepal_scatter.png", dpi=150, bbox_inches="tight")

# Visualization 2
plt.figure()
df.boxplot(column="petal length (cm)", by="species")
plt.title("Petal length by species")
plt.suptitle("")
plt.ylabel("Petal length (cm)")
plt.savefig("visualizations/petal_length_boxplot.png", dpi=150, bbox_inches="tight")
