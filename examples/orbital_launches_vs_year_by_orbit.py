import mcdowell_dataset_analysis as mda
import copy
import pandas as pd

dateset_name = "orbital_launches_vs_year_by_orbit"

# Initialize dataset
dataset = mda.McdowellDataset("./datasets")

mda.Filters.filter_by_launch_date(dataset.launch, start_date='2000-01-01')
mda.Filters.filter_by_launch_category(dataset.launch, ['O', 'D'])

dataset.launch.df['Launch_Year'] = dataset.launch.df['Launch_Date'].dt.year

orbits = ['LEO', 'SSO', 'MEO', 'GTO', 'GEO', 'HEO', 'BEO']

orbit_counts = {}
for orbit in orbits:
    orbit_df = copy.copy(dataset.launch)
    mda.Filters.filter_by_orbit(orbit_df, orbit)
    orbit_counts[orbit] = mda.ChartUtils.bin_dataframe(orbit_df.df, 'Launch_Year', bins=list(range(1999, 2026)), labels=list(range(2000, 2026)))

output_df = pd.concat(orbit_counts.values(), axis=1)
output_df.columns = orbit_counts.keys()

print(output_df)

output_df.to_csv(f'examples/outputs/{dateset_name}.csv', index=True)
print(f"CSV file '{dateset_name}.csv' has been created.")

mda.ChartUtils.plot_bar(
    output_df,
    title='Orbital Launches vs. Year by Orbit',
    subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
    x_label='Year',
    y_label='Number of Launches',
    output_path=f'examples/outputs/{dateset_name}.png',
    color_map=mda.ChartUtils.orbit_color_map,
    bargap=0.1,
)