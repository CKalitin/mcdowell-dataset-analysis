import mcdowell_dataset_analysis as mda

# Initialize dataset
dataset = mda.McdowellDataset()

# Filter for Starlink launches
mda.Filters.filter_by_mission(dataset.launch, 'Starlink', case=False)
filtered_df = dataset.launch.df
print(f"Number of Starlink launches: {len(filtered_df)}")

# Select relevant columns and drop missing Inclination
filtered_df = (
    filtered_df[['Launch_Date', 'Inc', 'Launch_Pad']]
    .dropna(subset=['Inc'])
)

# Remove 0 inclination values
filtered_df = filtered_df[filtered_df['Inc'] != 0]

print(f"Number of launches with valid Inclination: {len(filtered_df)}")
print("Unique launch pads for Starlink launches:")
print(filtered_df['Launch_Pad'].unique())

# Pivot for plotting
pivoted_df = mda.ChartUtils.pivot_dataframe(
    filtered_df,
    index_col='Launch_Date',
    column_col='Launch_Pad',
    value_col='Inc'
)

# Save to CSV
pivoted_df.to_csv(
    'examples/outputs/starlink_inclination_vs_date.csv',
    index=False
)
print("CSV file 'starlink_inclination_vs_date.csv' has been created.")

# Create scatter plot
mda.ChartUtils.plot_scatter(
    pivoted_df,
    x_col='Launch_Date',
    y_cols=pivoted_df.columns[1:],        # skip the date column
    title='Starlink Launches: Inclination vs. Launch Date by Launch Pad',
    subtitle='Christopher Kalitin 2025 – Data Cutoff: May 16 2025',
    x_label='Launch Date',
    y_label='Inclination (degrees)',
    dot_diameter=10,
    output_path='examples/outputs/starlink_inclination_vs_date.png',
    color_map={
        'LC40': '#fbbc04',
        'LC39A': '#cc0000',
        'SLC4E': '#3c78d8',
    },
)
