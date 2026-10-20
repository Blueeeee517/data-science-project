import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("visualizations", exist_ok=True)

# Generate simulated data
np.random.seed(42)
study_hours = np.random.uniform(1, 10, 50)
scores = study_hours * 8 + np.random.normal(0, 5, 50) + 40

df = pd.DataFrame({
    "Study Hours": study_hours,
    "Score": scores
})

# Visualization 1: Scatter plot
plt.figure()
plt.scatter(df["Study Hours"], df["Score"], color="blue", alpha=0.7)
plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid(True)
plt.savefig("visualizations/study_score_scatter.png", dpi=150, bbox_inches="tight")

# Visualization 2: Bar chart
df["Study Group"] = pd.cut(df["Study Hours"], bins=[0, 3, 6, 10], labels=["<3 hours", "3-6 hours", ">6 hours"])
avg_scores = df.groupby("Study Group")["Score"].mean()

plt.figure()
avg_scores.plot(kind="bar", color=["red", "orange", "green"])
plt.title("Average Score by Study Hours Group")
plt.xlabel("Study Hours")
plt.ylabel("Average Score")
plt.xticks(rotation=0)
plt.savefig("visualizations/grouped_scores_bar.png", dpi=150, bbox_inches="tight")
