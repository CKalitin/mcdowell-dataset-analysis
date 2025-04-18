import mcdowell_dataset_analysis as mda
import pandas as pd
import numpy as np
import copy

# Initialize dataset
dataset = mda.McdowellDataset()

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Filter for orbital and deep space launches, and Falcon 9 family
mda.Filters.filter_by_launch_category(dataset.launch, ['O', 'D'])  # Filter for orbital and deep space launches
mda.Filters.filter_by_launch_vehicle_family(dataset.launch, 'Falcon9')  # Filter for F9 and F9 Heavy

# Define orbit types in desired order
orbits = ['LEO', 'SSO', 'MEO', 'GTO', 'GEO', 'HEO', 'BEO']

# Separate the DataFrame into one DataFrame per orbit type (stored in a dictionary)
orbit_dfs = {}
for orbit in orbits:
    orbit_df = copy.copy(dataset.launch)
    mda.Filters.filter_by_orbit(orbit_df, orbit)
    orbit_dfs[orbit] = orbit_df

# Define payload mass bins and labels
bins = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000]
mass_labels = ['0-1T', '1-2T', '2-3T', '3-4T', '4-5T', '5-6T', '6-7T', '7-8T', '8-9T', '9-10T', '10-11T', '11-12T', '12-13T', '13-14T', '14-15T', '15-16T', '16-17T', '17-18T', '18-19T', '19-20T']

# Calculate total payload mass for each mass range and orbit
orbit_masses = {}
for orbit, orbit_df in orbit_dfs.items():
    # Create a column for mass range bins
    orbit_df.df['Mass_Range'] = pd.cut(
        orbit_df.df['Payload_Mass'],
        bins=bins,
        labels=mass_labels,
        include_lowest=True,
        right=True
    )
    # Group by mass range and sum the Payload_Mass
    total_mass = orbit_df.df.groupby('Mass_Range')['Payload_Mass'].sum()
    # Reindex to include all mass ranges, filling missing with 0
    total_mass = total_mass.reindex(mass_labels, fill_value=0)
    orbit_masses[orbit] = total_mass

# Create the final DataFrame with mass ranges as index and orbit types as columns
output_df = pd.DataFrame(orbit_masses)
output_df.index.name = 'Payload_Mass_Range'

# Print the final DataFrame
print("\nFinal DataFrame (Total Payload Mass in kg):")

# Save to CSV
output_df.to_csv('charts/total_mass_by_orbit_and_mass_range.csv', index=True)