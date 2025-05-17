import mcdowell_dataset_analysis as mda
import pandas as pd
import copy

# Initialize dataset
dataset = mda.McdowellDataset("./datasets")

# Filter for Falcon 9 orbital and deep space launches
mda.Filters.filter_by_launch_category(dataset.launch, ['O', 'D'])  # Filter for orbital and deep space launches
mda.Filters.filter_by_launch_vehicle_family(dataset.launch, 'Falcon9')  # Filter for Falcon 9 launches

# Define orbits and bins
orbits = ['LEO', 'SSO', 'MEO', 'GTO', 'GEO', 'HEO', 'BEO']
bins = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000,
        11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000]
mass_labels = ['0-1t', '1-2t', '2-3t', '3-4t', '4-5t', '5-6t', '6-7t', '7-8t', '8-9t', '9-10t',
               '10-11t', '11-12t', '12-13t', '13-14t', '14-15t', '15-16t', '16-17t', '17-18t', '18-19t', '19-20t']

# Bin data by orbit
orbit_counts = {}
for orbit in orbits:
    orbit_df = copy.copy(dataset.launch)
    mda.Filters.filter_by_orbit(orbit_df, orbit)
    orbit_counts[orbit] = mda.ChartUtils.bin_dataframe(orbit_df.df, 'Payload_Mass', bins, mass_labels)

# Create output DataFrame
output_df = pd.concat(orbit_counts.values(), axis=1)
output_df.columns = orbit_counts.keys()

print(output_df)

# Save to CSV
output_df.to_csv('examples/outputs/f9_mass_by_orbit.csv', index=True)
print("CSV file 'f9_mass_by_orbit.csv' has been created.")

mda.ChartUtils.plot_histogram(
    output_df,
    title='Falcon 9 Launches vs. Payload Mass by Orbit',
    subtitle='Christopher Kalitin 2025 - Data Cutoff: May 16 2025',
    xlabel='Payload Mass Range (tonnes)',
    ylabel='Number of Launches',
    output_path='examples/outputs/f9_mass_by_orbit.png',
    color_map=mda.ChartUtils.orbit_color_map
)
