import pandas as pd

# Step 1: Load the dataset from the Excel file.
file_path = '/Users/mizq7/Desktop/Excel data/118th_House_Master_Data_.xlsx'
df = pd.read_excel(file_path)

# Debug: Print the first few rows and column names to verify the data
print("Columns in the dataset:", df.columns)
print(df.head())

# Step 2: Calculate the percentage of Republicans in the California delegation.
# Here we assume the 'State' column uses the two-letter abbreviation (e.g., "CA").
ca_delegation = df[df['State'].str.strip().str.upper() == 'CA']
total_ca = len(ca_delegation)
rep_ca = ca_delegation[ca_delegation['Party'] == 'R']
total_rep_ca = len(rep_ca)

# Compute percentage (rounded to the nearest whole number).
if total_ca > 0:
    percentage_rep_ca = round((total_rep_ca / total_ca) * 100)
else:
    percentage_rep_ca = None

print("Republican percentage of CA delegation (rounded):", percentage_rep_ca)

# Step 3: Calculate the average number of terms served by Democrats.
# Use the 'TermsServed' column (ensure the column name exactly matches).
democrats = df[df['Party'] == 'D']
avg_terms_dem = democrats['TermsServed'].mean()
avg_terms_dem_rounded = round(avg_terms_dem, 2)

print("Average number of terms served by Democrats:", avg_terms_dem_rounded)
