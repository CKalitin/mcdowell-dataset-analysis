import mcdowell_dataset_analysis as mda

dataset_name = "starlink_inclination_vs_apogee_by_pad"

# Initialize dataset
dataset = mda.McdowellDataset()

# Filter for Starlink launches
mda.Filters.filter_by_mission(dataset.launch, 'Starlink', case=False)
filtered_df = dataset.launch.df
print(f"Number of Starlink launches: {len(filtered_df)}")

# Select relevant columns and drop missing Payload_Mass
"""filtered_df = (
    filtered_df[
        ['Apogee', 'Inc', 'Launch_Pad']
    ]
    .dropna(subset=['Inc'])
)"""

# Remove 0 payload mass values
filtered_df = filtered_df[filtered_df['Inc'] != 0]

print(f"Number of launches with valid Payload_Mass: {len(filtered_df)}")
print("Unique launch pads for Starlink launches:")
print(filtered_df['Launch_Pad'].unique())

# Pivot for plotting
pivoted_df = mda.ChartUtils.pivot_dataframe(
    filtered_df,
    index_col='Apogee',
    column_col='Launch_Pad',
    value_col='Inc'
)

# Save to CSV
pivoted_df.to_csv(
    f'examples/outputs/csv/{dataset_name}.csv',
    index=False
)
print(f"CSV file '{dataset_name}.csv' has been created.")

# Create scatter plot
mda.ChartUtils.plot_scatter(
    pivoted_df,
    x_col='Apogee',
    y_cols=pivoted_df.columns,        # skip the date column
    title='Starlink Launches: Inclination vs Apogee by Pad',
    subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
    x_label='Apogee (km)',
    y_label='Inclination (degrees)',
    dot_diameter=10,
    output_path=f'examples/outputs/chart/{dataset_name}.png',
    color_map=mda.ChartUtils.f9_site_color_map,
)
