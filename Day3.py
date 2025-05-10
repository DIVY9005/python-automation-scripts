import pandas as pd

# Load messy Excel file
df = pd.read_excel("raw_data.xlsx")

# Drop completely empty rows
df.dropna(how='all', inplace=True)

# Fill missing values (optional logic)
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Email'].fillna("noemail@unknown.com", inplace=True)

# Save cleaned file
df.to_excel("cleaned_data.xlsx", index=False)

print("✅ Data cleaned and saved as 'cleaned_data.xlsx'")
