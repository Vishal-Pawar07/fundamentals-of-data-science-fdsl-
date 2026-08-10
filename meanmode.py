import pandas as pd
import numpy as np
from collections import Counter

ss = pd.read_csv("country_wise_latest.csv")

profit = ss["Profit"].dropna()
profit_list = list(profit)

# Manual Mean / Average
manual_mean = sum(profit_list) / len(profit_list)

# Manual Median
sorted_profit = sorted(profit_list)
n = len(sorted_profit)

if n % 2 == 0:
    manual_median = (sorted_profit[n // 2 - 1] + sorted_profit[n // 2]) / 2
else:
    manual_median = sorted_profit[n // 2]

# Manual Mode
frequency = Counter(profit_list)
manual_mode = frequency.most_common(1)[0][0]

print("Manual Mean / Average of Profit:", manual_mean)
print("Manual Median of Profit:", manual_median)
print("Manual Mode of Profit:", manual_mode)

# NumPy
profit_array = np.array(profit_list)

print("NumPy Mean / Average of Profit:", np.mean(profit_array))
print("NumPy Median of Profit:", np.median(profit_array))

values, counts = np.unique(profit_array, return_counts=True)
numpy_mode = values[np.argmax(counts)]

print("NumPy Mode of Profit:", numpy_mode)

# Pandas
print("Pandas Mean / Average of Profit:", ss["Profit"].mean())
print("Pandas Median of Profit:", ss["Profit"].median())
print("Pandas Mode of Profit:", ss["Profit"].mode()[0]