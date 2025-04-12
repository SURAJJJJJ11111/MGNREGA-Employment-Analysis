import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\suraj\Downloads\employment-generated.csv")

# 1. Basic Information
print("📌 Basic Info:")
print(df.info())

# 2. Missing Values Check
print("\n📌 Missing Values:")
print(df.isnull().sum())

# 3. Summary Statistics
print("\n📌 Summary Statistics:")
print(df.describe(include='all'))

# 4. Duplicate Rows Check
print("\n📌 Duplicate Rows:")
print(df.duplicated().sum())

# 5. Preview of Dataset
print("\n📌 First 5 Rows:")
print(df.head())

# 6. Column Names
print("\n📌 Column Names:")
print(df.columns)

# 7. Unique Values for Categorical Columns (Example: 'state_name')
print("\n📌 Unique Values in 'state_name':")
print(df['state_name'].unique())

# 8. Value Counts for Categorical Columns (Example: 'state_name')
print("\n📌 Value Counts for 'state_name':")
print(df['state_name'].value_counts())

# 9. Correlation Matrix (Numeric Columns)
print("\n📌 Correlation Matrix (Numeric Columns):")
print(df.corr())

# 10. Constant Columns Check
constant_columns = [col for col in df.columns if df[col].nunique() == 1]
print("\n📌 Constant Columns (Columns with the Same Value for All Rows):")
print(constant_columns)

# 11. Data Types of Columns
print("\n📌 Data Types of Each Column:")
print(df.dtypes)

# 12. Missing Values Per Column
print("\n📌 Missing Values per Column:")
print(df.isnull().sum())
