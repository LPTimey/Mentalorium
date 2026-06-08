import matplotlib.pyplot as plt
import numpy as np
import os

def main():
    # Example data
    np.random.seed(42)

    data_1 = np.random.normal(50, 10, 200)
    data_2 = np.random.normal(60, 15, 200)
    data_3 = np.random.normal(55, 20, 200)
    data_4 = np.random.normal(65, 5, 200)

    data = [data_1, data_2, data_3, data_4]

    # Create plot
    plt.figure(figsize=(8, 5))
    plt.boxplot(data, labels=["A", "B", "C", "D"], patch_artist=True)

    plt.title("Box Plot Example")
    plt.ylabel("Values")
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.tight_layout()

    # Ensure output directory exists
    output_path = "out/test.png"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save figure
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()

    print(f"Saved plot to {output_path}")


if __name__ == "__main__":
    main()