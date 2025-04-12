import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\suraj\Downloads\employment-generated.csv")

# Display basic informationh
print(df.info())
print(df.head())  # Display first few rows
