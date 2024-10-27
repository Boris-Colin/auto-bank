import pandas as pd


path2 = "C:\\Users\\1thom\\Downloads\\export-operations-27-10-2024_08-51-13.csv"


df = pd.read_csv(path2, sep=';')
df_copy = df.drop(columns=['dateVal', 'categoryParent', 'comment', 'accountNum', 'accountLabel', 'accountbalance'])

df_copy['dateOp'] = pd.to_datetime(df_copy['dateOp'], errors='coerce')
# Remove commas and convert 'amount' to float
df_copy['amount'] = df_copy['amount'].str.replace(' ', '').str.replace(',', '.').astype(float)


# Add a 'year' column
df_copy['year'] = df_copy['dateOp'].dt.year
# Add 'month' column
df_copy['month'] = df_copy['dateOp'].dt.month

# Group by 'year' and 'month' and get the average sales
monthly_ex = df_copy.groupby(['year', 'month'])['amount'].mean()

print(monthly_ex)
print(df_copy.info())
print(df_copy.head())
