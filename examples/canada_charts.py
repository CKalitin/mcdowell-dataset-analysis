import mcdowell_dataset_analysis as mda
import standard_chart_generation as scg
import os

chart_title_prefix = "Canada"
output_prefix = "canada"

def simple_payload_category_per_year():
    dataset = mda.McdowellDataset("./datasets")

    output_name = f"canada_payloads_vs_year_by_simple_payload_category"

    simple_payload_categories = mda.Translation.payload_category_to_simple_payload_category.values()

    # Only include payloads with a simple payload category, which probably means orbital payloads
    mda.Filters.filter_by_sat_type_coarse(dataset.satcat, 'P')
    mda.Filters.filter_by_country(dataset.satcat, "Canada")

    dataset.satcat.df['Launch_Year'] = dataset.satcat.df['Launch_Date'].dt.year

    os.makedirs(f'examples/outputs/raw_dataframes/payloads', exist_ok=True)
    dataset.satcat.df.to_csv(f'examples/outputs/raw_dataframes/payloads/{output_name}.csv', index=False)
    print(f"Dataframe 'raw_dataframe_{output_name}.csv' has been created.")

    dataframes = mda.ChartUtils.group_dataset_into_dictionary_by_filter_function(
        dataset.satcat,
        filter_function=mda.Filters.filter_by_simple_payload_category,
        groups=simple_payload_categories,
        groupby_col="Launch_Year",
        count_values=True,
    )

    output_df = mda.ChartUtils.combine_dictionary_of_dataframes(dataframes)

    os.makedirs(f'examples/outputs/csv/payloads', exist_ok=True)
    output_df.to_csv(f"examples/outputs/csv/payloads/{output_name}.csv", index=True)
    print(f"CSV file '{output_name}.csv' has been created.")

    os.makedirs(f'examples/outputs/chart/payloads', exist_ok=True)
    mda.ChartUtils.plot_bar(
        output_df,
        title="Canada Payloads vs Year by Simple Payload Category",
        subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label="Year",
        y_label="Number of Payloads",
        output_path=f'examples/outputs/chart/payloads/{output_name}.png',
        color_map=mda.ChartUtils.simple_payload_category_color_map,
        bargap=0.0,
        x_tick0=0,
        x_tick_step_size=5
    )


def com_gov_mil_per_year():
    dataset = mda.McdowellDataset("./datasets")

    output_name = f"canada_payloads_vs_year_by_operator_type"

    filter_parameters = ["Academic", "Commercial", "Government", "Military"]
    filter_parameter_translate = {"A": "Academic",
                                  "B": "Commercial",
                                  "C": "Government",
                                  "D": "Military",
                                  }

    dataset.satcat.df['Payload_Category_Name'] = dataset.satcat.df['Payload_Class'].replace(filter_parameter_translate)

    # Only include payloads with a simple payload category, which probably means orbital payloads
    # Nah I'm not updating comments the wind turbines and trees are too nice, just exited Cheyenne Wyoming
    mda.Filters.filter_by_sat_type_coarse(dataset.satcat, 'P')
    mda.Filters.filter_by_country(dataset.satcat, "Canada")

    dataset.satcat.df['Launch_Year'] = dataset.satcat.df['Launch_Date'].dt.year

    # If sat owner is DRDC/UTIAS, it is a military payload
    # Manual set
    dataset.satcat.df.loc[
        dataset.satcat.df['Owner'].str.contains("DRDC|UTIAS", case=False, na=False),
        'Payload_Category_Name'
    ] = "Military"

    os.makedirs(f'examples/outputs/raw_dataframes/payloads', exist_ok=True)
    dataset.satcat.df.to_csv(f'examples/outputs/raw_dataframes/payloads/{output_name}.csv', index=False)
    print(f"Dataframe 'raw_dataframe_{output_name}.csv' has been created.")

    dataframes = mda.ChartUtils.group_dataset_into_dictionary_by_filter_function(
        dataset.satcat,
        filter_function=mda.Filters.filter_column_by_exact,
        groups=filter_parameters,
        groupby_col="Launch_Year",
        count_values=True,
        filter_function_additional_parameter="Payload_Category_Name",
    )

    output_df = mda.ChartUtils.combine_dictionary_of_dataframes(dataframes)

    os.makedirs(f'examples/outputs/csv/payloads', exist_ok=True)
    output_df.to_csv(f"examples/outputs/csv/payloads/{output_name}.csv", index=True)
    print(f"CSV file '{output_name}.csv' has been created.")

    os.makedirs(f'examples/outputs/chart/payloads', exist_ok=True)
    mda.ChartUtils.plot_bar(
        output_df,
        title="Canada Payloads vs Year by Operator Type",
        subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label="Year",
        y_label="Number of Payloads",
        output_path=f'examples/outputs/chart/payloads/{output_name}.png',
        color_map=mda.ChartUtils.payload_operator_color_map,
        bargap=0.0,
        x_tick0=0,
        x_tick_step_size=5
    )

simple_payload_category_per_year()
com_gov_mil_per_year()

scg.payloads_vs_mass_by_filter(
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    chart_title_suffix='Orbit',
    output_suffix='orbit_max_mass',
    filter_function=mda.Filters.filter_by_orbit,
    filter_function_parameters_list=['LEO', 'SSO', 'MEO', 'GTO', 'GEO', 'HEO', 'BEO'],
    filter_function_additional_parameter=None,
    mass_step_size_kg=1000,
    launch_vehicle_simplified_name=None,
    launch_vehicle_family=None,
    color_map=mda.ChartUtils.orbit_color_map,
    mass_suffix="t",
    mass_divisor=1000,
    country="Canada",
)

scg.payloads_vs_mass_by_filter(
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    chart_title_suffix='Orbit',
    output_suffix='orbit_100_5',
    filter_function=mda.Filters.filter_by_orbit,
    filter_function_parameters_list=['LEO', 'SSO', 'MEO', 'GTO', 'GEO', 'HEO', 'BEO'],
    filter_function_additional_parameter=None,
    mass_step_size_kg=5,
    launch_vehicle_simplified_name=None,
    launch_vehicle_family=None,
    color_map=mda.ChartUtils.orbit_color_map,
    mass_suffix="kg",
    mass_divisor=1,
    country="Canada",
    max_mass=100,
)

scg.payloads_vs_mass_by_filter(
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    chart_title_suffix='Orbit',
    output_suffix='orbit_1000_50',
    filter_function=mda.Filters.filter_by_orbit,
    filter_function_parameters_list=['LEO', 'SSO', 'MEO', 'GTO', 'GEO', 'HEO', 'BEO'],
    filter_function_additional_parameter=None,
    mass_step_size_kg=50,
    launch_vehicle_simplified_name=None,
    launch_vehicle_family=None,
    color_map=mda.ChartUtils.orbit_color_map,
    mass_suffix="kg",
    mass_divisor=1,
    country="Canada",
    max_mass=1000,
)