# src/visualization.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_revenue_trends(quarters, revenue):
    """
    Plots a line chart showing revenue trends.
    :param quarters: List of quarter labels.
    :param revenue: List of revenue values.
    """
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=quarters, y=revenue, marker="o")
    plt.title("Revenue Growth Over Recent Quarters")
    plt.xlabel("Quarter")
    plt.ylabel("Revenue (in millions)")
    plt.show()
