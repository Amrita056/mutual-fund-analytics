import pandas as pd
import matplotlib.pyplot as plt
benchmark = pd.read_csv("10_benchmark_indices.csv")
print("========== FIRST 5 ROWS ==========")
print(benchmark.head())
print("\n========== DATASET INFO ==========")
benchmark.info()
print("\n========== SHAPE ==========")
print(benchmark.shape)
print("\n========== COLUMN NAMES ==========")
print(benchmark.columns)
print("\n========== MISSING VALUES ==========")
print(benchmark.isnull().sum())
print("\n========== DUPLICATE ROWS ==========")
print(benchmark.duplicated().sum())
print("\n========== CONVERT DATE ==========")

benchmark["date"] = pd.to_datetime(benchmark["date"])

print(benchmark.dtypes)
print("\n========== DATE RANGE ==========")

print("Start :", benchmark["date"].min())
print("End   :", benchmark["date"].max())
print("\n========== BENCHMARK INDICES ==========")

print(benchmark["index_name"].unique())
first_index = benchmark["index_name"].unique()[0]

print("\nUsing Index :", first_index)

index_data = benchmark[
    benchmark["index_name"] == first_index
]
print("\n========== HIGHEST CLOSE VALUE ==========")

highest = index_data.loc[index_data["close_value"].idxmax()]

print(highest)
print("\n========== LOWEST CLOSE VALUE ==========")

lowest = index_data.loc[index_data["close_value"].idxmin()]

print(lowest)
plt.figure(figsize=(15,6))

plt.plot(
    index_data["date"],
    index_data["close_value"],
    color="purple",
    linewidth=2,
    label=first_index
)

plt.scatter(
    highest["date"],
    highest["close_value"],
    color="red",
    s=100,
    label="Highest"
)

plt.scatter(
    lowest["date"],
    lowest["close_value"],
    color="blue",
    s=100,
    label="Lowest"
)

plt.title(f"{first_index} Benchmark Trend")

plt.xlabel("Date")

plt.ylabel("Closing Value")

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig("benchmark_trend.png", dpi=300)

plt.show()

