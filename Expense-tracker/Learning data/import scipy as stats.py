import numpy as np
from scipy import stats

people = {
    "Liza": 19,
    "Shav": 23,
    "Alyssa": 19,
    "Helena": 20,
    "Abby": 20,
    "Tatyana": 62,
    "Zaur": 61,
    "Anya": 23
}

for name, age in people.items():
    print(f"{name}: {age}")

ages = list(people.values())
mean_age = np.mean(ages)
median_age = np.median(ages)
mode_age = stats.mode(ages)
print(f"Mean age: {mean_age}")
print(f"Median age: {median_age}")
print(f"Mode age: {mode_age}")