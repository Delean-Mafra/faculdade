from numpy import shape
import pandas as pd

# Read the CSV file directly from the current directory
df = pd.read_csv('dados.csv')

# Display the first few rows
print(df.head())

print(df.info())

print(df.isna().sum())

print(shape(df))
