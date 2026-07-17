import pandas as pd
import numpy as np

data = [{ "StudentName": "Tom", "Age": 13, "Grade": "Seventh" },
        { "StudentName": "Tom", "Age": 13, "Grade": "Seventh" },
        { "StudentName": "Jim", "Age": 15, "Grade": "Ninth" },
        { "StudentName": "Sabrina", "Age": 12, "Grade": "Sixth" },
        { "StudentName": "Penny", "Age": 15, "Grade": "Ninth" }]

# TODO: Create a DataFrame 'df'
df = pd.DataFrame(data)
print(f"The unresolved data is:\n{df}\n")

# TODO: Remove duplicates from the DataFrame
df = df.drop_duplicates()

# TODO: Calculate the median of the 'Age' column
median_age = df['Age'].median()
Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1

# TODO: Calculate Q1, Q3, and IQR for age. Afterwards, calculate the lower and upper bounds.
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 *IQR

# TODO: Replace any outliers in the 'Age' data with the calculated median
df['Age'] = np.where((df['Age'] > upper_bound) | (df['Age'] < lower_bound), median_age, df['Age'])

print(f"The updated df is:\n{df}\n")