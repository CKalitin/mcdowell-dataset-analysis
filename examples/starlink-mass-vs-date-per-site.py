import mcdowell_dataset_analysis as mda
import pandas as pd
import matplotlib.pyplot as plt

# Initialize the dataset
dataset = mda.McdowellDataset()
launch_df = dataset.launch.df.copy()

# Filter for Starlink launches
starlink_pattern = r'Starlink'
filtered_df = launch_df[launch_df['Flight'].str.contains(starlink_pattern, case=False, na=False, regex=True)]
print(f"Number of Starlink launches: {len(filtered_df)}")

# Select relevant columns
filtered_df = filtered_df[['Launch_Date', 'Payload_Mass', 'Launch_Pad']]

# Drop rows with missing Payload_Mass
filtered_df = filtered_df.dropna(subset=['Payload_Mass'])
print(f"Number of launches with valid Payload_Mass: {len(filtered_df)}")

# Print unique launch pads
print("Unique launch pads for Starlink launches:")
print(filtered_df['Launch_Pad'].unique())

# Pivot the table: Launch_Date as index, Launch_Pad as columns, Payload_Mass as values
pivoted_df = filtered_df.pivot(index='Launch_Date', columns='Launch_Pad', values='Payload_Mass')

# Reset index to make Launch_Date a column
pivoted_df = pivoted_df.reset_index()

# Sort by Launch_Date
pivoted_df = pivoted_df.sort_values(by='Launch_Date')

# Save to CSV without index
pivoted_df.to_csv('charts/starlink_mass_vs_date.csv', index=False)
print("CSV file 'starlink_mass_vs_date.csv' has been created.")

# Create scatter plot
plt.figure(figsize=(10, 6))
for pad in pivoted_df.columns[1:]:  # Skip 'Launch_Date'
    plt.scatter(pivoted_df['Launch_Date'], pivoted_df[pad], label=pad, alpha=0.7)

# Customize plot
plt.title('Starlink Launches: Payload Mass vs. Launch Date by Launch Pad')
plt.xlabel('Launch Date')
plt.ylabel('Payload Mass (kg)')
plt.legend(title='Launch Pad')
plt.grid(True)

# Save plot
plt.savefig('examples/outputs/starlink_mass_vs_date.png')
print("Plot saved as 'starlink_mass_vs_date.png'.")