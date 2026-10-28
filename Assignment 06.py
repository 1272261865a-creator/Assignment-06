import pandas as pd
import numpy as np

data = {
    'Student_ID':,
    'Name': ['Amit', 'Priya', 'Rohan', 'Sneha', 'Priya', 'Rahul', 'Anjali'],
    'Marks': [85.0, np.nan, 92.0, 78.0, np.nan, 65.0, np.nan],
    'City': ['Pune', 'Mumbai', np.nan, 'Pune', 'Mumbai', 'Delhi', 'Bangalore']
}

df = pd.DataFrame(data)
print("--- 1. Original Raw DataFrame ---")
print(df)
print("\n" + "="*50 + "\n")

print("--- 2. Dataset Information Summary ---")
df.info()
print("\nDescriptive Statistics:")
print(df.describe())
print("\n" + "="*50 + "\n")

print("--- 3. Handling Duplicate Records ---")
print("Duplicate rows detected:\n", df.duplicated())

df_cleaned = df.drop_duplicates().copy()
print("\nDataFrame after removing duplicates:")
print(df_cleaned)
print("\n" + "="*50 + "\n")

print("--- 4. Handling Missing Values ---")
print("Count of missing values per column:\n", df_cleaned.isnull().sum())

mean_marks = df_cleaned['Marks'].mean()
df_cleaned['Marks'] = df_cleaned['Marks'].fillna(mean_marks)

df_cleaned = df_cleaned.dropna(subset=['City'])

print("\nDataFrame after cleaning missing values (Imputed Marks & Dropped Null Cities):")
print(df_cleaned)
print("\n" + "="*50 + "\n")

print("--- 5. Data Selection and Filtering using .loc ---")
high_performers = df_cleaned.loc[df_cleaned['Marks'] >= 80, ['Name', 'Marks', 'City']]

print("Filtered Target Segment (Marks >= 80):")
print(high_performers)
