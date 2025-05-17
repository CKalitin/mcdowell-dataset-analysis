import mcdowell_dataset_analysis as mda
import pandas as pd
import copy
import plotly.express as px
import plotly.io as pio

# Initialize dataset
dataset = mda.McdowellDataset()

# Filter for Falcon 9 orbital and deep space launches
mda.Filters.filter_by_launch_category(dataset.launch, ['O', 'D'])  # Filter for orbital and deep space launches
mda.Filters.filter_by_launch_vehicle_family(dataset.launch, 'Falcon9')  # Filter for Falcon 9 launches

# Define orbits and bins
orbits = ['LEO', 'SSO', 'MEO', 'GTO', 'GEO', 'HEO', 'BEO']
bins = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000,
        11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000]
mass_labels = ['0-1T', '1-2T', '2-3T', '3-4T', '4-5T', '5-6T', '6-7T', '7-8T', '8-9T', '9-10T',
               '10-11T', '11-12T', '12-13T', '13-14T', '14-15T', '15-16T', '16-17T', '17-18T', '18-19T', '19-20T']

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

# Plot histogram
"""mda.ChartUtils.plot_histogram(
    output_df,
    title='Falcon 9 Launches: Payload Mass by Orbit',
    xlabel='Payload Mass Range (Tons)',
    ylabel='Number of Launches',
    output_path='examples/outputs/f9_mass_by_orbit.png'
)"""

fig = px.histogram(output_df,
                   x=output_df.index,
                   y=output_df.columns,
                   title='Falcon 9 Launches: Payload Mass by Orbit',
                   labels={'x': 'Payload Mass Range (Tons)', 'y': 'Number of Launches'},
                   barmode='group')

pio.write_image(fig, 'examples/outputs/f9_mass_by_orbit.png', format='png', width=800, height=600)