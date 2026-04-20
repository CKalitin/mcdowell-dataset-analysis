import mcdowell_dataset_analysis as mda
from datetime import datetime
import pandas as pd

def generate_launch_vehicle_charts(launch_vehicle_simplified_name, chart_title_prefix, output_prefix, mass_step_size_kg=1000, year_x_tick_step_size=1, month_x_tick_step_size=12, filter_out_suborbital=True):
    """Generate a series of charts for a specific launch vehicle.

    Charts:
        - Launches vs Mass by Orbit
        - Total Mass vs Mass by Orbit
        - Launches vs Mass by General Launch Payload Type
        - Total Mass vs Mass by General Launch Payload Type
        - Launches vs Month by General Launch Payload Type
        - Launches vs Month by Orbit
        - Launches vs Year by General Launch Payload Type
        - Launches vs Year by Orbit

    Args:
        launch_vehicle_simplified_name (str): The simplified name of the launch vehicle.
        chart_title_prefix (str): The prefix for the chart titles.
        output_prefix (str): The prefix for the output file names.
        mass_step_size_kg (int, optional): The step size for mass ranges in kg. Defaults to 1000.
        year_x_tick_step_size (int, optional): The step size for year ticks on the x-axis. Defaults to 1.
        month_x_tick_step_size (int, optional): The step size for month ticks on the x-axis. Defaults to 12.
        filter_out_suborbital (bool, optional): Whether to filter out suborbital launches. Defaults to True.
    """
    
    mass_suffix = "t" if mass_step_size_kg == 1000 else "kg"
    mass_divisor = 1000 if mass_step_size_kg == 1000 else 1

    launches_vs_mass_by_orbit(
        launch_vehicle_simplified_name=launch_vehicle_simplified_name,
        mass_step_size_kg=mass_step_size_kg,
        chart_title_prefix=chart_title_prefix,
        output_prefix=output_prefix,
        mass_suffix=mass_suffix,
        mass_divisor=mass_divisor,
        filter_out_suborbital=filter_out_suborbital,
    )

    total_mass_vs_mass_by_orbit(
        launch_vehicle_simplified_name=launch_vehicle_simplified_name,
        mass_step_size_kg=mass_step_size_kg,
        chart_title_prefix=chart_title_prefix,
        output_prefix=output_prefix,
        mass_suffix=mass_suffix,
        mass_divisor=mass_divisor,
        filter_out_suborbital=filter_out_suborbital,
    )

    launches_vs_mass_by_general_launch_payload_type(
        launch_vehicle_simplified_name=launch_vehicle_simplified_name,
        mass_step_size_kg=mass_step_size_kg,
        chart_title_prefix=chart_title_prefix,
        output_prefix=output_prefix,
        mass_suffix=mass_suffix,
        mass_divisor=mass_divisor,
        filter_out_suborbital=filter_out_suborbital,
    )

    total_mass_vs_mass_by_general_launch_payload_type(
        launch_vehicle_simplified_name=launch_vehicle_simplified_name,
        mass_step_size_kg=mass_step_size_kg,
        chart_title_prefix=chart_title_prefix,
        output_prefix=output_prefix,
        mass_suffix=mass_suffix,
        mass_divisor=mass_divisor,
        filter_out_suborbital=filter_out_suborbital,
    )

    launches_vs_month_by_general_launch_payload_type(
        launch_vehicle_simplified_name=launch_vehicle_simplified_name,
        chart_title_prefix=chart_title_prefix,
        output_prefix=output_prefix,
        x_tick_step_size=month_x_tick_step_size,
        filter_out_suborbital=filter_out_suborbital,
    )

    launches_vs_month_by_orbit(
        launch_vehicle_simplified_name=launch_vehicle_simplified_name,
        chart_title_prefix=chart_title_prefix,
        output_prefix=output_prefix,
        x_tick_step_size=month_x_tick_step_size,
        filter_out_suborbital=filter_out_suborbital,
    )

    launches_vs_year_by_general_launch_payload_type(
        launch_vehicle_simplified_name=launch_vehicle_simplified_name,
        chart_title_prefix=chart_title_prefix,
        output_prefix=output_prefix,
        x_tick_step_size=year_x_tick_step_size,
        filter_out_suborbital=filter_out_suborbital,
    )

    launches_vs_year_by_orbit(
        launch_vehicle_simplified_name=launch_vehicle_simplified_name,
        chart_title_prefix=chart_title_prefix,
        output_prefix=output_prefix,
        x_tick_step_size=year_x_tick_step_size,
        filter_out_suborbital=filter_out_suborbital,
    )

def generate_launch_vehicle_scatter_plots(launch_vehicle_simplified_name, chart_title_prefix, output_prefix, mass_step_size_kg=1000, filter_out_suborbital=True):
    """Generate scatter plots for a specific launch vehicle.
    
    Charts:
        - Launch Apogee vs Inclination by Orbit
        - Launch Apogee vs Date by Apogee and Orbit
        - Launch Inclination vs Date by Inclination and Orbit
        - Launch Payload Mass vs Date by Payload Mass and Orbit

    Args:
        launch_vehicle_simplified_name (str): The simplified name of the launch vehicle.
        chart_title_prefix (str): The prefix for the chart titles.
        output_prefix (str): The prefix for the output file names.
        mass_step_size_kg (int, optional): The step size for mass ranges in kg. Defaults to 1000.
        filter_out_suborbital (bool, optional): Whether to filter out suborbital launches. Defaults to True.
    """
    
    mass_suffix = "t" if mass_step_size_kg == 1000 else "kg"
    mass_multiplier = 0.001 if mass_step_size_kg == 1000 else 1
    
    launch_apogee_vs_inclination_by_filter_scatter(
        chart_title_prefix=chart_title_prefix,
        output_prefix=output_prefix,
        series_column='Simple_Orbit',
        filter_function=mda.Filters.filter_by_launch_vehicle_name_simplified,
        filter_function_parameter=launch_vehicle_simplified_name,
        series_title='Orbit',
        color_map=mda.ChartUtils.orbit_color_map,
        filter_out_suborbital=filter_out_suborbital,
    )

    launch_value_vs_date_by_filter_scatter(
        chart_title_prefix=chart_title_prefix,
        output_prefix=output_prefix,
        value_column='Apogee',
        series_column='Simple_Orbit',
        filter_function=mda.Filters.filter_by_launch_vehicle_name_simplified,
        filter_function_parameter=launch_vehicle_simplified_name,
        x_axis_title_suffix="(km)",
        value_title='Apogee',
        series_title='Orbit',
        color_map=mda.ChartUtils.orbit_color_map,
        x_axis_type='date',
        filter_out_suborbital=filter_out_suborbital,
    )

    launch_value_vs_date_by_filter_scatter(
        chart_title_prefix=chart_title_prefix,
        output_prefix=output_prefix,
        value_column='Inc',
        series_column='Simple_Orbit',
        filter_function=mda.Filters.filter_by_launch_vehicle_name_simplified,
        filter_function_parameter=launch_vehicle_simplified_name,
        x_axis_title_suffix="(degrees)",
        value_title='Inclination',
        series_title='Orbit',
        color_map=mda.ChartUtils.orbit_color_map,
        x_axis_type='date',
        filter_out_suborbital=filter_out_suborbital,
    )

    launch_value_vs_date_by_filter_scatter(
        chart_title_prefix=chart_title_prefix,
        output_prefix=output_prefix,
        value_column='Payload_Mass',
        series_column='Simple_Orbit',
        filter_function=mda.Filters.filter_by_launch_vehicle_name_simplified,
        filter_function_parameter=launch_vehicle_simplified_name,
        x_axis_title_suffix=f"({mass_suffix})",
        value_title='Payload Mass',
        series_title='Orbit',
        color_map=mda.ChartUtils.orbit_color_map,
        y_scaling_factor=mass_multiplier,
        x_axis_type='date',
        filter_out_suborbital=filter_out_suborbital,
    )

def generate_launch_vehicle_family_charts(launch_vehicle_simplified_name, chart_title_prefix, output_prefix, mass_step_size_kg=1000, year_x_tick_step_size=1, color_map=mda.ChartUtils.color_sequence_2_8, filter_out_suborbital=True):
    """Generate charts for a specific launch vehicle family.

    This is used on top of generate_launch_vehicle_charts if you want a charts that break down launches by vehicle, ie. for the multiple vehicles in a family (eg. Ariane 1 to 5).

    Args:
        launch_vehicle_simplified_name (str): The simplified name of the launch vehicle.
        chart_title_prefix (str): The prefix for the chart titles.
        output_prefix (str): The prefix for the output file names.
        mass_step_size_kg (int, optional): _description_. Defaults to 1000.
        year_x_tick_step_size (int, optional): _description_. Defaults to 1.
        color_map (_type_, optional): _description_. Defaults to mda.ChartUtils.color_sequence_2_8.
        filter_out_suborbital (bool, optional): Whether to filter out suborbital launches. Defaults to True.
    """
    
    mass_suffix = "t" if mass_step_size_kg == 1000 else "kg"
    mass_divisor = 1000 if mass_step_size_kg == 1000 else 1
    
    launches_vs_mass_by_filter(
        chart_title_prefix=chart_title_prefix,
        output_prefix=output_prefix,
        chart_title_suffix='Launch Vehicle',
        output_suffix='launch_vehicle',
        filter_function=mda.Filters.filter_by_launch_vehicle_name_simplified,
        filter_function_parameters_list=launch_vehicle_simplified_name,
        launch_vehicle_simplified_name=launch_vehicle_simplified_name,
        mass_step_size_kg=mass_step_size_kg,
        color_map=color_map,
        mass_suffix=mass_suffix,
        mass_divisor=mass_divisor,
        filter_out_suborbital=filter_out_suborbital,
    )

    total_mass_vs_mass_by_filter(
        chart_title_prefix=chart_title_prefix,
        output_prefix=output_prefix,
        chart_title_suffix='Launch Vehicle',
        output_suffix='launch_vehicle',
        filter_function=mda.Filters.filter_by_launch_vehicle_name_simplified,
        filter_function_parameters_list=launch_vehicle_simplified_name,
        launch_vehicle_simplified_name=launch_vehicle_simplified_name,
        mass_step_size_kg=mass_step_size_kg,
        color_map=color_map,
        mass_suffix=mass_suffix,
        mass_divisor=mass_divisor,
        filter_out_suborbital=filter_out_suborbital,
    )

    launches_vs_year_by_filter(
        chart_title_prefix=chart_title_prefix,
        output_prefix=output_prefix,
        chart_title_suffix='Launch Vehicle',
        output_suffix='launch_vehicle',
        filter_function=mda.Filters.filter_by_launch_vehicle_name_simplified,
        filter_function_parameters_list=launch_vehicle_simplified_name,
        launch_vehicle_simplified_name=launch_vehicle_simplified_name,
        x_tick_step_size=year_x_tick_step_size,
        color_map=color_map,
        filter_out_suborbital=filter_out_suborbital,
    )


def generate_extra_charts(launch_vehicle_simplified_name, chart_title_prefix, output_prefix, mass_step_size_kg=1000, year_x_tick_step_size=1, month_x_tick_step_size=12, color_map=mda.ChartUtils.color_sequence_2_8, filter_out_suborbital=True):
    """Generate extra charts.
    
    Charts:
        - Launch vs Mass by Launch Site
        - Total Mass vs Mass by Launch Site
        - Launces vs Year by Launch Site
    
    Args:
        launch_vehicle_simplified_name (str): The simplified name of the launch vehicle.
        chart_title_prefix (str): The prefix for the chart titles.
        output_prefix (str): The prefix for the output file names.
        mass_step_size_kg (int, optional): _description_. Defaults to 1000.
        year_x_tick_step_size (int, optional): _description_. Defaults to 1.
        month_x_tick_step_size (int, optional): _description_. Defaults to 12.
        color_map (_type_, optional): _description_. Defaults to mda.ChartUtils.color_sequence_2_8.
        filter_out_suborbital (bool, optional): Whether to filter out suborbital launches. Defaults to True.
    """
    
    mass_suffix = "t" if mass_step_size_kg == 1000 else "kg"
    mass_divisor = 1000 if mass_step_size_kg == 1000 else 1
    
    # Get every Launch_Pad (column 11) from launch.tsv, bypassing mda since it's not initialized yet
    launch_df = pd.read_csv("./datasets/launch.tsv", sep="\t", encoding="utf-8", low_memory=False)
    launch_sites = launch_df["Launch_Pad"].dropna().unique().tolist()
    
    color_map = mda.ChartUtils.f9_site_color_map if "Falcon 9" in launch_vehicle_simplified_name else color_map
    
    launches_vs_month_by_filter(
        chart_title_prefix=chart_title_prefix,
        output_prefix=output_prefix,
        chart_title_suffix='Launch Pad',
        output_suffix='launch_pad',
        filter_function=mda.Filters.filter_by_launch_pad_raw,
        filter_function_parameters_list=launch_sites,
        launch_vehicle_simplified_name=launch_vehicle_simplified_name,
        x_tick_step_size=month_x_tick_step_size,
        color_map=color_map,
        filter_out_suborbital=filter_out_suborbital,
    )

    launches_vs_year_by_filter(
        chart_title_prefix=chart_title_prefix,
        output_prefix=output_prefix,
        chart_title_suffix='Launch Pad',
        output_suffix='launch_pad',
        filter_function=mda.Filters.filter_by_launch_pad_raw,
        filter_function_parameters_list=launch_sites,
        launch_vehicle_simplified_name=launch_vehicle_simplified_name,
        x_tick_step_size=year_x_tick_step_size,
        color_map=color_map,
        filter_out_suborbital=filter_out_suborbital,
    )
    
    launches_vs_mass_by_filter(
        chart_title_prefix=chart_title_prefix,
        output_prefix=output_prefix,
        chart_title_suffix='Launch Pad',
        output_suffix='launch_pad',
        filter_function=mda.Filters.filter_by_launch_pad_raw,
        filter_function_parameters_list=launch_sites,
        launch_vehicle_simplified_name=launch_vehicle_simplified_name,
        mass_step_size_kg=mass_step_size_kg,
        color_map=color_map,
        mass_suffix=mass_suffix,
        mass_divisor=mass_divisor,
        filter_out_suborbital=filter_out_suborbital,
    )

    total_mass_vs_mass_by_filter(
        chart_title_prefix=chart_title_prefix,
        output_prefix=output_prefix,
        chart_title_suffix='Launch Pad',
        output_suffix='launch_pad',
        filter_function=mda.Filters.filter_by_launch_pad_raw,
        filter_function_parameters_list=launch_sites,
        launch_vehicle_simplified_name=launch_vehicle_simplified_name,
        mass_step_size_kg=mass_step_size_kg,
        color_map=color_map,
        mass_suffix=mass_suffix,
        mass_divisor=mass_divisor,
        filter_out_suborbital=filter_out_suborbital,
    )


def launches_vs_mass_by_filter(chart_title_prefix, output_prefix, chart_title_suffix, output_suffix, filter_function, filter_function_parameters_list, filter_function_additional_parameter=None, mass_step_size_kg=1000, launch_vehicle_simplified_name=None, launch_vehicle_family=None, color_map=None, mass_suffix='t', mass_divisor=100, filter_out_suborbital=True):
    """Generate a chart showing the number of launches by payload mass range by a given filter function (eg. launch vehicle, launch category, etc.).
    Eg. How many launches were 2-3 tonnes and LEO, how many 6-7 tonnes and GTO, etc.

    Args:
        chart_title_prefix (str): Prefix for the chart title (should be the prettified name of the launch vehicle) (eg. 'Falcon 9') 
        output_prefix (str): Simplified name of LV for output files (eg. 'f9' for Falcon 9 gives "f9_launches_vs_mass_by_orbit")
        filter_function (function): Function to filter the dataset by (eg. mda.Filters.filter_by_launch_vehicle_name_simplified)
        filter_function_parameters_list (list): List of parameters to pass to the filter function
        filter_function_additional_parameter (str): Additional parameter to pass to the filter function if needed
        mass_step_size_kg (int): Step size in kg for the mass bins (eg. 1000 gives bins of 0-1000 kg, 1000-2000 kg, etc.)
        launch_vehicle_simplified_name (str, optional): Launch vehicle to filter by
        launch_vehicle_family (str, optional): Family of launch vehicle to filter by. If not none, then filtering will be done by family instead of the launch_vehicle field.
        mass_suffix (str, optional): Suffix for the mass labels (default is 't' for tonnes, use 'kg' if you want). Defaults to 't'.
        mass_divisor (int, optional): Divisor for the mass values in the chart (default is 1000 to convert kg to tonnes). Defaults to 1000.
    """
    
    output_name = f"{output_prefix}_launches_vs_mass_by_{output_suffix}"

    # Initialize dataset
    dataset = mda.McdowellDataset("./datasets")

    # Filter the base dataset
    if filter_out_suborbital:
        mda.Filters.filter_by_launch_category(dataset.launch, ['O', 'D'])  # Filter for orbital and deep space launches
    if launch_vehicle_family is not None:
        mda.Filters.filter_by_launch_vehicle_family(dataset.launch, launch_vehicle_family)
    else:
        mda.Filters.filter_by_launch_vehicle_name_simplified(dataset.launch, launch_vehicle_simplified_name)

    mda.ChartUtils.log_and_save_df("dataframe", output_name, output_prefix, dataset.launch.df)
    
    max_mass = int(dataset.launch.df['Payload_Mass'].max())

    # Define mass bins and labels
    bins = list(range(0, max_mass+mass_step_size_kg, mass_step_size_kg)) # +mass_step_size_kg bc. range is exclusive
    mass_labels = [f"{int(bins[i]/mass_divisor)}-{int(bins[i+1]/mass_divisor)}{mass_suffix}" for i in range(len(bins)-1)]

    # Create a dictionary with key orbits and values are dataframes for each orbit showing the number of launches per payload mass range
    dataframes = mda.ChartUtils.bin_dataset_into_dictionary_by_filter_function(
        dataset=dataset.launch,
        filter_function=filter_function,
        filter_function_parameters_list=filter_function_parameters_list,
        value_col='Payload_Mass',
        bins=bins,
        bin_labels=mass_labels,
        filter_function_additional_parameter=filter_function_additional_parameter,
    )
    
    # remove dataframes with no data or all zeroes, so that launch pad filtering doesn't include literally all pads ever
    if filter_function == mda.Filters.filter_by_launch_pad_raw:
        dataframes = {key: df for key, df in dataframes.items() if not df.empty and df.sum().sum() > 0}

    # Create dictionary with columns that are the orbits and values are the mass ranges
    output_df = mda.ChartUtils.combine_dictionary_of_dataframes(dataframes)

    # Save to CSV
    mda.ChartUtils.log_and_save_df("csv", output_name, output_prefix, output_df)

    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Launches vs. Payload Mass by {chart_title_suffix}',
        subtitle=f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label=f'Payload Mass Range ({mass_suffix})',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        color_map=color_map,
        bargap=0.1,
    )
    
def launches_vs_mass_by_orbit(mass_step_size_kg, chart_title_prefix, output_prefix, launch_vehicle_simplified_name=None, launch_vehicle_family=None, mass_suffix='t', mass_divisor=1000, filter_out_suborbital=True):
    # Wrapper for back compatibility bc I don't want to ctrl f and replace them all
    launches_vs_mass_by_filter(
        chart_title_prefix=chart_title_prefix,
        output_prefix=output_prefix,
        chart_title_suffix='Orbit',
        output_suffix='orbit',
        filter_function=mda.Filters.filter_by_orbit,
        filter_function_parameters_list=['LEO', 'SSO', 'MEO', 'GTO', 'GEO', 'HEO', 'BEO'],
        filter_function_additional_parameter=None,
        mass_step_size_kg=mass_step_size_kg,
        launch_vehicle_simplified_name=launch_vehicle_simplified_name,
        launch_vehicle_family=launch_vehicle_family,
        color_map=mda.ChartUtils.orbit_color_map,
        mass_suffix=mass_suffix,
        mass_divisor=mass_divisor,
        filter_out_suborbital=filter_out_suborbital
    )

def total_mass_vs_mass_by_filter(chart_title_prefix, output_prefix, chart_title_suffix, output_suffix, filter_function, filter_function_parameters_list, filter_function_additional_parameter=None, mass_step_size_kg=1000, launch_vehicle_simplified_name=None, launch_vehicle_family=None, color_map=None, mass_suffix='t', mass_divisor=1000, filter_out_suborbital=True):
    """
    Generate a chart showing the distribution of total launched mass versus payload mass range by a given filter function (e.g., launch vehicle, launch category, etc.).
    """
    output_name = f"{output_prefix}_total_mass_vs_mass_by_{output_suffix}"

    # Initialize dataset
    dataset = mda.McdowellDataset("./datasets")

    # Filter the base dataset
    if filter_out_suborbital:
        mda.Filters.filter_by_launch_category(dataset.launch, ['O', 'D'])  # Filter for orbital and deep space launches
    if launch_vehicle_family is not None:
        mda.Filters.filter_by_launch_vehicle_family(dataset.launch, launch_vehicle_family)
    else:
        mda.Filters.filter_by_launch_vehicle_name_simplified(dataset.launch, launch_vehicle_simplified_name)

    mda.ChartUtils.log_and_save_df("dataframe", output_name, output_prefix, dataset.launch.df)

    max_mass = int(dataset.launch.df['Payload_Mass'].max())

    bins = list(range(0, max_mass + mass_step_size_kg, mass_step_size_kg))
    mass_labels = [f"{int(bins[i]/mass_divisor)}-{int(bins[i+1]/mass_divisor)}{mass_suffix}" for i in range(len(bins)-1)]

    dataframes = mda.ChartUtils.bin_dataset_into_dictionary_by_filter_function(
        dataset=dataset.launch,
        filter_function=filter_function,
        filter_function_parameters_list=filter_function_parameters_list,
        value_col='Payload_Mass',
        bins=bins,
        bin_labels=mass_labels,
        count_values=False,
        bin_column='Mass_Range',
        filter_function_additional_parameter=filter_function_additional_parameter
    )
    
    # remove dataframes with no data or all zeroes, so that launch pad filtering doesn't include literally all pads ever
    if filter_function == mda.Filters.filter_by_launch_pad_raw:
        def numeric_sum(df):
            numeric_cols = df.select_dtypes(include='number').columns
            return df[numeric_cols].sum().sum() if not df.empty and len(numeric_cols) > 0 else 0
        dataframes = {key: df for key, df in dataframes.items() if not df.empty and numeric_sum(df) > 0}
    
    total_masses = {}
    for key in dataframes.keys():
        total_mass = dataframes[key].groupby('Mass_Range', observed=False)['Payload_Mass'].sum()
        total_mass = total_mass.reindex(mass_labels, fill_value=0)
        total_masses[key] = total_mass / mass_divisor

    output_df = mda.ChartUtils.combine_dictionary_of_dataframes(total_masses)

    # Save to CSV
    mda.ChartUtils.log_and_save_df("csv", output_name, output_prefix, output_df)

    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Net Payload Mass vs Mass Range by {chart_title_suffix}',
        subtitle=f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label=f'Payload Mass Range ({mass_suffix})',
        y_label=f'Total Payload Mass ({mass_suffix})',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        color_map=color_map,
        bargap=0.1
    )
    
def total_mass_vs_mass_by_orbit(mass_step_size_kg, chart_title_prefix, output_prefix, launch_vehicle_simplified_name=None, launch_vehicle_family=None, mass_suffix='t', mass_divisor=1000, filter_out_suborbital=True):
    # Wrapper
    total_mass_vs_mass_by_filter(
        chart_title_prefix=chart_title_prefix,
        output_prefix=output_prefix,
        chart_title_suffix='Orbit',
        output_suffix='orbit',
        filter_function=mda.Filters.filter_by_orbit,
        filter_function_parameters_list=['LEO', 'SSO', 'MEO', 'GTO', 'GEO', 'HEO', 'BEO'],
        filter_function_additional_parameter=None,
        mass_step_size_kg=mass_step_size_kg,
        launch_vehicle_simplified_name=launch_vehicle_simplified_name,
        launch_vehicle_family=launch_vehicle_family,
        color_map=mda.ChartUtils.orbit_color_map,
        mass_suffix=mass_suffix,
        mass_divisor=mass_divisor,
        filter_out_suborbital=filter_out_suborbital
    )

def launches_vs_mass_by_general_launch_payload_type(mass_step_size_kg, chart_title_prefix, output_prefix, launch_vehicle_simplified_name=None, launch_vehicle_family=None, mass_suffix='t', mass_divisor=1000, filter_out_suborbital=True):
    """Generate a chart showing the number of launches by payload mass range by general launch payload type.
    Eg. How many launches were 2-3 tonnes and Starlink, how many 6-7 tonnes and Commercial, etc.

    Args:
        mass_step_size_kg (int): Step size in kg for the mass bins (eg. 1000 gives bins of 0-1000 kg, 1000-2000 kg, etc.)
        chart_title_prefix (str): Prefix for the chart title (should be the prettified name of the launch vehicle) (eg. 'Falcon 9') 
        output_prefix (str): Simplified name of LV for output files (eg. 'f9' for Falcon 9 gives "f9_launches_vs_mass_by_general_launch_payload_type")
        launch_vehicle_simplified_name (str, optional): Launch vehicle to filter by
        launch_vehicle_family (str, optional): Family of launch vehicle to filter by. If not none, then filtering will be done by family instead of the launch_vehicle field.
        mass_suffix (str, optional): Suffix for the mass labels (default is 't' for tonnes, use 'kg' if you want). Defaults to 't'.
        mass_divisor (int, optional): Divisor for the mass values in the chart (default is 1000 to convert kg to tonnes). Defaults to 1000.
    """
    
    output_name = f"{output_prefix}_launches_vs_mass_by_general_launch_payload_type"

    # Initialize dataset
    dataset = mda.McdowellDataset("./datasets")

    # Filter for orbital and deep space launches
    if filter_out_suborbital:
        mda.Filters.filter_by_launch_category(dataset.launch, ['O', 'D'])
    if launch_vehicle_family is not None:
        mda.Filters.filter_by_launch_vehicle_family(dataset.launch, launch_vehicle_family)
    else:
        mda.Filters.filter_by_launch_vehicle_name_simplified(dataset.launch, launch_vehicle_simplified_name)

    mda.ChartUtils.log_and_save_df("dataframe", output_name, output_prefix, dataset.launch.df)
    
    max_mass = int(dataset.launch.df['Payload_Mass'].max())

    # Define payload types and bins
    general_launch_payload_types = ['Starlink', 'Commercial', 'Chinese Commercial', 'Government', 'Eastern Government', 'Military', 'Eastern Military']
    bins = list(range(0, max_mass+mass_step_size_kg, mass_step_size_kg))
    mass_labels = [f"{int(bins[i]/mass_divisor)}-{int(bins[i+1]/mass_divisor)}{mass_suffix}" for i in range(len(bins)-1)]

    # Create a dictionary with key payload types and values are dataframes for each payload type showing the number of launches per payload mass range
    payload_type_dataframes = mda.ChartUtils.bin_dataset_into_dictionary_by_filter_function(
        dataset=dataset.launch,
        filter_function=mda.Filters.filter_column_by_exact,
        filter_function_parameters_list=general_launch_payload_types,
        value_col='Payload_Mass',
        bins=bins,
        bin_labels=mass_labels,
        filter_function_additional_parameter="General_Launch_Payload_Type"
    )

    # Create dictionary with columns that are the payload types and values are the mass ranges
    output_df = mda.ChartUtils.combine_dictionary_of_dataframes(payload_type_dataframes)

    # Save to CSV
    mda.ChartUtils.log_and_save_df("csv", output_name, output_prefix, output_df)

    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Launches vs. Payload Mass by Payload Type',
        subtitle=f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label=f'Payload Mass Range ({mass_suffix})',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        color_map=mda.ChartUtils.general_launch_payload_type_color_map,
        bargap=0.1,
    )

def total_mass_vs_mass_by_general_launch_payload_type(mass_step_size_kg, chart_title_prefix, output_prefix, launch_vehicle_simplified_name=None, launch_vehicle_family=None, mass_suffix='t', mass_divisor=1000, filter_out_suborbital=True):
    """Generate a chart showing the distribution of total launched mass versus payload mass range by general launch payload type.
    Eg. How much total mass was launched in 2-3 tonnes range for Starlink, how much for Commercial, etc.

    Args:
        mass_step_size_kg (int): Step size in kg for the mass bins (eg. 1000 gives bins of 0-1000 kg, 1000-2000 kg, etc.)
        chart_title_prefix (str): Prefix for the chart title (should be the prettified name of the launch vehicle) (eg. 'Falcon 9') 
        output_prefix (str): Simplified name of LV for output files (eg. 'f9' for Falcon 9 gives "f9_total_mass_vs_mass_by_general_launch_payload_type")
        launch_vehicle_simplified_name (str, optional): Launch vehicle to filter by
        launch_vehicle_family (str, optional): Family of launch vehicle to filter by. If not none, then filtering will be done by family instead of the launch_vehicle field.
        mass_suffix (str, optional): Suffix for the mass labels (default is 't' for tonnes, use 'kg' if you want). Defaults to 't'.
        mass_divisor (int, optional): Divisor for the mass values in the chart (default is 1000 to convert kg to tonnes). Defaults to 1000.
    """
    
    output_name = f"{output_prefix}_total_mass_vs_mass_by_general_launch_payload_type"

    # Initialize dataset
    dataset = mda.McdowellDataset("./datasets")

    # Filter for orbital and deep space launches
    if filter_out_suborbital:
        mda.Filters.filter_by_launch_category(dataset.launch, ['O', 'D'])
    if launch_vehicle_family is not None:
        mda.Filters.filter_by_launch_vehicle_family(dataset.launch, launch_vehicle_family)
    else:
        mda.Filters.filter_by_launch_vehicle_name_simplified(dataset.launch, launch_vehicle_simplified_name)

    mda.ChartUtils.log_and_save_df("dataframe", output_name, output_prefix, dataset.launch.df)
    
    max_mass = int(dataset.launch.df['Payload_Mass'].max())

    # Define payload types and bins
    general_launch_payload_types = ['Starlink', 'Commercial', 'Chinese Commercial', 'Government', 'Eastern Government', 'Military', 'Eastern Military']
    bins = list(range(0, max_mass+mass_step_size_kg, mass_step_size_kg))
    mass_labels = [f"{int(bins[i]/mass_divisor)}-{int(bins[i+1]/mass_divisor)}{mass_suffix}" for i in range(len(bins)-1)]

    # Create a dictionary with key payload types and values are dataframes for each payload type showing the total mass per payload mass range
    payload_type_dataframes = mda.ChartUtils.bin_dataset_into_dictionary_by_filter_function(
        dataset=dataset.launch,
        filter_function=mda.Filters.filter_column_by_exact,
        filter_function_parameters_list=general_launch_payload_types,
        value_col='Payload_Mass',
        bins=bins,
        bin_labels=mass_labels,
        filter_function_additional_parameter="General_Launch_Payload_Type",
        count_values=False,
        bin_column='Mass_Range'
    )

    payload_type_masses = {}
    for payload_type_key in payload_type_dataframes.keys():
        total_mass = payload_type_dataframes[payload_type_key].groupby('Mass_Range', observed=False)['Payload_Mass'].sum()
        total_mass = total_mass.reindex(mass_labels, fill_value=0)
        payload_type_masses[payload_type_key] = total_mass/mass_divisor

    output_df = mda.ChartUtils.combine_dictionary_of_dataframes(payload_type_masses)

    # Save to CSV
    mda.ChartUtils.log_and_save_df("csv", output_name, output_prefix, output_df)

    # Plot stacked bar chart
    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Net Payload Mass vs Mass Range by Payload Type',
        subtitle=f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label=f'Payload Mass Range ({mass_suffix})',
        y_label=f'Total Payload Mass ({mass_suffix})',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        color_map=mda.ChartUtils.general_launch_payload_type_color_map,
        bargap=0.1
    )

def launches_vs_month_by_orbit(chart_title_prefix, output_prefix, launch_vehicle_simplified_name=None, launch_vehicle_family=None, all_vehicles=False, x_tick_step_size=12, start_year=None, end_year=None, filter_out_suborbital=True):
    """Generate a chart showing the number of launches by month by orbit.

    Args:
        chart_title_prefix (str): Prefix for the chart title (should be the prettified name of the launch vehicle) (eg. 'Falcon 9') 
        output_prefix (str): Simplified name of LV for output files (eg. 'f9' for Falcon 9 gives "f9_launches_vs_month_by_orbit")
        launch_vehicle_simplified_name (str, optional): Launch vehicle to filter by
        launch_vehicle_family (str, optional): Family of launch vehicle to filter by. If not none, then filtering will be done by family instead of the launch_vehicle field.
        all_vehicles (bool, optional): If True, will not filter by launch vehicle. Defaults to False.
        x_tick_step_size (int, optional): Step size for x-axis ticks in months. Defaults to 12 (one year).
        start_year (int, optional): Start year for the data. By default it is the first year of the specified vehicle in the dataset.
        end_year (int, optional): End year for the data (inclusive). By default, the final year of the specified vehicle is used.
    """
    
    # Initialize dataset
    dataset = mda.McdowellDataset("./datasets")

    # Filter the base dataset
    if filter_out_suborbital:
        mda.Filters.filter_by_launch_category(dataset.launch, ['O', 'D'])
    if not all_vehicles:
        if launch_vehicle_family is not None:
            mda.Filters.filter_by_launch_vehicle_family(dataset.launch, launch_vehicle_family)
        else:
            mda.Filters.filter_by_launch_vehicle_name_simplified(dataset.launch, launch_vehicle_simplified_name)

    if start_year == None:
        start_year = dataset.launch.df['Launch_Date'].dt.year.min()
    if end_year == None:
        end_year = dataset.launch.df['Launch_Date'].dt.year.max()

    date_end = "present" if end_year == datetime.now().year else  f"{end_year}"
    output_name = f"{output_prefix}_launches_vs_month_by_orbit_{start_year}_{date_end}"

    # After getting the start and end years, filter the dataset by launch date
    mda.Filters.filter_by_launch_date(dataset.launch, start_date=f'{start_year}-01-01', end_date=f'{end_year}-12-31')
    
    # Encode launch month as year*12 + months to get total months since Jesus instead of years since Jesus
    dataset.launch.df['Launch_Month'] = dataset.launch.df['Launch_Date'].dt.year*12 + dataset.launch.df['Launch_Date'].dt.month
    
    mda.ChartUtils.log_and_save_df("dataframe", output_name, output_prefix, dataset.launch.df)
    
    orbits = ['LEO', 'SSO', 'MEO', 'GTO', 'GEO', 'HEO', 'BEO']
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    bin_labels = []
    for year in range(start_year, end_year+1, 1):
        for month in months:
            bin_labels.append(f"{month} {year}")

    # Create a dictionary with key orbits and values are dataframes for each orbit showing the number of launches per year
    orbit_dataframes = mda.ChartUtils.bin_dataset_into_dictionary_by_filter_function(
        dataset=dataset.launch,
        filter_function=mda.Filters.filter_by_orbit,
        filter_function_parameters_list=orbits,
        value_col='Launch_Month',
        bins=list(range(start_year*12, (end_year+1)*12+1)), # +1 year bc its exclusive, again +1 to align bins to months for some reason ugh pandas wtf investigate this future Chris
        bin_labels=bin_labels,
    )

    # Combine dictionary of dataframes into a single dataframe (by column)
    output_df = mda.ChartUtils.combine_dictionary_of_dataframes(orbit_dataframes)
    
    # Save to CSV
    mda.ChartUtils.log_and_save_df("csv", output_name, output_prefix, output_df)

    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Launches vs. Month by Orbit',
        subtitle=f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label='Date',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        color_map=mda.ChartUtils.orbit_color_map,
        bargap=0.0,
        x_tick0=0,
        x_tick_step_size=x_tick_step_size
    )
    
def launches_vs_month_by_general_launch_payload_type(chart_title_prefix, output_prefix, launch_vehicle_simplified_name=None, launch_vehicle_family=None, all_vehicles=False, x_tick_step_size=12, start_year=None, end_year=None, filter_out_suborbital=True):
    """Generate a chart showing the number of launches by month by general launch payload type.

    Args:
        chart_title_prefix (str): Prefix for the chart title (should be the prettified name of the launch vehicle) (eg. 'Falcon 9') 
        output_prefix (str): Simplified name of LV for output files (eg. 'f9' for Falcon 9 gives "f9_launches_vs_month_by_general_launch_payload_type")
        launch_vehicle_simplified_name (str, optional): Launch vehicle to filter by
        launch_vehicle_family (str, optional): Family of launch vehicle to filter by. If not none, then filtering will be done by family instead of the launch_vehicle field.
        all_vehicles (bool, optional): If True, will not filter by launch vehicle. Defaults to False.
        x_tick_step_size (int, optional): Step size for x-axis ticks in months. Defaults to 12 (one year).
        start_year (int, optional): Start year for the data. By default it is the first year of the specified vehicle in the dataset.
        end_year (int, optional): End year for the data (inclusive). By default, the final year of the specified vehicle is used.
    """
    
    # Initialize dataset
    dataset = mda.McdowellDataset("./datasets")

    # Filter the base dataset
    if filter_out_suborbital:
        mda.Filters.filter_by_launch_category(dataset.launch, ['O', 'D'])
    if not all_vehicles:
        if launch_vehicle_family is not None:
            mda.Filters.filter_by_launch_vehicle_family(dataset.launch, launch_vehicle_family)
        else:
            mda.Filters.filter_by_launch_vehicle_name_simplified(dataset.launch, launch_vehicle_simplified_name)

    if start_year == None:
        start_year = dataset.launch.df['Launch_Date'].dt.year.min()
    if end_year == None:
        end_year = dataset.launch.df['Launch_Date'].dt.year.max()

    date_end = "present" if end_year == datetime.now().year else  f"{end_year}"
    output_name = f"{output_prefix}_launches_vs_month_by_general_launch_payload_type_{start_year}_{date_end}"

    # After getting the start and end years, filter the dataset by launch date
    mda.Filters.filter_by_launch_date(dataset.launch, start_date=f'{start_year}-01-01', end_date=f'{end_year}-12-31')
    
    # Encode launch month as year*12 + months to get total months since Jesus instead of years since Jesus
    dataset.launch.df['Launch_Month'] = dataset.launch.df['Launch_Date'].dt.year*12 + dataset.launch.df['Launch_Date'].dt.month
    
    mda.ChartUtils.log_and_save_df("dataframe", output_name, output_prefix, dataset.launch.df)
    
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
    
    # Save to CSV
    mda.ChartUtils.log_and_save_df("csv", output_name, output_prefix, output_df)
    
    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Launches vs. Month by Payload Type',
        subtitle=f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label='Date',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        color_map=mda.ChartUtils.general_launch_payload_type_color_map,
        bargap=0.0,
        x_tick0=0,
        x_tick_step_size=x_tick_step_size
    )
    
def launches_vs_month_by_filter(chart_title_prefix, output_prefix, chart_title_suffix, output_suffix, filter_function, filter_function_parameters_list, filter_function_additional_parameter=None, launch_vehicle_simplified_name=None, launch_vehicle_family=None, all_vehicles=False, x_tick_step_size=12, color_map=None, start_year=None, end_year=None, filter_out_suborbital=True):
    """Generate a chart showing the number of launches by month by a specified filter function.

    Args:
        chart_title_prefix (str): Prefix for the chart title (should be the prettified name of the launch vehicle) (eg. 'Falcon 9') 
        output_prefix (str): Simplified name of LV for output files (eg. 'f9' for Falcon 9 gives "f9_launches_vs_month_by_filter")
        chart_title_suffix (str): Suffix for the chart title (eg. 'Orbit')
        output_suffix (str): Suffix for the output file names (eg. 'orbit')
        filter_function (function): Function to filter the dataset by (eg. mda.Filters.filter_by_orbit)
        filter_function_parameters_list (list): List of parameters to pass to the filter function
        filter_function_additional_parameter (str, optional): Additional parameter to pass to the filter function if needed
        launch_vehicle_simplified_name (str, optional): Launch vehicle to filter by
        launch_vehicle_family (str, optional): Family of launch vehicle to filter by. If not none, then filtering will be done by family instead of the launch_vehicle field.
        all_vehicles (bool, optional): If True, will not filter by launch vehicle. Defaults to False.
        x_tick_step_size (int, optional): Step size for x-axis ticks in months. Defaults to 12 (one year).
        start_year (int, optional): Start year for the data. By default it is the first year of the specified vehicle in the dataset.
        end_year (int, optional): End year for the data (inclusive). By default, the final year of the specified vehicle is used.
    """
    
    # Initialize dataset
    dataset = mda.McdowellDataset("./datasets")

    # Filter the base dataset
    if filter_out_suborbital:
        mda.Filters.filter_by_launch_category(dataset.launch, ['O', 'D'])
    if not all_vehicles:
        if launch_vehicle_family is not None:
            mda.Filters.filter_by_launch_vehicle_family(dataset.launch, launch_vehicle_family)
        else:
            mda.Filters.filter_by_launch_vehicle_name_simplified(dataset.launch, launch_vehicle_simplified_name)

    if start_year == None:
        start_year = dataset.launch.df['Launch_Date'].dt.year.min()
    if end_year == None:
        end_year = dataset.launch.df['Launch_Date'].dt.year.max()

    date_end = "present" if end_year == datetime.now().year else  f"{end_year}"
    output_name = f"{output_prefix}_launches_vs_month_by_{output_suffix}_{start_year}_{date_end}"

    # After getting the start and end years, filter the dataset by launch date
    mda.Filters.filter_by_launch_date(dataset.launch, start_date=f'{start_year}-01-01', end_date=f'{end_year}-12-31')
    
    # Encode launch month as year*12 + months to get total months since Jesus instead of years since Jesus
    dataset.launch.df['Launch_Month'] = dataset.launch.df['Launch_Date'].dt.year*12 + dataset.launch.df['Launch_Date'].dt.month
    
    mda.ChartUtils.log_and_save_df("dataframe", output_name, output_prefix, dataset.launch.df)
    
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    bin_labels = []
    for year in range(start_year, end_year+1, 1):
        for month in months:
            bin_labels.append(f"{month} {year}")

    # Create a dictionary with key filters and values are dataframes for each filter showing the number of launches per month
    dataframes = mda.ChartUtils.bin_dataset_into_dictionary_by_filter_function(
        dataset=dataset.launch,
        filter_function=filter_function,
        filter_function_parameters_list=filter_function_parameters_list,
        value_col='Launch_Month',
        bins=list(range(start_year*12, (end_year+1)*12+1)),
        bin_labels=bin_labels,
        filter_function_additional_parameter=filter_function_additional_parameter,
    )


    # remove dataframes with no data or all zeroes, so that launch pad filtering doesn't include literally all pads ever
    if filter_function == mda.Filters.filter_by_launch_pad_raw:
        dataframes = {key: df for key, df in dataframes.items() if not df.empty and df.sum().sum() > 0}

    # Combine dictionary of dataframes into a single dataframe (by column)
    output_df = mda.ChartUtils.combine_dictionary_of_dataframes(dataframes)
    
    # Save to CSV
    mda.ChartUtils.log_and_save_df("csv", output_name, output_prefix, output_df)

    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Launches vs. Month by {chart_title_suffix}',
        subtitle=f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label='Date',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        color_map=color_map,
        bargap=0.0,
        x_tick0=0,
        x_tick_step_size=x_tick_step_size
    )
    
def launches_vs_year_by_orbit(chart_title_prefix, output_prefix, launch_vehicle_simplified_name=None, launch_vehicle_family=None, all_vehicles=False, x_tick_step_size=1, start_year=None, end_year=None, filter_out_suborbital=True):
    """Generate a chart showing the number of launches by year by orbit.

    Args:
        chart_title_prefix (str): Prefix for the chart title (should be the prettified name of the launch vehicle) (eg. 'Falcon 9') 
        output_prefix (str): Simplified name of LV for output files (eg. 'f9' for Falcon 9 gives "f9_launches_vs_year_by_orbit")
        launch_vehicle_simplified_name (str, optional): Launch vehicle to filter by
        launch_vehicle_family (str, optional): Family of launch vehicle to filter by. If not none, then filtering will be done by family instead of the launch_vehicle field.
        all_vehicles (bool, optional): If True, will not filter by launch vehicle. Defaults to False.
        x_tick_step_size (int, optional): Step size for x-axis ticks in years. Defaults to 1 (one year).
        start_year (int, optional): Start year for the data. By default it is the first year of the specified vehicle in the dataset.
        end_year (int, optional): End year for the data (inclusive). By default, the final year of the specified vehicle is used.
    """
    
    # Initialize dataset
    dataset = mda.McdowellDataset("./datasets")

    # Filter the base dataset
    if filter_out_suborbital:
        mda.Filters.filter_by_launch_category(dataset.launch, ['O', 'D'])
    if not all_vehicles:
        if launch_vehicle_family is not None:
            mda.Filters.filter_by_launch_vehicle_family(dataset.launch, launch_vehicle_family)
        else:
            mda.Filters.filter_by_launch_vehicle_name_simplified(dataset.launch, launch_vehicle_simplified_name)

    if start_year == None:
        start_year = dataset.launch.df['Launch_Date'].dt.year.min()
    if end_year == None:
        end_year = dataset.launch.df['Launch_Date'].dt.year.max()

    date_end = "present" if end_year == datetime.now().year else  f"{end_year}"
    output_name = f"{output_prefix}_launches_vs_year_by_orbit_{start_year}_{date_end}"

    # After getting the start and end years, filter the dataset by launch date
    mda.Filters.filter_by_launch_date(dataset.launch, start_date=f'{start_year}-01-01', end_date=f'{end_year}-12-31')
    
    # Encode launch month as year*12 + months to get total months since Jesus instead of years since Jesus
    dataset.launch.df['Launch_Year'] = dataset.launch.df['Launch_Date'].dt.year
    
    mda.ChartUtils.log_and_save_df("dataframe", output_name, output_prefix, dataset.launch.df)
    
    orbits = ['LEO', 'SSO', 'MEO', 'GTO', 'GEO', 'HEO', 'BEO']

    # Create a dictionary with key orbits and values are dataframes for each orbit showing the number of launches per year
    orbit_dataframes = mda.ChartUtils.bin_dataset_into_dictionary_by_filter_function(
        dataset=dataset.launch,
        filter_function=mda.Filters.filter_by_orbit,
        filter_function_parameters_list=orbits,
        value_col='Launch_Year',
        bins=list(range(start_year-1, end_year+1)), # +1 year bc its exclusive
        bin_labels=list(range(start_year, end_year+1)),
        count_values=True
    )
    
    # Combine dictionary of dataframes into a single dataframe (by column)
    output_df = mda.ChartUtils.combine_dictionary_of_dataframes(orbit_dataframes)
    
    # Save to CSV
    mda.ChartUtils.log_and_save_df("csv", output_name, output_prefix, output_df)
    
    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Launches vs. Year by Orbit',
        subtitle=f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label='Year',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        color_map=mda.ChartUtils.orbit_color_map,
        bargap=0.1,
        x_tick_step_size=x_tick_step_size
    )

def launches_vs_year_by_general_launch_payload_type(chart_title_prefix, output_prefix, launch_vehicle_simplified_name=None, launch_vehicle_family=None, all_vehicles=False, x_tick_step_size=1, start_year=None, end_year=None, filter_out_suborbital=True):
    """Generate a chart showing the number of launches by year by general launch payload type.

    Args:
        chart_title_prefix (str): Prefix for the chart title (should be the prettified name of the launch vehicle) (eg. 'Falcon 9') 
        output_prefix (str): Simplified name of LV for output files (eg. 'f9' for Falcon 9 gives "f9_launches_vs_year_by_general_launch_payload_type")
        launch_vehicle_simplified_name (str, optional): Launch vehicle to filter by
        launch_vehicle_family (str, optional): Family of launch vehicle to filter by. If not none, then filtering will be done by family instead of the launch_vehicle field.
        all_vehicles (bool, optional): If True, will not filter by launch vehicle. Defaults to False.
        x_tick_step_size (int, optional): Step size for x-axis ticks in years. Defaults to 1 (one year).
        start_year (int, optional): Start year for the data. By default it is the first year of the specified vehicle in the dataset.
        end_year (int, optional): End year for the data (inclusive). By default, the final year of the specified vehicle is used.
    """
    
    # Initialize dataset
    dataset = mda.McdowellDataset("./datasets")

    # Filter the base dataset
    if filter_out_suborbital:
        mda.Filters.filter_by_launch_category(dataset.launch, ['O', 'D'])
    if not all_vehicles:
        if launch_vehicle_family is not None:
            mda.Filters.filter_by_launch_vehicle_family(dataset.launch, launch_vehicle_family)
        else:
            mda.Filters.filter_by_launch_vehicle_name_simplified(dataset.launch, launch_vehicle_simplified_name)

    if start_year == None:
        start_year = dataset.launch.df['Launch_Date'].dt.year.min()
    if end_year == None:
        end_year = dataset.launch.df['Launch_Date'].dt.year.max()

    date_end = "present" if end_year == datetime.now().year else  f"{end_year}"
    output_name = f"{output_prefix}_launches_vs_year_by_general_launch_payload_type_{start_year}_{date_end}"

    # After getting the start and end years, filter the dataset by launch date
    mda.Filters.filter_by_launch_date(dataset.launch, start_date=f'{start_year}-01-01', end_date=f'{end_year}-12-31')
    
    # Encode launch month as year*12 + months to get total months since Jesus instead of years since Jesus
    dataset.launch.df['Launch_Year'] = dataset.launch.df['Launch_Date'].dt.year
    
    mda.ChartUtils.log_and_save_df("dataframe", output_name, output_prefix, dataset.launch.df)
    
    general_launch_payload_Types = ['Starlink', 'Commercial', 'Chinese Commercial', 'Government', 'Eastern Government', 'Military', 'Eastern Military']

    # Create a dictionary with key orbits and values are dataframes for each orbit showing the number of launches per year
    orbit_dataframes = mda.ChartUtils.bin_dataset_into_dictionary_by_filter_function(
        dataset=dataset.launch,
        filter_function=mda.Filters.filter_column_by_exact,
        filter_function_parameters_list=general_launch_payload_Types,
        value_col='Launch_Year',
        bins=list(range(start_year-1, end_year+1)), # +1 year bc its exclusive
        bin_labels=list(range(start_year, end_year+1)),
        filter_function_additional_parameter="General_Launch_Payload_Type",
        count_values=True
    )
    
    # Combine dictionary of dataframes into a single dataframe (by column)
    output_df = mda.ChartUtils.combine_dictionary_of_dataframes(orbit_dataframes)
    
    # Save to CSV
    mda.ChartUtils.log_and_save_df("csv", output_name, output_prefix, output_df)
    
    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Launches vs. Year by Payload Type',
        subtitle=f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label='Year',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        color_map=mda.ChartUtils.general_launch_payload_type_color_map,
        bargap=0.1,
        x_tick_step_size=x_tick_step_size
    )

def launches_vs_year_by_filter(chart_title_prefix, output_prefix, chart_title_suffix, output_suffix, filter_function, filter_function_parameters_list, filter_function_additional_parameter=None, launch_vehicle_simplified_name=None, launch_vehicle_family=None, all_vehicles=False, x_tick_step_size=1, color_map=None, start_year=None, end_year=None, filter_out_suborbital=True):
    """Generate a chart showing the number of launches by year by a specified filter function.

    Args:
        chart_title_prefix (str): Prefix for the chart title (should be the prettified name of the launch vehicle) (eg. 'Falcon 9') 
        output_prefix (str): Simplified name of LV for output files (eg. 'f9' for Falcon 9 gives "f9_launches_vs_year_by_filter")
        filter_function (function): Function to filter the dataset by. Should take a dataset and a list of parameters.
        filter_function_parameters_list (list): List of parameters to pass to the filter function.
        launch_vehicle_simplified_name (str, optional): Launch vehicle to filter by
        launch_vehicle_family (str, optional): Family of launch vehicle to filter by. If not none, then filtering will be done by family instead of the launch_vehicle field.
        all_vehicles (bool, optional): If True, will not filter by launch vehicle. Defaults to False.
        x_tick_step_size (int, optional): Step size for x-axis ticks in years. Defaults to 1 (one year).
        start_year (int, optional): Start year for the data. By default it is the first year of the specified vehicle in the dataset.
        end_year (int, optional): End year for the data (inclusive). By default, the final year of the specified vehicle is used.
        filter_out_suborbital (bool, optional): If True, will filter out suborbital launches. Defaults to True.
    """
    
    # Initialize dataset
    dataset = mda.McdowellDataset("./datasets")

    # Filter the base dataset
    if filter_out_suborbital:
        mda.Filters.filter_by_launch_category(dataset.launch, ['O', 'D'])
    if all_vehicles == False:
        if launch_vehicle_family is not None:
            mda.Filters.filter_by_launch_vehicle_family(dataset.launch, launch_vehicle_family)
        else:
            mda.Filters.filter_by_launch_vehicle_name_simplified(dataset.launch, launch_vehicle_simplified_name)

    if start_year is None:
        start_year = dataset.launch.df['Launch_Date'].dt.year.min()
    if end_year is None:
        end_year = dataset.launch.df['Launch_Date'].dt.year.max()

    date_end = "present" if end_year == datetime.now().year else  f"{end_year}"
    output_name = f"{output_prefix}_launches_vs_year_by_{output_suffix}_{start_year}_{date_end}"

    # After getting the start and end years, filter the dataset by launch date
    mda.Filters.filter_by_launch_date(dataset.launch, start_date=f'{start_year}-01-01', end_date=f'{end_year}-12-31')

    dataset.launch.df['Launch_Year'] = dataset.launch.df['Launch_Date'].dt.year

    mda.ChartUtils.log_and_save_df("dataframe", output_name, output_prefix, dataset.launch.df)

    dataframes = mda.ChartUtils.bin_dataset_into_dictionary_by_filter_function(
        dataset=dataset.launch,
        filter_function=filter_function,
        filter_function_parameters_list=filter_function_parameters_list,
        value_col='Launch_Year',
        bins=list(range(start_year-1, end_year+1)),
        bin_labels=list(range(start_year, end_year+1)),
        count_values=True,
        filter_function_additional_parameter=filter_function_additional_parameter
    )

    # remove dataframes with no data or all zeroes, so that launch pad filtering doesn't include literally all pads ever
    if filter_function == mda.Filters.filter_by_launch_pad_raw:
        dataframes = {key: df for key, df in dataframes.items() if not df.empty and df.sum().sum() > 0}

    output_df = mda.ChartUtils.combine_dictionary_of_dataframes(dataframes)

    # Save to CSV
    mda.ChartUtils.log_and_save_df("csv", output_name, output_prefix, output_df)

    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Launches vs. Year by {chart_title_suffix}',
        subtitle=f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label='Year',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        bargap=0.1,
        color_map=color_map,
        x_tick_step_size=x_tick_step_size,
    )

def owner_payloads_vs_year_by_program(chart_title_prefix, output_prefix, owners_list, color_map=None, programing_simplification_dict=None, program_order=None):
    """Generate a chart showing the number of payloads by year by program for specified owners.

    Args:
        chart_title_prefix (str): Prefix for the chart title (should be the prettified name of the owner) (eg. 'SpaceX') 
        output_prefix (str): Simplified name of owner for output files (eg. 'spacex' for SpaceX gives "spacex_owner_payloads_vs_year_by_program")
        owners (list): List of owners to filter by
        programing_simplification_dict (dict, optional): Dictionary to simplify program names. ("New name": ["Old names", "another old name"]). MultiplDefaults to None.
        color_map (dict, optional): Color map for the programs. Dict or List. Defaults to None.
    """
    
    # Initialize dataset
    dataset = mda.McdowellDataset("./datasets")

    # Filter the base dataset for set owners
    mda.Filters.filter_column_by_exact(dataset.satcat, owners_list, "Owner")

    output_name = f"{output_prefix}_payloads_vs_year_by_program"

    programs = dataset.satcat.df['Payload_Program'].dropna().unique()

    dataset.satcat.df['Launch_Year'] = dataset.satcat.df['Launch_Date'].dt.year

    mda.ChartUtils.log_and_save_df("dataframe", output_name, output_prefix, dataset.satcat.df)
    
    # Create a dictionary with key programs and values are dataframes for each program showing the number of payloads per year
    dataframes = mda.ChartUtils.group_dataset_into_dictionary_by_filter_function(
        dataset.satcat,
        filter_function=mda.Filters.filter_column_by_exact,
        groups=programs,
        groupby_col="Launch_Year",
        count_values=True,
        filter_function_additional_parameter="Payload_Program"
    )
    
    # Combine dictionary of dataframes into a single dataframe (by column)
    output_df = mda.ChartUtils.combine_dictionary_of_dataframes(dataframes)

    # Add columns together that are part of the same simplified program in the dict
    if programing_simplification_dict is not None:
        for new_program, old_programs in programing_simplification_dict.items():
            if new_program not in output_df.columns:
                output_df[new_program] = 0
            for old_program in old_programs:
                if old_program in output_df.columns:
                    output_df[new_program] += output_df[old_program]
                    output_df.drop(columns=[old_program], inplace=True)

    # Reorder columns if program_order is specified
    if program_order is not None:
        output_df = output_df[program_order]
        
    # Save to CSV
    mda.ChartUtils.log_and_save_df("csv", output_name, output_prefix, output_df)

    mda.ChartUtils.plot_bar(
        output_df,
        title=f"{chart_title_prefix} Payloads vs Year by Program",
        subtitle=f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label="Year",
        y_label="Number of Payloads",
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        bargap=0.0,
        color_map=color_map,
    )

def owner_payloads_vs_year_by_category(chart_title_prefix, output_prefix, owners_list, category, color_map=None):
    """Generate a chart showing the number of payloads by year by a specified category (eg. country, launch vehicle, etc.) for specified owners.

    Categories:
        - "Launch Country"
        - "Launch Vehicle"
        - "Orbit"

    Args:
        chart_title_prefix (str): Prefix for the chart title (should be the prettified name of the owner) (eg. 'SpaceX') 
        output_prefix (str): Simplified name of owner for output files (eg. 'spacex' for SpaceX gives "spacex_owner_payloads_vs_year_by_country")
        owners_list (list): List of owners to filter by
        category (str): Category to filter by. Eg. "Launch Country", "Launch Vehicle", or "Orbit".
        color_map (dict, optional): Color map for the countries. Dict or List. Defaults to None.
    """
    
    category_to_column = {
        "Launch Country": "Launch_Country",
        "Launch Vehicle": "Launch_Vehicle_Simplified",
        "Orbit": "Simple_Orbit",
    }
    
    category_filter_column = category_to_column[category]
    
    dataset = mda.McdowellDataset("./datasets")

    # Filter the base dataset for set owners
    mda.Filters.filter_column_by_exact(dataset.satcat, owners_list, "Owner")

    output_name = f"{output_prefix}_payloads_vs_year_by_{str.lower(category).strip().replace(" ", "_")}"

    countries = dataset.satcat.df[category_filter_column].dropna().unique()

    dataset.satcat.df['Launch_Year'] = dataset.satcat.df['Launch_Date'].dt.year

    mda.ChartUtils.log_and_save_df("dataframe", output_name, output_prefix, dataset.satcat.df)
    
    # Create a dictionary with key countries and values are dataframes for each country showing the number of payloads per year
    dataframes = mda.ChartUtils.group_dataset_into_dictionary_by_filter_function(
        dataset.satcat,
        filter_function=mda.Filters.filter_column_by_exact,
        groups=countries,
        groupby_col="Launch_Year",
        count_values=True,
        filter_function_additional_parameter=category_filter_column
    )
    
    # Combine dictionary of dataframes into a single dataframe (by column)
    output_df = mda.ChartUtils.combine_dictionary_of_dataframes(dataframes)

    # Save to CSV
    mda.ChartUtils.log_and_save_df("csv", output_name, output_prefix, output_df)

    mda.ChartUtils.plot_bar(
        output_df,
        title=f"{chart_title_prefix} Payloads vs Year by {category}",
        subtitle=f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label="Year",
        y_label="Number of Payloads",
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        bargap=0.0,
        color_map=color_map,
    )

def launch_value_vs_date_by_filter_scatter(chart_title_prefix, output_prefix, value_column, series_column, filter_function, filter_function_parameter, filter_function_additional_parameter=None, x_axis_title_suffix="", value_title=None, series_title=None, color_map=None, x_tick_step_size=None, start_year=None, end_year=None, y_scaling_factor=1, x_axis_type=None, filter_out_suborbital=True):
    """
    Plot launches per date with a specified value column (e.g., Apogee, Mass, etc.) and series column (e.g., Launch Pad, Launch Vehicle, etc.) by filtering the dataset with a filter function.

    The value_column is plotted on the y-axis, and the series_column is used to split the data into different series.

    Args:
        chart_title_prefix (str): Prefix for the chart title (e.g., 'Falcon 9').
        output_prefix (str): Prefix for output file names.
        value_column (str): Name of the column to plot on y-axis (e.g., 'Apogee', 'Payload_Mass').
        series_column (str): Name of the column to group series by (e.g., 'Simple_Orbit', 'Launch_Vehicle').
        filter_function (callable): Function to filter the dataset (e.g., mda.Filters.filter_by_launch_vehicle_name_simplified).
        filter_function_parameter (Any): Parameter to pass to the filter_function.
        filter_function_additional_parameter (Any, optional): Additional parameter for the filter_function if needed. Defaults to None.
        x_axis_title_suffix (str, optional): Suffix to append to the y-axis label (e.g., "(km)", "(tonnes)"). Defaults to "".
        value_title (str, optional): Display name for the value column. Defaults to formatted value_column name.
        series_title (str, optional): Display name for the series column. Defaults to formatted series_column name.
        color_map (dict or list, optional): Color mapping for series. Defaults to None.
        x_tick_step_size (int, optional): Step size for x-axis ticks in months. Defaults to None.
        start_year (int, optional): Start year for the data. Defaults to None (uses earliest year in dataset).
        end_year (int, optional): End year for the data. Defaults to None (uses latest year in dataset).
        y_scaling_factor (float, optional): Scaling factor for y-axis values (e.g., 0.001 to convert kg to tonnes). Defaults to 1.
        x_axis_type (str, optional): Type of x-axis ('date' for date formatting, None for linear). Defaults to None.
        filter_out_suborbital (bool, optional): If True, filters out suborbital launches. Defaults to True.
        
    Interesting note:
    Because we're using raw dates and not a launch date field or something, we can't set x tick step size and get anything that makes sense. It's not a continuous dx in the dataset since some launches are hours apart and some are months.
    """
    
    dataset = mda.McdowellDataset()
    
    if filter_out_suborbital:
        mda.Filters.filter_by_launch_category(dataset.launch, ['O', 'D'])
    if filter_function_additional_parameter is not None:
        filter_function(dataset.launch, filter_function_parameter, filter_function_additional_parameter)
    else:
        filter_function(dataset.launch, filter_function_parameter)
    
    if start_year == None:
        start_year = dataset.launch.df['Launch_Date'].dt.year.min()
    if end_year == None:
        end_year = dataset.launch.df['Launch_Date'].dt.year.max()
    
    date_end = "present" if end_year == datetime.now().year else  f"{end_year}"
    output_name = f"{output_prefix}_launches_{value_column.lower()}_vs_date_by_{series_column.lower()}_{start_year}_{date_end}"
    
    mda.Filters.filter_by_launch_date(dataset.launch, start_date=f'{start_year}-01-01', end_date=f'{end_year}-12-31') # After getting the start and end years, filter the dataset by launch date
    filtered_df = dataset.launch.df

    mda.ChartUtils.log_and_save_df("dataframe", output_name, output_prefix, filtered_df)
    
    filtered_df = filtered_df[['Launch_Date', value_column, series_column]].dropna(subset=[value_column])
    filtered_df = filtered_df[filtered_df[value_column] != 0] # Remove 0 values

    pivoted_df = mda.ChartUtils.pivot_dataframe(filtered_df, 'Launch_Date', series_column, value_column) # Pivot for plotting

    # Reorder in the order of the color map
    if color_map is not None and type(color_map) is dict:
        cols = list(color_map.keys())
        cols = [col for col in cols if col in pivoted_df.columns] # Remove keys that are not in the pivoted_df columns
        cols.insert(0, "Launch_Date")  # Ensure Launch_Date is always included as the first column
        pivoted_df = pivoted_df.reindex(columns=cols)
    
    # Save to CSV
    mda.ChartUtils.log_and_save_df("csv", output_name, output_prefix, pivoted_df)

    if value_title is None:
        value_title = value_column.replace("_", " ").title()
    if series_title is None:
        series_title = series_column.replace("_", " ").title()
        
    mda.ChartUtils.plot_scatter(
        pivoted_df,
        x_col='Launch_Date',
        y_cols=pivoted_df.columns[1:], # Skip date line? pls fix
        title=f'{chart_title_prefix} Launches {value_title} vs. Date by {series_title}',
        subtitle=f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label='Launch Date',
        y_label=f'{value_title} {x_axis_title_suffix}',
        dot_diameter=10,
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        color_map=color_map,
        y_scaling_factor=y_scaling_factor,
        x_tick_step_size=x_tick_step_size,
        x_axis_type=x_axis_type
    )
    
def launch_apogee_vs_inclination_by_filter_scatter(chart_title_prefix, output_prefix, series_column, filter_function, filter_function_parameter, filter_function_additional_parameter=None, series_title=None, color_map=None, start_year=None, end_year=None, filter_out_suborbital=True):
    """
    Plot launches per date with Apogee vs Inclination by filtering the dataset with a filter function.

    Args:
        chart_title_prefix (str): Prefix for the chart title (e.g., 'Falcon 9').
        output_prefix (str): Prefix for output file names.
        filter_function (callable): Function to filter the dataset. Should accept the dataset as its first argument.
        filter_function_parameters (Any): Parameters to pass to the filter_function.
        x_axis_title_suffix (str, optional): Suffix for the x-axis title. Defaults to "".
        y_scaling_factor (int, optional): Scaling factor for the y-axis values. Defaults to 1.
        start_year (int, optional): Start year for the data. Defaults to None (uses earliest year in dataset).
        end_year (int, optional): End year for the data. Defaults to None (uses latest year in dataset).
    """
    
    # Initialize dataset
    dataset = mda.McdowellDataset()

    if filter_out_suborbital:
        mda.Filters.filter_by_launch_category(dataset.launch, ['O', 'D'])
    if filter_function_additional_parameter is not None:
        filter_function(dataset.launch, filter_function_parameter, filter_function_additional_parameter)
    else:
        filter_function(dataset.launch, filter_function_parameter)
    
    if start_year == None:
        start_year = dataset.launch.df['Launch_Date'].dt.year.min()
    if end_year == None:
        end_year = dataset.launch.df['Launch_Date'].dt.year.max()
    
    date_end = "present" if end_year == datetime.now().year else  f"{end_year}"
    output_name = f"{output_prefix}_launches_apogee_vs_inc_by_{series_column.lower()}_{start_year}_{date_end}"
    
    mda.Filters.filter_by_launch_date(dataset.launch, start_date=f'{start_year}-01-01', end_date=f'{end_year}-12-31') # After getting the start and end years, filter the dataset by launch date
    filtered_df = dataset.launch.df
    
    filtered_df = filtered_df[filtered_df['Apogee'] != 0] # Remove 0 values
    filtered_df = filtered_df[filtered_df['Inc'] != 0] # Remove 0 values
    
    mda.ChartUtils.log_and_save_df("dataframe", output_name, output_prefix, filtered_df)
    
    pivoted_df = mda.ChartUtils.pivot_dataframe(filtered_df, index_col='Inc', column_col=series_column, value_col='Apogee') # Pivot for plotting

    # Reorder in the order of the color map
    if color_map is not None and type(color_map) is dict:
        cols = list(color_map.keys())
        cols = [col for col in cols if col in pivoted_df.columns] # Remove keys that are not in the pivoted_df columns
        cols.insert(0, 'Inc')  # Ensure 'Inc' is always included as the first column
        pivoted_df = pivoted_df.reindex(columns=cols)

    # Save to CSV
    mda.ChartUtils.log_and_save_df("csv", output_name, output_prefix, pivoted_df)

    if series_title is None:
        series_title = series_column.replace("_", " ").title()
    
    mda.ChartUtils.plot_scatter(
        pivoted_df,
        x_col='Inc',
        y_cols=pivoted_df.columns,
        title=f'{chart_title_prefix} Launches Apogee vs Inclination by {series_title}',
        subtitle=f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label='Inclination (degrees)',
        y_label='Apogee (km)',
        dot_diameter=10,
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        color_map=color_map,
    )

def payloads_filtered_vs_year_by_filter(chart_title_prefix, output_prefix, chart_title_suffix, output_suffix, initial_filter_functions, initial_filter_function_parameters_list, filter_function, filter_function_parameters_list, filter_function_additional_parameter=None, initial_filter_function_additional_parameters=[None], x_tick_step_size=1, color_map=None, start_year=None, end_year=None):
    """Generate a chart showing the number of payloads of a particular filter (eg. filter by simple payload category for earth observation) by year, filtered by a specified filter function.
    
    Args:
        chart_title_prefix (str): Prefix for the chart title (should be the prettified name of the category) (eg. 'Orbital Payloads')
        output_prefix (str): Simplified name of category for output files (eg. 'orbital' for Orbital Payloads gives "orbital_payloads_vs_year_by_filter")
        initial_filter_functions (function): Functions to filter the dataset by before doing anything else. Eg. filter by simple payload category for observation satellites. Should take a dataset and a parameter.
        initial_filter_function_parameters (Any): Parameters to pass to the initial filter functions, one each must be same index as initial filter functions.
        filter_function (function): Function to filter the dataset by. Should take a dataset and a
        filter_function_parameters_list (list): List of parameters to pass to the filter function.
        filter_function_additional_parameter (str, optional): Additional parameter for the filter function. Defaults to None.
        initial_filter_function_additional_parameters (str, optional): List of additional parameters for the initial filter functions. Defaults to None. eg. ['Something', None, None]
        x_tick_step_size (int, optional): Step size for x-axis ticks in years. Defaults to 1 (one year).
        start_year (int, optional): Start year for the data. By default it is the first year of the specified filter in the dataset.
        end_year (int, optional): End year for the data (inclusive). By default, the final year of the specified filter is used.
    """
    
    dataset = mda.McdowellDataset("./datasets")
    
    # Apply initial filters
    for initial_filter_function, initial_filter_parameter, initial_additional_parameter in zip(initial_filter_functions, initial_filter_function_parameters_list, initial_filter_function_additional_parameters):
        if initial_additional_parameter is not None:
            initial_filter_function(dataset.satcat, initial_filter_parameter, initial_additional_parameter)
        else:
            initial_filter_function(dataset.satcat, initial_filter_parameter)
            
    if start_year == None:
        start_year = dataset.satcat.df['Launch_Date'].dt.year.min()
    if end_year == None:
        end_year = dataset.satcat.df['Launch_Date'].dt.year.max()

    date_end = "present" if end_year == datetime.now().year else  f"{end_year}"
    output_name = f"{output_prefix}_payloads_vs_year_by_{output_suffix}_{start_year}_{date_end}"

    # After getting the start and end years, filter the dataset by launch date
    mda.Filters.filter_by_launch_date(dataset.satcat, start_date=f'{start_year}-01-01', end_date=f'{end_year}-12-31')
    
    dataset.satcat.df['Launch_Year'] = dataset.satcat.df['Launch_Date'].dt.year
    filtered_df = dataset.satcat.df
    
    mda.ChartUtils.log_and_save_df("dataframe", output_name, output_prefix, filtered_df)
    
    # Create a dictionary with key filters and values are dataframes for each filter showing the number of payloads per year
    dataframes = mda.ChartUtils.group_dataset_into_dictionary_by_filter_function(
        dataset.satcat,
        filter_function=filter_function,
        groups=filter_function_parameters_list,
        groupby_col="Launch_Year",
        count_values=True,
        filter_function_additional_parameter=filter_function_additional_parameter
    )
    
    output_df = mda.ChartUtils.combine_dictionary_of_dataframes(dataframes)
    
    # Save to CSV
    mda.ChartUtils.log_and_save_df("csv", output_name, output_prefix, output_df)
    
    mda.ChartUtils.plot_bar(
        output_df,
        title=f"{chart_title_prefix} Payloads vs Year by {chart_title_suffix}",
        subtitle=f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label="Year",
        y_label="Number of Payloads",
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        bargap=0.0,
        x_tick_step_size=x_tick_step_size,
        color_map=color_map,
    )

def payloads_vs_mass_by_filter(chart_title_prefix, output_prefix, chart_title_suffix, output_suffix, filter_function, filter_function_parameters_list, filter_function_additional_parameter=None, mass_step_size_kg=1000, launch_vehicle_simplified_name=None, launch_vehicle_family=None, color_map=None, mass_suffix='t', mass_divisor=100, filter_out_suborbital=True, country=None, max_mass=None):
    """Generate a chart showing the number of payloads by payload mass range by a given filter function (eg. launch vehicle, launch category, etc.).
    Eg. How many payloads were 2-3 tonnes and LEO, how many 6-7 tonnes and GTO, etc.

    Args:
        chart_title_prefix (str): Prefix for the chart title (should be the prettified name of the launch vehicle) (eg. 'Falcon 9') 
        output_prefix (str): Simplified name of LV for output files (eg. 'f9' for Falcon 9 gives "f9_launches_vs_mass_by_orbit")
        filter_function (function): Function to filter the dataset by (eg. mda.Filters.filter_by_launch_vehicle_name_simplified)
        filter_function_parameters_list (list): List of parameters to pass to the filter function
        filter_function_additional_parameter (str): Additional parameter to pass to the filter function if needed
        mass_step_size_kg (int): Step size in kg for the mass bins (eg. 1000 gives bins of 0-1000 kg, 1000-2000 kg, etc.)
        launch_vehicle_simplified_name (str, optional): Launch vehicle to filter by
        launch_vehicle_family (str, optional): Family of launch vehicle to filter by. If not none, then filtering will be done by family instead of the launch_vehicle field.
        mass_suffix (str, optional): Suffix for the mass labels (default is 't' for tonnes, use 'kg' if you want). Defaults to 't'.
        mass_divisor (int, optional): Divisor for the mass values in the chart (default is 1000 to convert kg to tonnes). Defaults to 1000.
    """
    
    output_name = f"{output_prefix}_payloads_vs_mass_by_{output_suffix}"

    # Initialize dataset
    dataset = mda.McdowellDataset("./datasets")

    mda.Filters.filter_by_sat_type_coarse(dataset.satcat, 'P')
    if launch_vehicle_family is not None:
        mda.Filters.filter_by_launch_vehicle_family(dataset.satcat, launch_vehicle_family)
    if launch_vehicle_simplified_name is not None:
        mda.Filters.filter_by_launch_vehicle_name_simplified(dataset.satcat, launch_vehicle_simplified_name)
    if country is not None:
        mda.Filters.filter_by_country(dataset.satcat, country)

    mda.ChartUtils.log_and_save_df("dataframe", output_name, output_prefix, dataset.satcat.df)
    
    if max_mass is None:
        max_mass = int(dataset.satcat.df['Mass'].max())

    # Define mass bins and labels
    bins = list(range(0, max_mass+mass_step_size_kg, mass_step_size_kg)) # +mass_step_size_kg bc. range is exclusive
    mass_labels = [f"{int(bins[i]/mass_divisor)}-{int(bins[i+1]/mass_divisor)}{mass_suffix}" for i in range(len(bins)-1)]

    # Create a dictionary with key orbits and values are dataframes for each orbit showing the number of launches per payload mass range
    dataframes = mda.ChartUtils.bin_dataset_into_dictionary_by_filter_function(
        dataset=dataset.satcat,
        filter_function=filter_function,
        filter_function_parameters_list=filter_function_parameters_list,
        value_col='Mass',
        bins=bins,
        bin_labels=mass_labels,
        filter_function_additional_parameter=filter_function_additional_parameter,
    )

    # Create dictionary with columns that are the orbits and values are the mass ranges
    output_df = mda.ChartUtils.combine_dictionary_of_dataframes(dataframes)

    # Save to CSV
    mda.ChartUtils.log_and_save_df("csv", output_name, output_prefix, output_df)

    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Payloads vs. Payload Mass by {chart_title_suffix}',
        subtitle=f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label=f'Payload Mass Range ({mass_suffix})',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        color_map=color_map,
        bargap=0.1,
    )
    
def cumulative_payloads_by_filter_vs_date_since_first_payload(chart_title_prefix, output_prefix, filter_function, filter_function_parameters_list, filter_function_additional_parameter=None, series_names=None, color_map=None, start_year=None, end_year=None, date_column='Launch_Date', y_axis_type='linear', line_width=2, max_cumulative_payloads=None, max_days_since_first=None):
    """
    Plot cumulative payloads by filter vs date since first payload, with option for multiple series (e.g., OneWeb, Starlink).
    
    This normalizes all launches to a common start date for visualization.
    
    Args:
        chart_title_prefix (str): Chart title prefix.
        output_prefix (str): Output file prefix.
        filter_function (function): Function to filter the satcat dataset.
        filter_function_parameters_list (list): List of filter parameters (one per series).
        filter_function_additional_parameter (any, optional): Additional parameter for filter function.
        series_names (list, optional): Names for each series (defaults to filter_function_parameters_list).
        color_map (dict or list, optional): Color mapping for series.
        start_year (int, optional): Start year for data.
        end_year (int, optional): End year for data.
        date_column (str, optional): Date column to use (default 'Launch_Date').
        y_axis_type (str, optional): 'linear' or 'log' for y-axis scaling.
        line_width (int, optional): Width of the lines. Defaults to 2.
        max_cumulative_payloads (int, optional): Maximum cumulative payload count to display on y-axis.
        max_days_since_first (int, optional): Maximum days since first launch to display on x-axis.
    """
    
    dataset = mda.McdowellDataset("./datasets")
    
    if start_year == None:
        start_year = dataset.launch.df['Launch_Date'].dt.year.min()
    if end_year == None:
        end_year = dataset.launch.df['Launch_Date'].dt.year.max()
        
    date_end = "present" if end_year == datetime.now().year else  f"{end_year}"
    output_name = f"{output_prefix}_vs_date_since_first_payload_by_filter_{start_year}_{date_end}"
    output_name += f"_{max_cumulative_payloads}" if max_cumulative_payloads is not None else ""
    output_name += f"_{max_days_since_first}" if max_days_since_first is not None else ""
    output_name += "_log" if y_axis_type == 'log' else ""
    
    # After getting the start and end years, filter the dataset by launch date
    mda.Filters.filter_by_launch_date(dataset.launch, start_date=f'{start_year}-01-01', end_date=f'{end_year}-12-31')
    
    mda.ChartUtils.log_and_save_df("dataframe", output_name, output_prefix, dataset.launch.df)
    
    dataframes = mda.ChartUtils.filter_dataset_into_dictionary_by_filter_function(
        dataset.satcat,
        filter_function=filter_function,
        filter_function_parameters_list=filter_function_parameters_list,
        filter_function_additional_parameter=filter_function_additional_parameter
    )
    
    # Create dict of first payload launch date for each dataframe
    first_payload_dates = {}
    for filter_function_parameter in filter_function_parameters_list:
        first_payload_dates[filter_function_parameter] = dataframes[filter_function_parameter]['Launch_Date'].min()
        
    # Create new column of time since first payload in each dataframe
    for filter_function_parameter in filter_function_parameters_list:
        first_payload_date = first_payload_dates[filter_function_parameter]
        dataframes[filter_function_parameter]['Time_Since_First_Payload'] = (
            dataframes[filter_function_parameter]['Launch_Date'] - first_payload_date
        ).dt.days

    # Now sum cumulative payloads for each dataframe, versus time_since_first_payload
    cumulative_dataframes = mda.ChartUtils.create_cumulative_series_by_column(
        dataframes_dict=dataframes,
        column_name='Time_Since_First_Payload'
    )
    
    # Combine all series into a single dataframe (use 'none' to avoid lines dropping to zero)
    output_df = mda.ChartUtils.combine_cumulative_series(cumulative_dataframes, fill_method='none')
    
    # Rename columns using series_names if provided
    if series_names:
        column_mapping = dict(zip(filter_function_parameters_list, series_names))
        output_df.rename(columns=column_mapping, inplace=True)
    
    # Reset index to have Time_Since_First_Payload as a column for plotting
    output_df.reset_index(inplace=True)
    
    # Apply limits if specified
    if max_days_since_first is not None:
        output_df = output_df[output_df['Time_Since_First_Payload'] <= max_days_since_first]
    
    if max_cumulative_payloads is not None:
        # Clip all payload columns to the maximum value
        payload_columns = output_df.columns[1:].tolist()  # All columns except Time_Since_First_Payload
        for col in payload_columns:
            output_df[col] = output_df[col].clip(upper=max_cumulative_payloads)
    
    # Save to CSV
    mda.ChartUtils.log_and_save_df("csv", output_name, output_prefix, output_df)
    
    # Create line chart
    y_columns = output_df.columns[1:].tolist()  # All columns except Time_Since_First_Payload
    
    mda.ChartUtils.plot_line(
        output_df,
        x_col='Time_Since_First_Payload',
        y_cols=y_columns,
        title=f'{chart_title_prefix} Cumulative Sats vs. Days Since First Launch',
        subtitle=f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label='Days Since First Launch',
        y_label='Cumulative Number of Sats',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        color_map=color_map,
        line_width=line_width,
        y_axis_type=y_axis_type,
    )


# ---------------------------------------------------------------------------
# Helpers used by commercial western category charts
# ---------------------------------------------------------------------------

_SMALL_SAT_MASS_KG = 600
_RIDESHARE_THRESHOLD = 10  # payloads on same launch to qualify as rideshare

# Small-sat constellations: individually small but part of a deployed constellation
_LEO_CONSTELLATION_KEYWORDS = [
    'OneWeb', 'Kuiper', 'Telesat', 'Iridium', 'Globalstar', 'Orbcomm',
    'Swarm', 'Spire', 'ICEYE', 'Flock', 'H360',
    'Kineis', 'Kepler', 'Satelog', 'Astrocast', 'Myriota',
]

_GEO_MEO_CONSTELLATION_KEYWORDS = ['O3b', 'mPOWER']

_CAPSULE_CARGO_KEYWORDS = ['Dragon', 'Cygnus', 'Starliner', 'CST-100', 'Dream Chaser']

COMMERCIAL_WESTERN_CATEGORY_ORDER = [
    'Starlink',
    'LEO Constellation',
    'GEO/MEO Constellation',
    'Small Sat Rideshare',
    'Small Sat',
    'Commercial LEO/SSO/MEO',
    'Commercial GTO/GEO',
    'Capsule/Cargo',
    'High-Energy',
]

# Priority used when collapsing payload categories to one label per launch (lower = wins).
# Separate from display order: Capsule/Cargo wins over Small Sat so a Dragon mission
# carrying cubesat secondaries is classified as Capsule/Cargo, not Small Sat.
_CATEGORY_PRIORITY = {
    'Starlink': 0,
    'Capsule/Cargo': 1,
    'GEO/MEO Constellation': 2,
    'LEO Constellation': 3,
    'High-Energy': 4,
    'Commercial GTO/GEO': 5,
    'Small Sat Rideshare': 6,
    'Commercial LEO/SSO/MEO': 7,
    'Small Sat': 8,
}


def _derive_orbit_from_apogee(apogee_series, perigee_series=None):
    """Map apogee (km) to a simple orbit string. Returns a Series of strings."""
    import numpy as np

    apo = apogee_series.copy()
    peri = perigee_series if perigee_series is not None else pd.Series([0.0] * len(apo), index=apo.index)

    conditions = [
        (apo <= 0) | apo.isna(),
        apo < 2000,
        (apo >= 2000) & (apo < 35000),
        (apo >= 35000) & (apo < 42000) & (peri.fillna(0) > 25000),  # circular near GEO
        (apo >= 35000) & (apo < 42000),                              # elliptical → GTO
    ]
    choices = ['Unknown', 'LEO', 'MEO', 'GEO', 'GTO']
    return pd.Series(np.select(conditions, choices, default='HEO'), index=apo.index)


def _load_psatcat_orbit(df, launch_df=None):
    """Merge psatcat UN-registration orbit data into *df* and add Derived_Orbit column.

    Falls back to Simple_Orbit from launch_df for entries where apogee data is unavailable.
    """
    psatcat = pd.read_csv("./datasets/psatcat.tsv", sep="\t", encoding="utf-8", low_memory=False)
    psatcat = psatcat.drop(index=0).reset_index(drop=True)
    psatcat.rename(columns={"#JCAT": "JCAT"}, inplace=True)
    psatcat["JCAT"] = psatcat["JCAT"].astype(str).str.upper().str.strip()
    for col in ["UNApogee", "UNPerigee", "DispApo", "DispPeri"]:
        psatcat[col] = pd.to_numeric(psatcat[col], errors="coerce")

    df = df.merge(psatcat[["JCAT", "UNApogee", "UNPerigee", "DispApo", "DispPeri"]], on="JCAT", how="left")
    eff_apo  = df["UNApogee"].where(df["UNApogee"].fillna(0) > 0, df["DispApo"])
    eff_peri = df["UNPerigee"].where(df["UNPerigee"].fillna(0) > 0, df["DispPeri"])
    df["Derived_Orbit"] = _derive_orbit_from_apogee(eff_apo, eff_peri)

    if launch_df is not None and "Simple_Orbit" in launch_df.columns:
        orbit_lookup = (
            launch_df[["Launch_Tag", "Simple_Orbit"]]
            .drop_duplicates("Launch_Tag")
            .rename(columns={"Simple_Orbit": "_Launch_Simple_Orbit"})
        )
        df = df.merge(orbit_lookup, on="Launch_Tag", how="left")
        unknown_mask = df["Derived_Orbit"] == "Unknown"
        df.loc[unknown_mask, "Derived_Orbit"] = df.loc[unknown_mask, "_Launch_Simple_Orbit"].fillna("Unknown").values
        df = df.drop(columns=["_Launch_Simple_Orbit"])

    return df


def _filter_commercial_western(df):
    """Return commercial western payload rows from a satcat-style dataframe."""
    return df[
        (df["Type"].str.strip().str.startswith("P", na=False)) &
        (~df["Launch_State"].isin(["CN", "RU", "SU"])) &
        (df["Payload_Class"] == "B")
    ].copy()


def _classify_commercial_western_categories(df, orbit_col='Derived_Orbit'):
    """Return a copy of *df* with 'Commercial_Western_Category' column.

    Rows must already be filtered to western commercial payloads only.

    Categories (highest priority wins):
        Starlink > Capsule/Cargo > High-Energy > GEO/MEO Constellation
        > LEO Constellation > Commercial GTO/GEO > Commercial LEO/SSO/MEO
        > Small Sat Rideshare > Small Sat
    """
    df = df.copy()

    # Default by mass: large payload → Commercial LEO/SSO/MEO, small → Small Sat
    df['Commercial_Western_Category'] = 'Commercial LEO/SSO/MEO'
    small_mask = df['Mass'] <= _SMALL_SAT_MASS_KG
    df.loc[small_mask, 'Commercial_Western_Category'] = 'Small Sat'

    # Orbit-based overrides
    gto_geo_mask = df[orbit_col].isin(['GTO', 'GEO'])
    df.loc[gto_geo_mask, 'Commercial_Western_Category'] = 'Commercial GTO/GEO'

    heo_mask = df[orbit_col] == 'HEO'
    df.loc[heo_mask, 'Commercial_Western_Category'] = 'High-Energy'

    # Small sat rideshare: many small payloads on the same launch
    small_per_launch = df.loc[small_mask].groupby('Launch_Tag').size()
    rideshare_tags = set(small_per_launch[small_per_launch > _RIDESHARE_THRESHOLD].index)
    df.loc[small_mask & df['Launch_Tag'].isin(rideshare_tags), 'Commercial_Western_Category'] = 'Small Sat Rideshare'

    # GEO/MEO constellations (override orbit/size categories)
    gmc_pattern = '|'.join(_GEO_MEO_CONSTELLATION_KEYWORDS)
    gmc_mask = (
        df['Payload_Program'].str.contains(gmc_pattern, case=False, na=False) |
        df['Payload_Name'].str.contains(gmc_pattern, case=False, na=False)
    )
    df.loc[gmc_mask, 'Commercial_Western_Category'] = 'GEO/MEO Constellation'

    # LEO constellations (override orbit/size categories)
    lc_pattern = '|'.join(_LEO_CONSTELLATION_KEYWORDS)
    lc_mask = (
        df['Payload_Program'].str.contains(lc_pattern, case=False, na=False) |
        df['Payload_Name'].str.contains(lc_pattern, case=False, na=False)
    )
    df.loc[lc_mask, 'Commercial_Western_Category'] = 'LEO Constellation'

    # Capsule/Cargo (override constellations)
    cap_pattern = '|'.join(_CAPSULE_CARGO_KEYWORDS)
    cap_mask = (
        df['Payload_Program'].str.contains(cap_pattern, case=False, na=False) |
        df['Payload_Name'].str.contains(cap_pattern, case=False, na=False)
    )
    df.loc[cap_mask, 'Commercial_Western_Category'] = 'Capsule/Cargo'

    # Starlink always wins
    sl_mask = (
        df['Payload_Name'].str.contains('Starlink', case=False, na=False) |
        df['Payload_Program'].str.contains('Starlink', case=False, na=False)
    )
    df.loc[sl_mask, 'Commercial_Western_Category'] = 'Starlink'

    return df


def _get_classified_cw_satcat(dataset):
    """Return a satcat dataframe with commercial western payloads classified."""
    df = _filter_commercial_western(dataset.satcat.df.copy())
    df = _load_psatcat_orbit(df, dataset.launch.df)
    df = _classify_commercial_western_categories(df)
    return _apply_effective_mass(df)


def _apply_effective_mass(satcat_df):
    """Add Effective_Mass column: TotMass for capsule/cargo spacecraft where TotMass > Mass.

    Cygnus/HTV: Mass = cargo only, TotMass = full spacecraft.
    Dragon: Mass = cargo+capsule (lower estimate), TotMass = full assembly.
    Normal satellites: TotMass == Mass so no change.
    """
    satcat_df = satcat_df.copy()
    satcat_df['Effective_Mass'] = satcat_df['Mass'].copy()
    _cap_pattern = '|'.join(_CAPSULE_CARGO_KEYWORDS)
    cap_mask = (
        satcat_df['Name'].astype(str).str.strip().str.contains(_cap_pattern, case=False, na=False) |
        satcat_df['Payload_Name'].astype(str).str.contains(_cap_pattern, case=False, na=False) |
        satcat_df['Payload_Program'].astype(str).str.contains(_cap_pattern, case=False, na=False)
    )
    tot_mask = cap_mask & (satcat_df['TotMass'] > satcat_df['Mass'])
    satcat_df.loc[tot_mask, 'Effective_Mass'] = satcat_df.loc[tot_mask, 'TotMass']
    return satcat_df


def _mass_per_launch(satcat_df):
    """Return a Series of total Effective_Mass per Launch_Tag."""
    return satcat_df.groupby('Launch_Tag')['Effective_Mass'].sum()


def commercial_western_payload_categories_pie(
    chart_title_prefix='Commercial Western',
    output_prefix='commercial_western',
    start_year=None,
    end_year=None,
    date_range=None,
):
    """Generate pie charts of commercial western payloads broken down by mission category.

    Produces two charts:
        - Payload count per category
        - Total launched mass per category (tonnes)

    Western = Launch_State not in CN / RU / SU.
    Commercial = Payload_Class == 'B' (Business).
    Orbit is derived from psatcat UN-registration apogee/perigee.

    Args:
        chart_title_prefix (str): Prefix for chart titles.
        output_prefix (str): Prefix for output file names.
        start_year (int, optional): Start year for filtering data.
        end_year (int, optional): End year for filtering data.
    """
    output_name_count = f"{output_prefix}_payload_category_count_pie"
    output_name_mass  = f"{output_prefix}_payload_category_mass_pie"

    dataset = mda.McdowellDataset("./datasets")
    df = _get_classified_cw_satcat(dataset)

    # Optional date range filter
    if start_year is not None:
        df = df[df['Launch_Date'].dt.year >= start_year]
    if end_year is not None:
        df = df[df['Launch_Date'].dt.year <= end_year]

    count_by_cat = df.groupby('Commercial_Western_Category').size().reindex(COMMERCIAL_WESTERN_CATEGORY_ORDER, fill_value=0)
    mass_by_cat  = (df.groupby('Commercial_Western_Category')['Mass'].sum() / 1000).reindex(COMMERCIAL_WESTERN_CATEGORY_ORDER, fill_value=0)

    count_by_cat = count_by_cat[count_by_cat > 0]
    mass_by_cat  = mass_by_cat[mass_by_cat > 0]

    mda.ChartUtils.log_and_save_df("csv", output_name_count, output_prefix,
                                   count_by_cat.rename("Count").reset_index())
    mda.ChartUtils.log_and_save_df("csv", output_name_mass, output_prefix,
                                   mass_by_cat.rename("Mass_t").reset_index())

    color_map = mda.ChartUtils.commercial_western_category_color_map

    date_range_note = f' - {date_range}' if date_range else ''
    cw_subtitle = f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}{date_range_note}'

    mda.ChartUtils.plot_pie(
        values=count_by_cat.values,
        names=count_by_cat.index.tolist(),
        title=f'{chart_title_prefix} Payload Count by Category',
        subtitle=cw_subtitle,
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name_count}.png',
        color_map=color_map,
    )

    mda.ChartUtils.plot_pie(
        values=mass_by_cat.values,
        names=mass_by_cat.index.tolist(),
        title=f'{chart_title_prefix} Total Launched Mass by Category',
        subtitle=cw_subtitle,
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name_mass}.png',
        color_map=color_map,
    )


def _dominant_launch_category(satcat_df):
    """Assign one commercial western category to each launch.

    Uses priority ordering (Starlink > Capsule/Cargo > ...) but detects
    rideshare launches by program-diversity so mixed Transporter missions
    are classified as 'Small Sat Rideshare' rather than 'LEO Constellation'.

    A launch is 'Small Sat Rideshare' if it has > _RIDESHARE_THRESHOLD small
    commercial western payloads from at least 5 distinct Payload_Programs.
    """
    _RIDESHARE_PROGRAM_THRESHOLD = 5

    small_mask = satcat_df['Mass'] <= _SMALL_SAT_MASS_KG
    small_df = satcat_df[small_mask]

    # Unique program count per launch among small payloads
    unique_programs = small_df.groupby('Launch_Tag')['Payload_Program'].nunique()
    small_count = small_df.groupby('Launch_Tag').size()

    rideshare_launch_tags = set(
        small_count[
            (small_count > _RIDESHARE_THRESHOLD) &
            (unique_programs >= _RIDESHARE_PROGRAM_THRESHOLD)
        ].index
    )

    def dominant(group):
        tag = group.name
        if tag in rideshare_launch_tags:
            return 'Small Sat Rideshare'
        return min(group, key=lambda c: _CATEGORY_PRIORITY.get(c, 99))

    return (
        satcat_df.groupby('Launch_Tag')['Commercial_Western_Category']
        .apply(dominant)
        .reset_index()
        .rename(columns={'Commercial_Western_Category': 'Launch_Category'})
    )


def commercial_western_launches_vs_mass_by_category(
    chart_title_prefix='Commercial Western',
    output_prefix='commercial_western',
    mass_step_size_kg=1000,
    max_display_mass_kg=20000,
    mass_suffix='t',
    mass_divisor=1000,
    start_year=None,
    end_year=None,
    date_range=None,
):
    """Generate a bar chart: launches vs payload mass range by commercial western category.

    Each launch is assigned one category. Rideshare is detected by program
    diversity so Transporter-style missions appear as 'Small Sat Rideshare'
    even when they also carry constellation satellites.

    X-axis = total payload mass range, Y-axis = launch count, series = category.

    Args:
        chart_title_prefix (str): Prefix for chart titles.
        output_prefix (str): Prefix for output file names.
        mass_step_size_kg (int): Width of each mass bin in kg. Default 1000 (1 tonne).
        max_display_mass_kg (int): Cap on displayed mass range. Default 20000 (20 t).
        mass_suffix (str): Unit label suffix. Default 't'.
        mass_divisor (int): Divisor to convert kg to display units. Default 1000.
        start_year (int, optional): Inclusive start year filter. Default None (all years).
        end_year (int, optional): Inclusive end year filter. Default None (all years).
    """
    output_name = f"{output_prefix}_launches_vs_mass_by_category"

    dataset = mda.McdowellDataset("./datasets")

    satcat_df = _get_classified_cw_satcat(dataset)  # already applies _apply_effective_mass
    launch_category = _dominant_launch_category(satcat_df)
    cw_mass_by_launch = _mass_per_launch(satcat_df)

    launch_df = dataset.launch.df[['Launch_Tag', 'Launch_Date', 'LV_Type', 'Mission']].copy()
    launch_df = launch_df.merge(launch_category, on='Launch_Tag', how='inner')
    launch_df['Payload_Mass'] = launch_df['Launch_Tag'].map(cw_mass_by_launch).fillna(0)

    launch_df = launch_df[launch_df['Payload_Mass'] > 0].sort_values('Launch_Date')

    # Optional date range filter
    if start_year is not None:
        launch_df = launch_df[launch_df['Launch_Date'].dt.year >= start_year]
    if end_year is not None:
        launch_df = launch_df[launch_df['Launch_Date'].dt.year <= end_year]

    # Save the per-launch raw dataframe (all launches, not just display range)
    mda.ChartUtils.log_and_save_df("dataframe", output_name, output_prefix,
                                   launch_df[['Launch_Tag', 'Launch_Date', 'LV_Type', 'Mission',
                                              'Payload_Mass', 'Launch_Category']])

    # Clip to display range (very heavy Starship launches would dominate otherwise)
    launch_df = launch_df[launch_df['Payload_Mass'] <= max_display_mass_kg]

    bins = list(range(0, max_display_mass_kg + mass_step_size_kg, mass_step_size_kg))
    mass_labels = [f"{int(bins[i]/mass_divisor)}-{int(bins[i+1]/mass_divisor)}{mass_suffix}"
                   for i in range(len(bins) - 1)]

    output_dict = {}
    for cat in COMMERCIAL_WESTERN_CATEGORY_ORDER:
        cat_df = launch_df[launch_df['Launch_Category'] == cat]
        binned = pd.cut(cat_df['Payload_Mass'], bins=bins, labels=mass_labels, include_lowest=True)
        output_dict[cat] = binned.value_counts().reindex(mass_labels, fill_value=0)

    output_df = pd.DataFrame(output_dict, index=mass_labels)

    # Trim trailing all-zero rows
    last_nonzero = (output_df.sum(axis=1) > 0).cumsum()
    output_df = output_df.loc[last_nonzero > 0]

    mda.ChartUtils.log_and_save_df("csv", output_name, output_prefix, output_df)

    date_range_note = f' - {date_range}' if date_range else ''
    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Launches vs. Payload Mass by Category',
        subtitle=f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}{date_range_note}',
        x_label=f'Payload Mass Range ({mass_suffix})',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        color_map=mda.ChartUtils.commercial_western_category_color_map,
        bargap=0.1,
    )


def commercial_western_rideshare_by_lv(
    chart_title_prefix='Commercial Western',
    output_prefix='commercial_western',
    mass_step_size_kg=1000,
    max_display_mass_kg=10000,
    mass_suffix='t',
    mass_divisor=1000,
    start_year=None,
    end_year=None,
    date_range=None,
):
    """Generate bar and pie charts for Small Sat Rideshare launches broken down by launch vehicle.

    Produces three charts:
        - Launches vs. Payload Mass by Launch Vehicle (bar chart)
        - Rideshare Payload Count by Launch Vehicle (pie)
        - Rideshare Total Launched Mass by Launch Vehicle (pie)

    Args:
        chart_title_prefix (str): Prefix for chart titles.
        output_prefix (str): Prefix for output file names.
        mass_step_size_kg (int): Width of each mass bin in kg. Default 1000.
        max_display_mass_kg (int): Cap on displayed mass range. Default 10000.
        mass_suffix (str): Unit label suffix. Default 't'.
        mass_divisor (int): Divisor to convert kg to display units. Default 1000.
        start_year (int, optional): Inclusive start year filter.
        end_year (int, optional): Inclusive end year filter.
        date_range (str, optional): Display label for subtitle.
    """
    output_name_bar   = f"{output_prefix}_rideshare_launches_vs_mass_by_lv"
    output_name_count = f"{output_prefix}_rideshare_lv_count_pie"
    output_name_mass  = f"{output_prefix}_rideshare_lv_mass_pie"

    dataset = mda.McdowellDataset("./datasets")

    satcat_df = _get_classified_cw_satcat(dataset)
    launch_category = _dominant_launch_category(satcat_df)
    cw_mass_by_launch = _mass_per_launch(satcat_df)

    launch_df = dataset.launch.df[['Launch_Tag', 'Launch_Date', 'LV_Type', 'Mission']].copy()
    launch_df = launch_df.merge(launch_category, on='Launch_Tag', how='inner')
    launch_df['Payload_Mass'] = launch_df['Launch_Tag'].map(cw_mass_by_launch).fillna(0)

    launch_df = launch_df[launch_df['Payload_Mass'] > 0].sort_values('Launch_Date')

    # Filter to Small Sat Rideshare only
    launch_df = launch_df[launch_df['Launch_Category'] == 'Small Sat Rideshare']

    if start_year is not None:
        launch_df = launch_df[launch_df['Launch_Date'].dt.year >= start_year]
    if end_year is not None:
        launch_df = launch_df[launch_df['Launch_Date'].dt.year <= end_year]

    lv_order = launch_df.groupby('LV_Type')['Payload_Mass'].sum().sort_values(ascending=False).index.tolist()

    date_range_note = f' - {date_range}' if date_range else ''
    subtitle = (f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell'
                f' - Data Cutoff: {dataset.date_updated}{date_range_note}')
    color_map = mda.ChartUtils.rideshare_lv_color_map

    # --- Bar chart ---
    bar_df = launch_df[launch_df['Payload_Mass'] <= max_display_mass_kg].copy()
    bins = list(range(0, max_display_mass_kg + mass_step_size_kg, mass_step_size_kg))
    mass_labels = [f"{int(bins[i]/mass_divisor)}-{int(bins[i+1]/mass_divisor)}{mass_suffix}"
                   for i in range(len(bins) - 1)]

    output_dict = {}
    for lv in lv_order:
        lv_df = bar_df[bar_df['LV_Type'] == lv]
        binned = pd.cut(lv_df['Payload_Mass'], bins=bins, labels=mass_labels, include_lowest=True)
        output_dict[lv] = binned.value_counts().reindex(mass_labels, fill_value=0)

    output_df = pd.DataFrame(output_dict, index=mass_labels)
    last_nonzero = (output_df.sum(axis=1) > 0).cumsum()
    output_df = output_df.loc[last_nonzero > 0]

    mda.ChartUtils.log_and_save_df("csv", output_name_bar, output_prefix, output_df)
    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Small Sat Rideshare Launches vs. Payload Mass by Launch Vehicle',
        subtitle=subtitle,
        x_label=f'Payload Mass Range ({mass_suffix})',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name_bar}.png',
        color_map=color_map,
        bargap=0.1,
    )

    # --- Pie charts ---
    count_by_lv = launch_df.groupby('LV_Type').size().reindex(lv_order, fill_value=0)
    mass_by_lv  = (launch_df.groupby('LV_Type')['Payload_Mass'].sum() / 1000).reindex(lv_order, fill_value=0)

    mda.ChartUtils.log_and_save_df("csv", output_name_count, output_prefix,
                                   count_by_lv.rename("Count").reset_index())
    mda.ChartUtils.log_and_save_df("csv", output_name_mass, output_prefix,
                                   mass_by_lv.rename("Mass_t").reset_index())

    mda.ChartUtils.plot_pie(
        values=count_by_lv.values,
        names=count_by_lv.index.tolist(),
        title=f'{chart_title_prefix} Small Sat Rideshare Launch Count by Launch Vehicle',
        subtitle=subtitle,
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name_count}.png',
        color_map=color_map,
    )

    mda.ChartUtils.plot_pie(
        values=mass_by_lv.values,
        names=mass_by_lv.index.tolist(),
        title=f'{chart_title_prefix} Small Sat Rideshare Total Mass by Launch Vehicle',
        subtitle=subtitle,
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name_mass}.png',
        color_map=color_map,
    )


def western_launches_vs_mass_by_lv(
    chart_title_prefix='Western',
    output_prefix='western',
    mass_step_size_kg=1000,
    max_display_mass_kg=20000,
    mass_suffix='t',
    mass_divisor=1000,
    start_year=None,
    end_year=None,
    date_range=None,
):
    """Generate a bar chart: all western launches vs payload mass by launch vehicle (top 14 + Other).

    X-axis = total payload mass range, Y-axis = launch count, series = launch vehicle.

    Args:
        chart_title_prefix (str): Prefix for chart titles.
        output_prefix (str): Prefix for output file names.
        mass_step_size_kg (int): Width of each mass bin in kg. Default 1000 (1 tonne).
        max_display_mass_kg (int): Cap on displayed mass range. Default 20000 (20 t).
        mass_suffix (str): Unit label suffix. Default 't'.
        mass_divisor (int): Divisor to convert kg to display units. Default 1000.
        start_year (int, optional): Inclusive start year filter.
        end_year (int, optional): Inclusive end year filter.
        date_range (str, optional): Display label for subtitle.
    """
    output_name = f"{output_prefix}_launches_vs_mass_by_lv"

    dataset = mda.McdowellDataset("./datasets")

    satcat_df = _filter_western_all(dataset.satcat.df.copy())
    satcat_df = _apply_effective_mass(satcat_df)
    mass_by_launch = _mass_per_launch(satcat_df)

    launch_df = dataset.launch.df[['Launch_Tag', 'Launch_Date', 'LV_Type', 'Mission']].copy()
    launch_df['Payload_Mass'] = launch_df['Launch_Tag'].map(mass_by_launch).fillna(0)
    launch_df = launch_df[launch_df['Payload_Mass'] > 0].sort_values('Launch_Date')

    if start_year is not None:
        launch_df = launch_df[launch_df['Launch_Date'].dt.year >= start_year]
    if end_year is not None:
        launch_df = launch_df[launch_df['Launch_Date'].dt.year <= end_year]

    launch_df = launch_df[launch_df['Payload_Mass'] <= max_display_mass_kg]

    lv_by_mass = launch_df.groupby('LV_Type')['Payload_Mass'].sum().sort_values(ascending=False)
    top_lvs = lv_by_mass.index[:12].tolist()
    launch_df['LV_Display'] = launch_df['LV_Type'].where(
        launch_df['LV_Type'].isin(top_lvs), other='Other'
    )
    lv_order = top_lvs + (['Other'] if (~launch_df['LV_Type'].isin(top_lvs)).any() else [])

    bins = list(range(0, max_display_mass_kg + mass_step_size_kg, mass_step_size_kg))
    mass_labels = [f"{int(bins[i]/mass_divisor)}-{int(bins[i+1]/mass_divisor)}{mass_suffix}"
                   for i in range(len(bins) - 1)]

    output_dict = {}
    for lv in lv_order:
        lv_df = launch_df[launch_df['LV_Display'] == lv]
        binned = pd.cut(lv_df['Payload_Mass'], bins=bins, labels=mass_labels, include_lowest=True)
        output_dict[lv] = binned.value_counts().reindex(mass_labels, fill_value=0)

    output_df = pd.DataFrame(output_dict, index=mass_labels)
    last_nonzero = (output_df.sum(axis=1) > 0).cumsum()
    output_df = output_df.loc[last_nonzero > 0]

    mda.ChartUtils.log_and_save_df("csv", output_name, output_prefix, output_df)

    date_range_note = f' - {date_range}' if date_range else ''
    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Launches vs. Payload Mass by Launch Vehicle',
        subtitle=f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}{date_range_note}',
        x_label=f'Payload Mass Range ({mass_suffix})',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        color_map=mda.ChartUtils.color_sequence_3_12 + ['#434343'],
        bargap=0.1,
    )


def western_small_sat_mass_distribution_by_lv(
    chart_title_prefix='Western',
    output_prefix='western',
    max_mass_kg=1000,
    mass_step_size_kg=50,
    start_year=None,
    end_year=None,
    date_range=None,
):
    """Bar chart: individual western small sat mass distribution by launch vehicle (top 14 + Other).

    Each bar represents individual satellites (not launches), binned by their own mass.

    Args:
        chart_title_prefix (str): Prefix for chart titles.
        output_prefix (str): Prefix for output file names.
        max_mass_kg (int): Upper mass bound in kg. Default 1000.
        mass_step_size_kg (int): Bin width in kg. Default 50.
        start_year (int, optional): Inclusive start year filter on launch date.
        end_year (int, optional): Inclusive end year filter on launch date.
        date_range (str, optional): Display label for subtitle.
    """
    output_name = f"{output_prefix}_small_sat_mass_distribution_by_lv"

    dataset = mda.McdowellDataset("./datasets")

    satcat_df = _filter_western_all(dataset.satcat.df.copy())
    satcat_df = _apply_effective_mass(satcat_df)
    mass_by_launch = _mass_per_launch(satcat_df)

    launch_df = dataset.launch.df[['Launch_Tag', 'Launch_Date', 'LV_Type']].copy()
    launch_df['Payload_Mass'] = launch_df['Launch_Tag'].map(mass_by_launch).fillna(0)
    launch_df = launch_df[(launch_df['Payload_Mass'] > 0) & (launch_df['Payload_Mass'] <= max_mass_kg)]

    if start_year is not None:
        launch_df = launch_df[launch_df['Launch_Date'].dt.year >= start_year]
    if end_year is not None:
        launch_df = launch_df[launch_df['Launch_Date'].dt.year <= end_year]

    lv_by_count = launch_df.groupby('LV_Type').size().sort_values(ascending=False)
    top_lvs = lv_by_count.index[:12].tolist()
    launch_df['LV_Display'] = launch_df['LV_Type'].where(launch_df['LV_Type'].isin(top_lvs), other='Other')
    lv_order = top_lvs + (['Other'] if (~launch_df['LV_Type'].isin(top_lvs)).any() else [])

    bins_50kg = list(range(0, max_mass_kg + mass_step_size_kg, mass_step_size_kg))
    labels_50kg = [f"{bins_50kg[i]}-{bins_50kg[i+1]}kg" for i in range(len(bins_50kg) - 1)]
    bins_1t = list(range(0, max_mass_kg + 1000, 1000))
    labels_1t = [f"{bins_1t[i]//1000}-{bins_1t[i+1]//1000}t" for i in range(len(bins_1t) - 1)]

    launch_df['Mass_Bin_50kg'] = pd.cut(launch_df['Payload_Mass'], bins=bins_50kg, labels=labels_50kg, include_lowest=True)
    launch_df['Mass_Bin_1t'] = pd.cut(launch_df['Payload_Mass'], bins=bins_1t, labels=labels_1t, include_lowest=True)

    mda.ChartUtils.log_and_save_df("dataframe", output_name, output_prefix,
                                   launch_df[['Launch_Tag', 'Launch_Date', 'LV_Type', 'LV_Display',
                                              'Payload_Mass', 'Mass_Bin_50kg', 'Mass_Bin_1t']])

    bins = bins_50kg
    mass_labels = labels_50kg

    output_dict = {}
    for lv in lv_order:
        lv_launches = launch_df[launch_df['LV_Display'] == lv]
        binned = pd.cut(lv_launches['Payload_Mass'], bins=bins, labels=mass_labels, include_lowest=True)
        output_dict[lv] = binned.value_counts().reindex(mass_labels, fill_value=0)

    output_df = pd.DataFrame(output_dict, index=mass_labels)
    last_nonzero = (output_df.sum(axis=1) > 0).cumsum()
    output_df = output_df.loc[last_nonzero > 0]

    mda.ChartUtils.log_and_save_df("csv", output_name, output_prefix, output_df)

    date_range_note = f' - {date_range}' if date_range else ''
    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Small Sat Launch Mass Distribution by Launch Vehicle',
        subtitle=f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}{date_range_note}',
        x_label='Total Payload Mass (kg)',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        color_map=mda.ChartUtils.color_sequence_3_8 + ['#434343'],
        bargap=0.1,
    )


def western_launches_vs_mass_by_lv_and_orbit(
    chart_title_prefix='Western',
    output_prefix='western',
    max_mass_kg=5000,
    mass_step_size_kg=200,
    start_year=None,
    end_year=None,
    date_range=None,
):
    """Two bar charts: western launches vs payload mass (0-5t, 200 kg bins) by LV (top 8 + Other) and by orbit.

    Args:
        chart_title_prefix (str): Prefix for chart titles.
        output_prefix (str): Prefix for output file names.
        max_mass_kg (int): Upper mass bound in kg. Default 5000.
        mass_step_size_kg (int): Bin width in kg. Default 200.
        start_year (int, optional): Inclusive start year filter.
        end_year (int, optional): Inclusive end year filter.
        date_range (str, optional): Display label for subtitle.
    """
    output_name_lv    = f"{output_prefix}_launches_vs_mass_200kg_by_lv"
    output_name_orbit = f"{output_prefix}_launches_vs_mass_200kg_by_orbit"

    dataset = mda.McdowellDataset("./datasets")

    satcat_df = _filter_western_all(dataset.satcat.df.copy())
    satcat_df = _load_psatcat_orbit(satcat_df, dataset.launch.df)
    satcat_df = _apply_effective_mass(satcat_df)
    satcat_df['Launch_Orbit'] = satcat_df['Derived_Orbit']

    mass_by_launch = _mass_per_launch(satcat_df)
    dominant_orbit = _dominant_category_by_mass(satcat_df, 'Launch_Orbit')

    # Aggregate payload names per launch for the raw dataframe
    payload_names = (
        satcat_df.groupby('Launch_Tag')['Payload_Name']
        .apply(lambda x: ', '.join(x.dropna().astype(str).unique()))
        .rename('Payload_Names')
    )

    launch_df = dataset.launch.df[['Launch_Tag', 'Launch_Date', 'LV_Type', 'Mission']].copy()
    launch_df['Payload_Mass'] = launch_df['Launch_Tag'].map(mass_by_launch).fillna(0)
    launch_df = launch_df[(launch_df['Payload_Mass'] > 0) & (launch_df['Payload_Mass'] <= max_mass_kg)]
    launch_df = launch_df.merge(dominant_orbit, on='Launch_Tag', how='left')
    launch_df['Launch_Category'] = launch_df['Launch_Category'].fillna('Unknown')

    if start_year is not None:
        launch_df = launch_df[launch_df['Launch_Date'].dt.year >= start_year]
    if end_year is not None:
        launch_df = launch_df[launch_df['Launch_Date'].dt.year <= end_year]

    bins = list(range(0, max_mass_kg + mass_step_size_kg, mass_step_size_kg))
    mass_labels = [f"{bins[i]}-{bins[i+1]}kg" for i in range(len(bins) - 1)]

    launch_df['Mass_Bin_200kg'] = pd.cut(launch_df['Payload_Mass'], bins=bins, labels=mass_labels, include_lowest=True)
    launch_df = launch_df.merge(payload_names, on='Launch_Tag', how='left')

    mda.ChartUtils.log_and_save_df("dataframe", output_name_lv, output_prefix,
                                   launch_df[['Launch_Tag', 'Launch_Date', 'LV_Type', 'Mission',
                                              'Payload_Mass', 'Mass_Bin_200kg', 'Launch_Category',
                                              'Payload_Names']])

    date_range_note = f' - {date_range}' if date_range else ''
    subtitle = (f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell'
                f' - Data Cutoff: {dataset.date_updated}{date_range_note}')

    # --- Chart by LV ---
    lv_by_count = launch_df.groupby('LV_Type').size().sort_values(ascending=False)
    top_lvs = lv_by_count.index[:8].tolist()
    launch_df['LV_Display'] = launch_df['LV_Type'].where(launch_df['LV_Type'].isin(top_lvs), other='Other')
    lv_order = top_lvs + (['Other'] if (~launch_df['LV_Type'].isin(top_lvs)).any() else [])

    output_dict = {}
    for lv in lv_order:
        lv_launches = launch_df[launch_df['LV_Display'] == lv]
        binned = pd.cut(lv_launches['Payload_Mass'], bins=bins, labels=mass_labels, include_lowest=True)
        output_dict[lv] = binned.value_counts().reindex(mass_labels, fill_value=0)
    lv_df = pd.DataFrame(output_dict, index=mass_labels)
    lv_df = lv_df.loc[(lv_df.sum(axis=1) > 0).cumsum() > 0]
    mda.ChartUtils.log_and_save_df("csv", output_name_lv, output_prefix, lv_df)
    mda.ChartUtils.plot_bar(
        lv_df,
        title=f'{chart_title_prefix} Launches vs. Payload Mass by Launch Vehicle',
        subtitle=subtitle,
        x_label='Total Payload Mass (kg)',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name_lv}.png',
        color_map=mda.ChartUtils.color_sequence_5_12 + ['#757575', '#434343'],
        bargap=0.1,
    )

    # --- Chart by orbit ---
    orbit_order = [o for o in WESTERN_ORBIT_ORDER if o in launch_df['Launch_Category'].values]
    output_dict = {}
    for orbit in orbit_order:
        orbit_launches = launch_df[launch_df['Launch_Category'] == orbit]
        binned = pd.cut(orbit_launches['Payload_Mass'], bins=bins, labels=mass_labels, include_lowest=True)
        output_dict[orbit] = binned.value_counts().reindex(mass_labels, fill_value=0)
    orbit_df = pd.DataFrame(output_dict, index=mass_labels)
    orbit_df = orbit_df.loc[(orbit_df.sum(axis=1) > 0).cumsum() > 0]
    mda.ChartUtils.log_and_save_df("csv", output_name_orbit, output_prefix, orbit_df)
    mda.ChartUtils.plot_bar(
        orbit_df,
        title=f'{chart_title_prefix} Launches vs. Payload Mass by Orbit',
        subtitle=subtitle,
        x_label='Total Payload Mass (kg)',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name_orbit}.png',
        color_map=mda.ChartUtils.western_orbit_color_map,
        bargap=0.1,
    )


# ---------------------------------------------------------------------------
# Shared helpers for all western charts
# ---------------------------------------------------------------------------

WESTERN_ORBIT_ORDER = ['LEO', 'MEO', 'GEO', 'GTO', 'HEO', 'Unknown']

WESTERN_GOVMIL_CATEGORY_ORDER = [
    'ISS',
    'Military LEO',
    'Military non-LEO',
    'Government LEO',
    'Government non-LEO',
]

WESTERN_NET_CATEGORY_ORDER = COMMERCIAL_WESTERN_CATEGORY_ORDER + WESTERN_GOVMIL_CATEGORY_ORDER


def _filter_western_govmil(df):
    """Return western non-commercial payload rows (Defense, Civil, Academic)."""
    return df[
        (df['Type'].str.strip().str.startswith('P', na=False)) &
        (~df['Launch_State'].isin(['CN', 'RU', 'SU'])) &
        (df['Payload_Class'] != 'B') &
        df['Payload_Class'].notna() &
        (df['Payload_Class'].astype(str).str.strip() != '')
    ].copy()


def _filter_western_all(df):
    """Return all western payload rows regardless of class."""
    return df[
        (df['Type'].str.strip().str.startswith('P', na=False)) &
        (~df['Launch_State'].isin(['CN', 'RU', 'SU']))
    ].copy()


def _classify_western_govmil_categories(df, orbit_col='Derived_Orbit'):
    """Classify western gov/mil payloads: ISS, Military LEO/non-LEO, Government LEO/non-LEO.

    ISS: Payload_Category == 'SS' and orbit is not HEO (captures HTV, Kounotori, ATV).
    Military: Payload_Class == 'D'.
    Government/Academic: Class C/A.
    LEO includes SSO; non-LEO includes Unknown (likely classified high orbits).
    """
    df = df.copy()
    leo_mask = df[orbit_col].isin(['LEO', 'SSO'])
    mil_mask = df['Payload_Class'].astype(str).str.strip() == 'D'
    _LUNAR_PROGRAMS = ['Artemis', 'Lunar Gateway', 'Lunar Reconnaissance']
    iss_mask = (
        df['Payload_Category'].astype(str).str.strip().str.contains('SS', na=False) &
        (df[orbit_col] != 'HEO') &
        ~df['Payload_Program'].astype(str).str.strip().isin(_LUNAR_PROGRAMS)
    )

    df['Western_GovMil_Category'] = 'Government non-LEO'
    df.loc[leo_mask, 'Western_GovMil_Category'] = 'Government LEO'
    df.loc[mil_mask & ~leo_mask, 'Western_GovMil_Category'] = 'Military non-LEO'
    df.loc[mil_mask & leo_mask, 'Western_GovMil_Category'] = 'Military LEO'
    df.loc[iss_mask, 'Western_GovMil_Category'] = 'ISS'
    return df


def _get_classified_western_govmil_satcat(dataset):
    df = _filter_western_govmil(dataset.satcat.df.copy())
    df = _load_psatcat_orbit(df, dataset.launch.df)
    df = _classify_western_govmil_categories(df)
    return _apply_effective_mass(df)


def _classify_western_all_categories(df, orbit_col='Derived_Orbit'):
    """Classify all western payloads: commercial categories for B-class, govmil for others."""
    df = df.copy()
    df['Western_Category'] = 'Unknown'
    commercial_mask = df['Payload_Class'].astype(str).str.strip() == 'B'

    if commercial_mask.any():
        comm_df = _classify_commercial_western_categories(df[commercial_mask].copy(), orbit_col)
        df.loc[commercial_mask, 'Western_Category'] = comm_df['Commercial_Western_Category'].values

    if (~commercial_mask).any():
        gm_df = _classify_western_govmil_categories(df[~commercial_mask].copy(), orbit_col)
        df.loc[~commercial_mask, 'Western_Category'] = gm_df['Western_GovMil_Category'].values

    return df


def _get_classified_western_all_satcat(dataset):
    df = _filter_western_all(dataset.satcat.df.copy())
    df = _load_psatcat_orbit(df, dataset.launch.df)
    df = _classify_western_all_categories(df)
    return _apply_effective_mass(df)


def _dominant_category_by_mass(satcat_df, category_col):
    """For each launch, pick the category of the highest Effective_Mass payload."""
    idx = satcat_df.groupby('Launch_Tag')['Effective_Mass'].idxmax()
    return (
        satcat_df.loc[idx, ['Launch_Tag', category_col]]
        .rename(columns={category_col: 'Launch_Category'})
        .reset_index(drop=True)
    )



def _bar_and_pies(
    launch_df,
    category_order,
    output_prefix,
    output_name,
    chart_title_prefix,
    date_updated,
    color_map,
    mass_step_size_kg=1000,
    max_display_mass_kg=20000,
    mass_suffix='t',
    mass_divisor=1000,
    bargap=0.1,
    date_range=None,
    sort_pie=True,
):
    """Generate bar chart + count pie + mass pie from a per-launch dataframe."""
    date_range_note = f' - {date_range}' if date_range else ''
    subtitle = f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell - Data Cutoff: {date_updated}{date_range_note}'

    count_by_cat = launch_df.groupby('Launch_Category').size().reindex(category_order, fill_value=0)
    mass_by_cat = (launch_df.groupby('Launch_Category')['Payload_Mass'].sum() / mass_divisor
                   ).reindex(category_order, fill_value=0)
    count_by_cat = count_by_cat[count_by_cat > 0]
    mass_by_cat  = mass_by_cat[mass_by_cat > 0]

    mda.ChartUtils.log_and_save_df('csv', f'{output_name}_count_pie', output_prefix,
                                   count_by_cat.rename('Count').reset_index())
    mda.ChartUtils.log_and_save_df('csv', f'{output_name}_mass_pie', output_prefix,
                                   mass_by_cat.rename(f'Mass_{mass_suffix}').reset_index())
    mda.ChartUtils.plot_pie(
        values=count_by_cat.values,
        names=count_by_cat.index.tolist(),
        title=f'{chart_title_prefix} Launch Count by Category',
        subtitle=subtitle,
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}_count_pie.png',
        color_map=color_map,
        sort=sort_pie,
    )
    mda.ChartUtils.plot_pie(
        values=mass_by_cat.values,
        names=mass_by_cat.index.tolist(),
        title=f'{chart_title_prefix} Total Launched Mass by Category',
        subtitle=subtitle,
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}_mass_pie.png',
        color_map=color_map,
        sort=sort_pie,
    )

    bins = list(range(0, max_display_mass_kg + mass_step_size_kg, mass_step_size_kg))
    mass_labels = [f"{int(bins[i]/mass_divisor)}-{int(bins[i+1]/mass_divisor)}{mass_suffix}"
                   for i in range(len(bins) - 1)]
    bar_df = launch_df[launch_df['Payload_Mass'] <= max_display_mass_kg]
    output_dict = {}
    for cat in category_order:
        cat_df = bar_df[bar_df['Launch_Category'] == cat]
        binned = pd.cut(cat_df['Payload_Mass'], bins=bins, labels=mass_labels, include_lowest=True)
        output_dict[cat] = binned.value_counts().reindex(mass_labels, fill_value=0)
    bar_out = pd.DataFrame(output_dict, index=mass_labels)
    last_nonzero = (bar_out.sum(axis=1) > 0).cumsum()
    bar_out = bar_out.loc[last_nonzero > 0]
    mda.ChartUtils.log_and_save_df('csv', output_name, output_prefix, bar_out)
    mda.ChartUtils.plot_bar(
        bar_out,
        title=f'{chart_title_prefix} Launches vs. Payload Mass by Category',
        subtitle=subtitle,
        x_label=f'Payload Mass Range ({mass_suffix})',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        color_map=color_map,
        bargap=bargap,
    )


def _build_launch_df(satcat_df, category_col, dataset, start_year=None, end_year=None):
    """Assemble per-launch dataframe with dominant category and total effective mass."""
    launch_category = _dominant_category_by_mass(satcat_df, category_col)
    mass_by_launch = _mass_per_launch(satcat_df)

    launch_df = dataset.launch.df[['Launch_Tag', 'Launch_Date', 'LV_Type', 'Mission']].copy()
    launch_df = launch_df.merge(launch_category, on='Launch_Tag', how='inner')
    launch_df['Payload_Mass'] = launch_df['Launch_Tag'].map(mass_by_launch).fillna(0)
    launch_df = launch_df[launch_df['Payload_Mass'] > 0].sort_values('Launch_Date')
    if start_year is not None:
        launch_df = launch_df[launch_df['Launch_Date'].dt.year >= start_year]
    if end_year is not None:
        launch_df = launch_df[launch_df['Launch_Date'].dt.year <= end_year]
    return launch_df


# ---------------------------------------------------------------------------
# Western all launches by orbit
# ---------------------------------------------------------------------------

def western_launches_vs_mass_by_orbit(
    chart_title_prefix='Western',
    output_prefix='western',
    mass_step_size_kg=1000,
    max_display_mass_kg=20000,
    start_year=None,
    end_year=None,
    date_range=None,
):
    """Bar chart + pies: all western launches vs payload mass, series = orbit."""
    output_name = f'{output_prefix}_launches_vs_mass_by_orbit'
    dataset = mda.McdowellDataset('./datasets')

    satcat_df = _filter_western_all(dataset.satcat.df.copy())
    satcat_df = _load_psatcat_orbit(satcat_df, dataset.launch.df)
    satcat_df = _apply_effective_mass(satcat_df)
    satcat_df['Launch_Orbit'] = satcat_df['Derived_Orbit']

    launch_df = _build_launch_df(satcat_df, 'Launch_Orbit', dataset, start_year, end_year)
    mda.ChartUtils.log_and_save_df('dataframe', output_name, output_prefix,
                                   launch_df[['Launch_Tag', 'Launch_Date', 'LV_Type', 'Mission',
                                              'Payload_Mass', 'Launch_Category']])
    _bar_and_pies(launch_df, WESTERN_ORBIT_ORDER, output_prefix, output_name,
                  chart_title_prefix, dataset.date_updated,
                  mda.ChartUtils.western_orbit_color_map,
                  mass_step_size_kg, max_display_mass_kg,
                  date_range=date_range)


# ---------------------------------------------------------------------------
# Western gov/mil charts
# ---------------------------------------------------------------------------

def western_govmil_payload_categories_pie(
    chart_title_prefix='Western Gov/Mil',
    output_prefix='western',
    date_range=None,
):
    """Pie charts (count + mass) for western gov/mil payloads by category."""
    dataset = mda.McdowellDataset('./datasets')
    df = _get_classified_western_govmil_satcat(dataset)
    date_range_note = f' - {date_range}' if date_range else ''
    subtitle = f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}{date_range_note}'

    count_by_cat = df.groupby('Western_GovMil_Category').size().reindex(WESTERN_GOVMIL_CATEGORY_ORDER, fill_value=0)
    mass_by_cat  = (df.groupby('Western_GovMil_Category')['Effective_Mass'].sum() / 1000
                    ).reindex(WESTERN_GOVMIL_CATEGORY_ORDER, fill_value=0)
    count_by_cat = count_by_cat[count_by_cat > 0]
    mass_by_cat  = mass_by_cat[mass_by_cat > 0]

    out_count = f'{output_prefix}_govmil_payload_category_count_pie'
    out_mass  = f'{output_prefix}_govmil_payload_category_mass_pie'
    mda.ChartUtils.log_and_save_df('csv', out_count, output_prefix,
                                   count_by_cat.rename('Count').reset_index())
    mda.ChartUtils.log_and_save_df('csv', out_mass, output_prefix,
                                   mass_by_cat.rename('Mass_t').reset_index())
    mda.ChartUtils.plot_pie(
        values=count_by_cat.values, names=count_by_cat.index.tolist(),
        title=f'{chart_title_prefix} Payload Count by Category', subtitle=subtitle,
        output_path=f'examples/outputs/chart/{output_prefix}/{out_count}.png',
        color_map=mda.ChartUtils.western_govmil_category_color_map,
        sort=False,
    )
    mda.ChartUtils.plot_pie(
        values=mass_by_cat.values, names=mass_by_cat.index.tolist(),
        title=f'{chart_title_prefix} Total Launched Mass by Category', subtitle=subtitle,
        output_path=f'examples/outputs/chart/{output_prefix}/{out_mass}.png',
        color_map=mda.ChartUtils.western_govmil_category_color_map,
        sort=False,
    )


def western_govmil_launches_vs_mass_by_category(
    chart_title_prefix='Western Gov/Mil',
    output_prefix='western',
    mass_step_size_kg=1000,
    max_display_mass_kg=20000,
    start_year=None,
    end_year=None,
    date_range=None,
):
    """Bar chart + pies: western gov/mil launches vs payload mass by category."""
    output_name = f'{output_prefix}_govmil_launches_vs_mass_by_category'
    dataset = mda.McdowellDataset('./datasets')

    satcat_df = _get_classified_western_govmil_satcat(dataset)
    launch_df = _build_launch_df(satcat_df, 'Western_GovMil_Category', dataset, start_year, end_year)
    mda.ChartUtils.log_and_save_df('dataframe', output_name, output_prefix,
                                   launch_df[['Launch_Tag', 'Launch_Date', 'LV_Type', 'Mission',
                                              'Payload_Mass', 'Launch_Category']])
    _bar_and_pies(launch_df, WESTERN_GOVMIL_CATEGORY_ORDER, output_prefix, output_name,
                  chart_title_prefix, dataset.date_updated,
                  mda.ChartUtils.western_govmil_category_color_map,
                  mass_step_size_kg, max_display_mass_kg,
                  date_range=date_range, sort_pie=False)


# ---------------------------------------------------------------------------
# Net western (all launches) charts
# ---------------------------------------------------------------------------

def western_net_by_orbit_pie(
    chart_title_prefix='Western',
    output_prefix='western',
    start_year=None,
    end_year=None,
    date_range=None,
):
    """Pie charts (launch count + mass) for all western launches by orbit."""
    dataset = mda.McdowellDataset('./datasets')

    satcat_df = _filter_western_all(dataset.satcat.df.copy())
    satcat_df = _load_psatcat_orbit(satcat_df, dataset.launch.df)
    satcat_df = _apply_effective_mass(satcat_df)
    satcat_df['Launch_Orbit'] = satcat_df['Derived_Orbit']

    launch_df = _build_launch_df(satcat_df, 'Launch_Orbit', dataset, start_year, end_year)

    date_range_note = f' - {date_range}' if date_range else ''
    subtitle = f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}{date_range_note}'
    out_count = f'{output_prefix}_net_launches_by_orbit_count_pie'
    out_mass  = f'{output_prefix}_net_launches_by_orbit_mass_pie'

    count_by_orbit = launch_df.groupby('Launch_Category').size().reindex(WESTERN_ORBIT_ORDER, fill_value=0)
    mass_by_orbit  = (launch_df.groupby('Launch_Category')['Payload_Mass'].sum() / 1000
                      ).reindex(WESTERN_ORBIT_ORDER, fill_value=0)
    count_by_orbit = count_by_orbit[count_by_orbit > 0]
    mass_by_orbit  = mass_by_orbit[mass_by_orbit > 0]

    mda.ChartUtils.log_and_save_df('csv', out_count, output_prefix,
                                   count_by_orbit.rename('Count').reset_index())
    mda.ChartUtils.log_and_save_df('csv', out_mass, output_prefix,
                                   mass_by_orbit.rename('Mass_t').reset_index())
    mda.ChartUtils.plot_pie(
        values=count_by_orbit.values, names=count_by_orbit.index.tolist(),
        title=f'{chart_title_prefix} Launch Count by Orbit', subtitle=subtitle,
        output_path=f'examples/outputs/chart/{output_prefix}/{out_count}.png',
        color_map=mda.ChartUtils.western_orbit_color_map,
    )
    mda.ChartUtils.plot_pie(
        values=mass_by_orbit.values, names=mass_by_orbit.index.tolist(),
        title=f'{chart_title_prefix} Total Launched Mass by Orbit (tonnes)', subtitle=subtitle,
        output_path=f'examples/outputs/chart/{output_prefix}/{out_mass}.png',
        color_map=mda.ChartUtils.western_orbit_color_map,
    )


def western_net_launches_vs_mass_by_category(
    chart_title_prefix='Western',
    output_prefix='western',
    mass_step_size_kg=1000,
    max_display_mass_kg=20000,
    start_year=None,
    end_year=None,
    date_range=None,
):
    """Bar chart + pies: all western launches vs payload mass by combined category."""
    output_name = f'{output_prefix}_net_launches_vs_mass_by_category'
    dataset = mda.McdowellDataset('./datasets')

    satcat_df = _get_classified_western_all_satcat(dataset)
    launch_df = _build_launch_df(satcat_df, 'Western_Category', dataset, start_year, end_year)
    mda.ChartUtils.log_and_save_df('dataframe', output_name, output_prefix,
                                   launch_df[['Launch_Tag', 'Launch_Date', 'LV_Type', 'Mission',
                                              'Payload_Mass', 'Launch_Category']])
    _bar_and_pies(launch_df, WESTERN_NET_CATEGORY_ORDER, output_prefix, output_name,
                  chart_title_prefix, dataset.date_updated,
                  mda.ChartUtils.western_net_category_color_map,
                  mass_step_size_kg, max_display_mass_kg,
                  date_range=date_range)
