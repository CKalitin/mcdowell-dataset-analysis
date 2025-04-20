import mcdowell_dataset_analysis as mda
import pandas as pd
import matplotlib.pyplot as plt

# Initialize the dataset
dataset = mda.McdowellDataset()
launch_df = dataset.launch.df.copy()

# Filter for Starlink launches
starlink_pattern = r'Starlink'
filtered_df = launch_df[launch_df['Mission'].str.contains(starlink_pattern, case=False, na=False, regex=True)]
print(f"Number of Starlink launches: {len(filtered_df)}")

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

print(filtered_df.head(500))

# Select relevant columns
filtered_df = filtered_df[['Launch_Date', 'Apogee', 'Launch_Pad']]

# Drop rows with missing Apogee
filtered_df = filtered_df.dropna(subset=['Apogee'])
print(f"Number of launches with valid Apogee: {len(filtered_df)}")

# Print unique launch pads
print("Unique launch pads for Starlink launches:")
print(filtered_df['Launch_Pad'].unique())

# Pivot the table: Launch_Date as index, Launch_Pad as columns, Apogee as values
pivoted_df = filtered_df.pivot(index='Launch_Date', columns='Launch_Pad', values='Apogee')

# Reset index to make Launch_Date a column
pivoted_df = pivoted_df.reset_index()

# Sort by Launch_Date
pivoted_df = pivoted_df.sort_values(by='Launch_Date')

# Save to CSV without index
pivoted_df.to_csv('charts/starlink_apogee_vs_date.csv', index=False)
print("CSV file 'starlink_apogee_vs_date.csv' has been created.")

# Create scatter plot
plt.figure(figsize=(10, 6))
for pad in pivoted_df.columns[1:]:  # Skip 'Launch_Date'
    plt.scatter(pivoted_df['Launch_Date'], pivoted_df[pad], label=pad, alpha=0.7)

# Customize plot
plt.title('Starlink Launches: Apogee vs. Launch Date by Launch Pad')
plt.xlabel('Launch Date')
plt.ylabel('Apogee (km)')
plt.legend(title='Launch Pad')
plt.grid(True)

# Save plot
plt.savefig('charts/starlink_apogee_vs_date.png')
print("Plot saved as 'starlink_apogee_vs_date.png'.")