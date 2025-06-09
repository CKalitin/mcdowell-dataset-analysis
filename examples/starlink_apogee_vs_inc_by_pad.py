import mcdowell_dataset_analysis as mda

dataset_name = "starlink_apogee_vs_inclination_by_pad"

# Initialize dataset
dataset = mda.McdowellDataset()

# Filter for Starlink launches
mda.Filters.filter_by_mission(dataset.launch, 'Starlink', case=False)
filtered_df = dataset.launch.df

# Remove 0 payload mass values
filtered_df = filtered_df[filtered_df['Inc'] != 0]

# Pivot for plotting
pivoted_df = mda.ChartUtils.pivot_dataframe(
    filtered_df,
    index_col='Inc',
    column_col='Launch_Pad',
    value_col='Apogee'
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
    x_col='Inc',
    y_cols=pivoted_df.columns,
    title='Starlink Launches: Apogee vs Inclination by Pad',
    subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
    x_label='Inclination (degrees)',
    y_label='Apogee (km)',
    dot_diameter=10,
    output_path=f'examples/outputs/chart/{dataset_name}.png',
    color_map=mda.ChartUtils.f9_site_color_map,
)
