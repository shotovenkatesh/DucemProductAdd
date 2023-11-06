import pandas as pd

# Load the "cleaned_ef.csv" file into a DataFrame
df = pd.read_csv('cleaned_ef.csv')

# Create a new column by concatenating "Name" and "Weight" columns
df['Name_Weight'] = df['Name'] + ' ' + df['weight'].astype(str)

# Save the modified data to the same or a new CSV file
df.to_csv('cleaned_ef.csv', index=False)

