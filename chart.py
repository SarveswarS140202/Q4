import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1. Generate synthetic data
np.random.seed(42)
n = 100
data = pd.DataFrame({
    "Acquisition_Cost": np.random.uniform(50, 500, n),
    "Customer_Lifetime_Value": np.random.uniform(200, 5000, n),
    "Segment": np.random.choice(["High-Value", "Medium-Value", "Low-Value"], size=n)
})

# 2. Styling
sns.set_style("whitegrid")
sns.set_context("talk")

# 3. Create scatterplot
plt.figure(figsize=(8, 8))  # base figure
sns.scatterplot(
    data=data,
    x="Acquisition_Cost",
    y="Customer_Lifetime_Value",
    hue="Segment",
    palette="Set2",
    s=80,
    edgecolor="black"
)

plt.title("Customer Lifetime Value vs Acquisition Cost", fontsize=16, weight="bold")
plt.xlabel("Acquisition Cost ($)", fontsize=12)
plt.ylabel("Customer Lifetime Value ($)", fontsize=12)
plt.legend(title="Customer Segment", loc="upper left", frameon=True)

# 4. Save with exact resolution (512x512 px)
plt.savefig("chart.png", dpi=64, bbox_inches=None, pad_inches=0)
plt.close()
