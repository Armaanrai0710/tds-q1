import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

TARGET = 85.0

def main():
    here = os.path.dirname(__file__)
    root = os.path.abspath(os.path.join(here, ".."))
    data_path = os.path.join(root, "data", "retention_2024.csv")
    plots_dir = os.path.join(root, "plots")
    os.makedirs(plots_dir, exist_ok=True)

    df = pd.read_csv(data_path)
    df["quarter"] = pd.Categorical(df["quarter"], categories=["Q1","Q2","Q3","Q4"], ordered=True)
    df = df.sort_values("quarter")

    avg = round(df["customer_retention_rate"].mean(), 2)
    print(f"Average retention (2024): {avg}")

    # Trend line
    plt.figure()
    plt.plot(df["quarter"], df["customer_retention_rate"], marker="o")
    plt.axhline(TARGET, linestyle="--")
    plt.title("Customer Retention Rate - 2024 Trend vs Target")
    plt.xlabel("Quarter")
    plt.ylabel("Retention Rate")
    plt.tight_layout()
    trend_path = os.path.join(plots_dir, "trend_vs_target.png")
    plt.savefig(trend_path, dpi=200)
    plt.close()

    # Gap chart (bar of shortfall to target; negative means above target)
    gap = TARGET - df["customer_retention_rate"]
    plt.figure()
    plt.bar(df["quarter"], gap)
    plt.axhline(0, linewidth=1)
    plt.title("Gap to Target (85) by Quarter")
    plt.xlabel("Quarter")
    plt.ylabel("Points below target (negative means above)")
    plt.tight_layout()
    gap_path = os.path.join(plots_dir, "gap_to_target.png")
    plt.savefig(gap_path, dpi=200)
    plt.close()

    # Save a quick summary JSON
    summary = {
        "average_2024": avg,
        "best_quarter": df.loc[df["customer_retention_rate"].idxmax(), "quarter"],
        "best_value": float(df["customer_retention_rate"].max()),
        "worst_quarter": df.loc[df["customer_retention_rate"].idxmin(), "quarter"],
        "worst_value": float(df["customer_retention_rate"].min()),
        "target": TARGET,
        "quarterly_values": df.set_index("quarter")["customer_retention_rate"].to_dict()
    }
    with open(os.path.join(root, "analysis_summary.json"), "w") as f:
        import json; json.dump(summary, f, indent=2)

if __name__ == "__main__":
    main()
