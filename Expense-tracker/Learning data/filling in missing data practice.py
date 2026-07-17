import pandas as pd
import matplotlib.pyplot as plt
# Mock client information
client_data = {
    "ClientID": [1, 2, 3, 4, 5],
    "Name": ["Alice", "Bob", "Charlie", None, "Eve"],
    "Age": [25, None, 35, None, 45],
    "City": ["New York", None, "Chicago", "Houston", "Phoenix"]
}
df = pd.DataFrame(client_data)
df["Name"] = df["Name"].fillna("Unknown")
df["City"] = df["City"].fillna("Unknown")
#This fills in the missing values in the "Name" and "City" columns with "Unknown".

df["Age"]=df["Age"].fillna(df["Age"].median())
#This fills in missing values in age column with the median age of the existing values.

print(df)
plt.hist(df["Age"], bins=5, color="blue", edgecolor="black")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Distribution of Ages")
# This creates a histogram to visualize the distribution of ages in the dataset.
plt.show()
