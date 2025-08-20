import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ---------------------------
# Generate Synthetic Data
# ---------------------------
np.random.seed(42)

# Define customer segments
segments = ["Budget", "Regular", "Premium", "VIP"]

# Generate synthetic purchase amounts
data = {
    "Segment": np.repeat(segments, 200),
    "PurchaseAmount": np.concatenate([
        np.random.normal(50, 15, 200),    # Budget customers
        np.random.normal(150, 40, 200),   # Regular customers
        np.random.normal(400, 100, 200),  # Premium customers
        np.random.normal(800, 200, 200)   # VIP customers
    ])
}

df = pd.DataFrame(data)

# ---------------------------
# Visualization
# ---------------------------
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=1.0)

plt.figure(figsize=(8, 8))  # 512x512 pixels at dpi=64

# Create boxplot
ax = sns.boxplot(
    data=df,
    x="Segment",
    y="PurchaseAmount",
    palette="Set2",
    width=0.6
)

# Add title and labels
ax.set_title("Customer Purchase Amount Distribution by Segment", fontsize=16, weight="bold")
ax.set_xlabel("Customer Segment", fontsize=14)
ax.set_ylabel("Purchase Amount (USD)", fontsize=14)

# Remove top/right borders for professional look
sns.despine()

# ---------------------------
# Save chart
# ---------------------------
plt.savefig("chart.png", dpi=64)
plt.close()
