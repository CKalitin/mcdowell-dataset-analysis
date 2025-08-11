import mcdowell_dataset_analysis as mda
from mcdowell_dataset_analysis import standard_chart_generation as scg
import os

def launches_vs_mass_LEO_excl_russia_china(mass_step_size_kg, chart_title_prefix, output_prefix, mass_suffix='t', mass_divisor=1000):
    # Load and filter dataset
    dataset = mda.McdowellDataset("./datasets")
    
    # Step 1: Filter for orbital and deep space launches
    mda.Filters.filter_by_launch_category(dataset.launch, ['O', 'D'])

    # Step 2: Filter by orbit to LEO only
    mda.Filters.filter_by_orbit(dataset.launch, 'LEO')

    mda.Filters.filter_by_country(dataset.launch, ['Russia', 'Soviet Union', 'China'], negate=True)

    #mda.Filters.filter_column_by_contains(dataset.launch, 'Starlink', 'Mission', negate=True)

    min_mass = 0 #90000
    mda.Filters.filter_by_mass(dataset.launch, min_mass=min_mass)  # Filter out launches with no payload mass

    columns_to_keep = [
        "Launch_Tag", "Launch_Date", "LV_Type", "Flight", "Mission", "Apogee",
        "Agency", "LaunchCode", "Group", "Category", "Notes", "Simple_Orbit",
        "Launch_Vehicle_Simplified", "State", "Country", "Launch_Site_Name",
        "Payload_Mass", "Perigee", "Inc", "OpOrbit", "First_Simple_Payload_Category",
        "First_Payload_Class", "General_Launch_Payload_Type"
    ]

    dataset.launch.df = dataset.launch.df[columns_to_keep]

    # Step 4: Proceed with binning and plotting
    output_name = f"{output_prefix}_launches_vs_mass_LEO_excl_russia_china"
    os.makedirs(f'examples/outputs/raw_dataframes/{output_prefix}', exist_ok=True)
    dataset.launch.df.to_csv(f'examples/outputs/raw_dataframes/{output_prefix}/raw_dataframe_{output_name}.csv', index=False)
    print(f"Dataframe 'raw_dataframe_{output_name}.csv' has been created.")

    max_mass = int(dataset.launch.df['Payload_Mass'].max())
    bins = list(range(min_mass, max_mass + mass_step_size_kg, mass_step_size_kg))
    mass_labels = [f"{int(bins[i]/mass_divisor)}-{int(bins[i+1]/mass_divisor)}{mass_suffix}" for i in range(len(bins)-1)]

    # Bin using General_Launch_Payload_Type (or use any other grouping if desired)
    """dataframes = mda.ChartUtils.bin_dataset_into_dictionary_by_filter_function(
        dataset=dataset.launch,
        filter_function=mda.Filters.filter_column_by_exact,
        filter_function_parameters_list=['LEO'],
        value_col='Payload_Mass',
        bins=bins,
        bin_labels=mass_labels,
        filter_function_additional_parameter='Simple_Orbit'
    )"""
    
    dataset.launch.df = dataset.launch.df[dataset.launch.df['Launch_Vehicle_Simplified'].notna()]
    
    lv = dataset.launch.df['Launch_Vehicle_Simplified'].value_counts().index.tolist()
    
    # Bin using Launch_Vehicle_Simplified
    dataframes = mda.ChartUtils.bin_dataset_into_dictionary_by_filter_function(
        dataset=dataset.launch,
        filter_function=mda.Filters.filter_column_by_exact,
        filter_function_parameters_list=lv,
        value_col='Payload_Mass',
        bins=bins,
        bin_labels=mass_labels,
        filter_function_additional_parameter='Launch_Vehicle_Simplified',
    )

    output_df = mda.ChartUtils.combine_dictionary_of_dataframes(dataframes)
    os.makedirs(f'examples/outputs/csv/{output_prefix}', exist_ok=True)
    output_df.to_csv(f'examples/outputs/csv/{output_prefix}/{output_name}.csv', index=True)
    print(f"CSV file '{output_name}.csv' has been created.")

    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Launches to LEO (Excl. Russia/China) vs. Payload Mass',
        subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label=f'Payload Mass Range ({mass_suffix})',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        color_map=mda.ChartUtils.color_sequence_2_10,  # Optional: single color
        bargap=0.1,
        x_tick_step_size=5
    )

"""launches_vs_mass_LEO_excl_russia_china(
    mass_step_size_kg=1000,
    chart_title_prefix="test",
    output_prefix="test"
)"""

scg.cumulative_payloads_by_filter_vs_date_since_first_payload(
    chart_title_prefix="Constellations",
    output_prefix="payloads",
    filter_function=mda.Filters.filter_column_by_contains,
    filter_function_parameters_list=["Starlink", "OneWeb", "Kuiper"],#, "Iridium SV", "Iridium Next SV"],
    filter_function_additional_parameter="PLName",
    series_names=["Starlink", "OneWeb", "Kuiper"],#, "Iridium", "Iridium Next"],
    start_year=2020,
    end_year=2025,
    line_width=4,
)