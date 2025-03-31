import pandas as pd

# Load your CSV file
df = pd.read_csv('customer_churn_dataset-testing-master.csv')

# Check first few rows to inspect the data
print(df.head())

# Remove the '?' and any extra spaces from the 'Total Spend' column
df['Total Spend'] = df['Total Spend'].str.replace('?', '', regex=False).str.strip()

# Convert the cleaned column to numeric (float)
df['Total Spend'] = pd.to_numeric(df['Total Spend'], errors='coerce')

# Display the cleaned column
print(df['Total Spend'].head())
df.to_csv('customer_churn_dataset-testing-master.csv', index=False)