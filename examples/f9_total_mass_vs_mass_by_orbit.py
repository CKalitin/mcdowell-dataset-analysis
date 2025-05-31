import mcdowell_dataset_analysis as mda
import pandas as pd
import copy

output_name = "f9_total_mass_vs_mass_by_orbit"

# Initialize dataset
dataset = mda.McdowellDataset()

mda.Filters.filter_by_launch_category(dataset.launch, ['O', 'D'])  # Filter for orbital and deep space launches
mda.Filters.filter_by_launch_vehicle_family(dataset.launch, 'Falcon9')  # Filter for Falcon 9 launches

# Define orbit types in desired order
orbits = ['LEO', 'SSO', 'MEO', 'GTO', 'GEO', 'HEO', 'BEO']
bins = list(range(0, 19000, 1000))
mass_labels = [f"{int(bins[i]/1000)}-{int(bins[i+1]/1000)}t" for i in range(len(bins)-1)]

orbit_dataframes = mda.ChartUtils.bin_dataset_into_dictionary_by_filter_function(
    dataset=dataset.launch,
    filter_function=mda.Filters.filter_by_orbit,
    filter_function_parameters=orbits,
    value_col='Payload_Mass',
    bins=bins,
    bin_labels=mass_labels,
    count_values=False,
    bin_column = 'Mass_Range'
)

orbit_masses = {}
for orbit_dataframe_key in orbit_dataframes.keys():
    total_mass = orbit_dataframes[orbit_dataframe_key].groupby('Mass_Range', observed=False)['Payload_Mass'].sum() # Sum mass in payload range for this orbit
    total_mass = total_mass.reindex(mass_labels, fill_value=0)
    orbit_masses[orbit_dataframe_key] = total_mass/1000

output_df = mda.ChartUtils.combine_dictionary_of_dataframes(orbit_masses)

print(output_df)

# Save to CSV
output_df.to_csv(f'examples/outputs/csv/{output_name}.csv', index=True)
print(f"CSV file '{output_name}.csv' has been created.")

# Plot stacked bar chart
mda.ChartUtils.plot_bar(
    output_df,
    title='Falcon 9 Net Payload Mass vs Mass Range by Orbit',
    subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
    x_label='Payload Mass Range (tonnes)',
    y_label='Total Payload Mass (tonnes)',
    output_path=f'examples/outputs/chart/{output_name}.png',
    color_map=mda.ChartUtils.orbit_color_map,
    bargap=0.1
)