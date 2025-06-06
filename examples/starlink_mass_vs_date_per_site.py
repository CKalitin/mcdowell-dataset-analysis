import mcdowell_dataset_analysis as mda

dataset_name = "starlink_mass_vs_date_by_pad"

# Initialize dataset
dataset = mda.McdowellDataset()

# Filter for Starlink launches
mda.Filters.filter_by_mission(dataset.launch, 'Starlink', case=False)
filtered_df = dataset.launch.df
print(f"Number of Starlink launches: {len(filtered_df)}")

# Select relevant columns and drop missing Payload_Mass
filtered_df = (
    filtered_df[
        ['Launch_Date', 'Payload_Mass', 'Launch_Pad']
    ]
    .dropna(subset=['Payload_Mass'])
)

# Remove 0 payload mass values
filtered_df = filtered_df[filtered_df['Payload_Mass'] != 0]

print(f"Number of launches with valid Payload_Mass: {len(filtered_df)}")
print("Unique launch pads for Starlink launches:")
print(filtered_df['Launch_Pad'].unique())

# Pivot for plotting
pivoted_df = mda.ChartUtils.pivot_dataframe(
    filtered_df,
    index_col='Launch_Date',
    column_col='Launch_Pad',
    value_col='Payload_Mass'
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
    x_col='Launch_Date',
    y_cols=pivoted_df.columns[1:],
    title='Starlink Launches: Payload Mass vs. Launch Date by Pad',
    subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
    x_label='Launch Date',
    y_label='Payload Mass (t)',
    y_scaling_factor=1e-3,  # Convert kg to metric tons
    dot_diameter=10,
    output_path=f'examples/outputs/chart/{dataset_name}.png',
    color_map={
        'LC40': '#fbbc04',
        'LC39A': '#cc0000',
        'SLC4E': '#3c78d8',
    },
)
