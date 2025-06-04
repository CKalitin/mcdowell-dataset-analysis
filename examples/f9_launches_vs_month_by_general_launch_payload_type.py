import mcdowell_dataset_analysis as mda

# end_year is inclusive
def main(start_year, end_year):
    dateset_name = f"f9_launch_vs_month_by_general_launch_payload_type_{start_year}_{end_year}"

    # Initialize dataset
    dataset = mda.McdowellDataset("./datasets")

    # Filter the base dataset
    mda.Filters.filter_by_launch_date(dataset.launch, start_date=f'{start_year}-01-01')
    mda.Filters.filter_by_launch_category(dataset.launch, ['O', 'D'])
    mda.Filters.filter_by_launch_vehicle_raw_name(dataset.launch, "Falcon 9")

    # Encode launch month as year*12 + months to get total months since Jesus instead of years since Jesus
    dataset.launch.df['Launch_Month'] = dataset.launch.df['Launch_Date'].dt.year*12 + dataset.launch.df['Launch_Date'].dt.month
    
    general_launch_payload_Types = ['Starlink', 'Commercial', 'Chinese Commercial', 'Government', 'Eastern Government', 'Military', 'Eastern Military']
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    bin_labels = []
    for year in range(start_year, end_year+1, 1):
        for month in months:
            bin_labels.append(f"{month} {year}")

    # Create a dictionary with key orbits and values are dataframes for each orbit showing the number of launches per year
    orbit_dataframes = mda.ChartUtils.bin_dataset_into_dictionary_by_filter_function(
        dataset=dataset.launch,
        filter_function=mda.Filters.filter_column_by_contains,
        filter_function_parameters_list=general_launch_payload_Types,
        value_col='Launch_Month',
        bins=list(range(start_year*12, (end_year+1)*12+1)), # +1 year bc its exclusive, again +1 to align bins to months for some reason ugh pandas wtf investigate this future Chris
        bin_labels=bin_labels,
        filter_function_additional_parameter="General_Launch_Payload_Type"
    )

    # Combine dictionary of dataframes into a single dataframe (by column)
    output_df = mda.ChartUtils.combine_dictionary_of_dataframes(orbit_dataframes)

    print(output_df)

    output_df.to_csv(f'examples/outputs/csv/{dateset_name}.csv', index=True)
    print(f"CSV file '{dateset_name}.csv' has been created.")

    mda.ChartUtils.plot_bar(
        output_df,
        title='F9 Launches vs Month by General Launch Payload Type',
        subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label='Date',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{dateset_name}.png',
        color_map=mda.ChartUtils.general_launch_payload_type_color_map,
        bargap=0.0,
        x_tick0=0,
        x_tick_step_size=12
    )
    
main(2010, 2025)