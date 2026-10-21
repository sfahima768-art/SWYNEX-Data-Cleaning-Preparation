import pandas as pd

# Load the raw dataset
df = pd.read_csv("student.csv")

print("Original Dataset:")
print(df)

# Remove duplicate records
df = df.drop_duplicates()

# Convert Age and Marks into numeric values
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")

# Standardize department names
df["Department"] = df["Department"].str.strip().str.upper()

# Fill missing numeric values with column averages
df["Age"] = df["Age"].fillna(df["Age"].mean()).round().astype(int)
df["Marks"] = df["Marks"].fillna(df["Marks"].mean()).round(2)

# Save the cleaned dataset
df.to_csv("cleaned_student.csv", index=False)

print("\nCleaned Dataset:")
print(df)

print("\nCleaning completed successfully!")
print("Cleaned dataset saved as cleaned_student.csv")