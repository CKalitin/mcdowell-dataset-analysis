import mcdowell_dataset_analysis as mda

def main(start_year):
    dateset_name = f"orbital_launches_vs_year_by_general_launch_payload_type_{start_year}"

    # Initialize dataset
    dataset = mda.McdowellDataset("./datasets")

    # Filter the base dataset
    mda.Filters.filter_by_launch_date(dataset.launch, start_date=f'{start_year}-01-01')
    mda.Filters.filter_by_launch_category(dataset.launch, ['O', 'D'])

    # Add launch year column for easier binning
    dataset.launch.df['Launch_Year'] = dataset.launch.df['Launch_Date'].dt.year

    general_launch_payload_types = ['Starlink', 'Commercial', 'Chinese Commercial', 'Government', 'Eastern Government', 'Military', 'Eastern Military']

    # Create a dictionary with key orbits and values are dataframes for each orbit showing the number of launches per year
    orbit_dataframes = mda.ChartUtils.bin_dataset_into_dictionary_by_filter_function(
        dataset=dataset.launch,
        filter_function=mda.Filters.filter_column_by_exact,
        filter_function_parameters_list=general_launch_payload_types,
        value_col='Launch_Year',
        bins=list(range(start_year-1, 2026)), # -1 because it's weird
        bin_labels=list(range(start_year, 2026)),
        filter_function_additional_parameter="General_Launch_Payload_Type",
    )

    # Combine dictionary of dataframes into a single dataframe (by column)
    output_df = mda.ChartUtils.combine_dictionary_of_dataframes(orbit_dataframes)

    print(output_df)

    output_df.to_csv(f'examples/outputs/csv/{dateset_name}.csv', index=True)
    print(f"CSV file '{dateset_name}.csv' has been created.")

    mda.ChartUtils.plot_bar(
        output_df,
        title='Orbital Launches vs Year by General Launch Payload Type',
        subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label='Year',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{dateset_name}.png',
        color_map=mda.ChartUtils.general_launch_payload_type_color_map,
        bargap=0.1,
        x_tick_step_size=5,
    )
    
main(2000)
main(1957)