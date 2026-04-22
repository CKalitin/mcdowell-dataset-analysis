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

_LAUNCH_STATE_NAMES = {
    'US':   'United States',
    'GUF':  'France',
    'IN':   'India',
    'J':    'Japan',
    'NZ':   'New Zealand',
    'KR':   'South Korea',
    'IL':   'Israel',
    'AU':   'Australia',
    'KE':   'Kenya',
    'KI':   'Kiribati',
    'ESCN': 'Spain',
    'TTPI': 'Marshall Islands',
    'DZ':   'Algeria',
    'IR':   'Iran',
    'KP':   'North Korea',
}

WESTERN_ORBIT_ORDER = ['LEO', 'SSO', 'MEO', 'GTO', 'GEO', 'HEO', 'BEO', 'Unknown']

WESTERN_GOVMIL_CATEGORY_ORDER = ['ISS', 'Military LEO', 'Military non-LEO', 'Government LEO', 'Government non-LEO']

WESTERN_NET_CATEGORY_ORDER = [
    'Starlink', 'LEO Constellation', 'GEO/MEO Constellation',
    'Small Sat Rideshare', 'Small Sat',
    'Commercial LEO/SSO/MEO', 'Commercial GTO/GEO', 'Capsule/Cargo', 'High-Energy',
    'ISS', 'Military LEO', 'Military non-LEO', 'Government LEO', 'Government non-LEO',
]

_OWNER_CONSOLIDATION = {
    'PLAN':   'Planet Labs',
    'PLABS':  'Planet Labs',
    'PLABST': 'Planet Labs',
}

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
        (~df["Launch_State"].isin(["CN", "RU", "SU", "IR", "KP"])) &
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


def western_launches_vs_mass(
    chart_title_prefix,
    output_prefix,
    output_name,
    data_filter='all',
    group_by='orbit',
    top_n=None,
    category_order=None,
    color_map=None,
    min_mass_kg=0,
    max_mass_kg=20000,
    mass_step_size_kg=1000,
    include_pies=False,
    pies_only=False,
    sort_pie=True,
    start_year=None,
    end_year=None,
    date_range=None,
    save_raw_df=False,
):
    """Generic bar chart (+ optional pies): western launches vs payload mass.

    Args:
        chart_title_prefix (str): Prefix for chart titles.
        output_prefix (str): Output folder/file prefix.
        output_name (str): Base filename stem. Pies append _count_pie/_mass_pie.
        data_filter (str): 'all', 'commercial', 'govmil', 'net'.
        group_by (str): 'orbit', 'lv', or 'category'.
        top_n (int|None): For group_by='lv': top N LVs by launch count, rest -> 'Other'.
        category_order (list|None): Fixed series order for 'category'/'orbit' modes.
        color_map (dict|list|None): Colour map or sequence passed to plot functions.
        min_mass_kg (int): Lower mass bound. Default 0.
        max_mass_kg (int): Upper mass cap — launches above this are excluded. Default 20000.
        mass_step_size_kg (int): Bin width in kg. Default 1000.
        include_pies (bool): Also generate launch-count and total-mass pie charts.
        pies_only (bool): Skip bar chart; only generate pies (implies include_pies).
        sort_pie (bool): Sort pie slices by value. Default True.
        start_year (int|None): Inclusive start year filter.
        end_year (int|None): Inclusive end year filter.
        date_range (str|None): Date range label for chart subtitle.
        save_raw_df (bool): Save per-launch raw dataframe with mass bin columns.
    """
    dataset = mda.McdowellDataset('./datasets')

    if group_by == 'lv':
        if data_filter == 'commercial':
            satcat_df = _get_classified_cw_satcat(dataset)
        elif data_filter == 'govmil':
            satcat_df = _get_classified_western_govmil_satcat(dataset)
        else:
            satcat_df = _filter_western_all(dataset.satcat.df.copy())
            satcat_df = _apply_effective_mass(satcat_df)
        mass_by_launch = _mass_per_launch(satcat_df)
        launch_df = dataset.launch.df[['Launch_Tag', 'Launch_Date', 'Launch_Vehicle_Simplified', 'Mission']].copy()
        launch_df['Payload_Mass'] = launch_df['Launch_Tag'].map(mass_by_launch).fillna(0)
        launch_df = launch_df[launch_df['Payload_Mass'] > 0].sort_values('Launch_Date')
        if start_year is not None:
            launch_df = launch_df[launch_df['Launch_Date'].dt.year >= start_year]
        if end_year is not None:
            launch_df = launch_df[launch_df['Launch_Date'].dt.year <= end_year]
        launch_df = launch_df[
            (launch_df['Payload_Mass'] >= min_mass_kg) &
            (launch_df['Payload_Mass'] <= max_mass_kg)
        ]
        lv_counts = launch_df.groupby('Launch_Vehicle_Simplified').size().sort_values(ascending=False)
        top_lvs = lv_counts.index[:top_n].tolist() if top_n else lv_counts.index.tolist()
        has_other = top_n is not None and (~launch_df['Launch_Vehicle_Simplified'].isin(top_lvs)).any()
        launch_df['LV_Display'] = launch_df['Launch_Vehicle_Simplified'].where(
            launch_df['Launch_Vehicle_Simplified'].isin(top_lvs), other='Other'
        )
        category_order = top_lvs + (['Other'] if has_other else [])
        group_col = 'LV_Display'

    elif group_by == 'orbit':
        satcat_df = _filter_western_all(dataset.satcat.df.copy())
        satcat_df = _load_psatcat_orbit(satcat_df, dataset.launch.df)
        satcat_df = _apply_effective_mass(satcat_df)
        satcat_df['Launch_Orbit'] = satcat_df['Derived_Orbit']
        launch_df = _build_launch_df(satcat_df, 'Launch_Orbit', dataset, start_year, end_year)
        launch_df = launch_df[
            (launch_df['Payload_Mass'] >= min_mass_kg) &
            (launch_df['Payload_Mass'] <= max_mass_kg)
        ]
        if category_order is None:
            category_order = WESTERN_ORBIT_ORDER
        group_col = 'Launch_Category'

    elif group_by == 'category':
        if data_filter == 'commercial':
            satcat_df = _get_classified_cw_satcat(dataset)
            launch_category = _dominant_launch_category(satcat_df)
            mass_by_launch = _mass_per_launch(satcat_df)
            launch_df = dataset.launch.df[['Launch_Tag', 'Launch_Date', 'Launch_Vehicle_Simplified', 'Mission']].copy()
            launch_df = launch_df.merge(launch_category, on='Launch_Tag', how='inner')
            launch_df['Payload_Mass'] = launch_df['Launch_Tag'].map(mass_by_launch).fillna(0)
            launch_df = launch_df[launch_df['Payload_Mass'] > 0].sort_values('Launch_Date')
            if start_year is not None:
                launch_df = launch_df[launch_df['Launch_Date'].dt.year >= start_year]
            if end_year is not None:
                launch_df = launch_df[launch_df['Launch_Date'].dt.year <= end_year]
            if category_order is None:
                category_order = COMMERCIAL_WESTERN_CATEGORY_ORDER
        elif data_filter == 'govmil':
            satcat_df = _get_classified_western_govmil_satcat(dataset)
            launch_df = _build_launch_df(satcat_df, 'Western_GovMil_Category', dataset, start_year, end_year)
            if category_order is None:
                category_order = WESTERN_GOVMIL_CATEGORY_ORDER
        else:  # 'net' or 'all'
            satcat_df = _get_classified_western_all_satcat(dataset)
            launch_df = _build_launch_df(satcat_df, 'Western_Category', dataset, start_year, end_year)
            if category_order is None:
                category_order = WESTERN_NET_CATEGORY_ORDER
        launch_df = launch_df[
            (launch_df['Payload_Mass'] >= min_mass_kg) &
            (launch_df['Payload_Mass'] <= max_mass_kg)
        ]
        group_col = 'Launch_Category'

    else:
        raise ValueError(f"Unknown group_by: {group_by!r}. Expected 'orbit', 'lv', or 'category'.")

    mass_suffix = 't' if mass_step_size_kg >= 1000 else 'kg'
    mass_divisor = 1000 if mass_step_size_kg >= 1000 else 1
    bins = list(range(min_mass_kg, max_mass_kg + mass_step_size_kg, mass_step_size_kg))
    mass_labels = [
        f"{int(bins[i]/mass_divisor)}-{int(bins[i+1]/mass_divisor)}{mass_suffix}"
        for i in range(len(bins) - 1)
    ]
    group_label = {'orbit': 'Orbit', 'lv': 'Launch Vehicle', 'category': 'Category'}[group_by]
    date_range_note = f' - {date_range}' if date_range else ''
    subtitle = (
        f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell'
        f' - Data Cutoff: {dataset.date_updated}{date_range_note}'
    )

    if save_raw_df:
        raw_cols = ['Launch_Tag', 'Launch_Date', 'Launch_Vehicle_Simplified', 'Mission', 'Payload_Mass', group_col]
        raw_df = launch_df[raw_cols].copy()
        raw_df['Mass_Bin'] = pd.cut(
            raw_df['Payload_Mass'], bins=bins, labels=mass_labels, include_lowest=True
        )
        if mass_step_size_kg != 1000:
            bins_1t = list(range(min_mass_kg, max_mass_kg + 1000, 1000))
            labels_1t = [
                f"{bins_1t[i]//1000}-{bins_1t[i+1]//1000}t"
                for i in range(len(bins_1t) - 1)
            ]
            raw_df['Mass_Bin_1t'] = pd.cut(
                raw_df['Payload_Mass'], bins=bins_1t, labels=labels_1t, include_lowest=True
            )
        mda.ChartUtils.log_and_save_df('dataframe', output_name, output_prefix, raw_df)

    if include_pies or pies_only:
        count_by = launch_df.groupby(group_col).size().reindex(category_order, fill_value=0)
        mass_by = (
            launch_df.groupby(group_col)['Payload_Mass'].sum() / 1000
        ).reindex(category_order, fill_value=0)
        count_by = count_by[count_by > 0]
        mass_by = mass_by[mass_by > 0]
        mda.ChartUtils.log_and_save_df('csv', f'{output_name}_count_pie', output_prefix,
                                       count_by.rename('Count').reset_index())
        mda.ChartUtils.log_and_save_df('csv', f'{output_name}_mass_pie', output_prefix,
                                       mass_by.rename('Mass_t').reset_index())
        mda.ChartUtils.plot_pie(
            values=count_by.values, names=count_by.index.tolist(),
            title=f'{chart_title_prefix} Launch Count by {group_label}',
            subtitle=subtitle,
            output_path=f'examples/outputs/chart/{output_prefix}/{output_name}_count_pie.png',
            color_map=color_map, sort=sort_pie,
        )
        mda.ChartUtils.plot_pie(
            values=mass_by.values, names=mass_by.index.tolist(),
            title=f'{chart_title_prefix} Total Launched Mass by {group_label}',
            subtitle=subtitle,
            output_path=f'examples/outputs/chart/{output_prefix}/{output_name}_mass_pie.png',
            color_map=color_map, sort=sort_pie,
        )

    if pies_only:
        return

    output_dict = {}
    for cat in category_order:
        cat_df = launch_df[launch_df[group_col] == cat]
        binned = pd.cut(cat_df['Payload_Mass'], bins=bins, labels=mass_labels, include_lowest=True)
        output_dict[cat] = binned.value_counts().reindex(mass_labels, fill_value=0)
    output_df = pd.DataFrame(output_dict, index=mass_labels)
    last_nonzero = (output_df.sum(axis=1) > 0).cumsum()
    output_df = output_df.loc[last_nonzero > 0]
    mda.ChartUtils.log_and_save_df('csv', output_name, output_prefix, output_df)
    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Launches vs. Payload Mass by {group_label}',
        subtitle=subtitle,
        x_label=f'Total Payload Mass ({mass_suffix})',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        color_map=color_map,
        bargap=0.1,
    )


def western_payload_pie(
    chart_title_prefix,
    output_prefix,
    output_name_count,
    output_name_mass,
    data_filter='commercial',
    category_order=None,
    color_map=None,
    sort=True,
    start_year=None,
    end_year=None,
    date_range=None,
):
    """Payload-level pie charts (count + mass) for western payloads by category.

    Counts individual payloads (satcat rows), not launches.

    Args:
        chart_title_prefix (str): Prefix for chart titles.
        output_prefix (str): Output folder/file prefix.
        output_name_count (str): Filename stem for the count pie.
        output_name_mass (str): Filename stem for the mass pie.
        data_filter (str): 'commercial' or 'govmil'.
        category_order (list|None): Fixed category order. Auto-derived if None.
        color_map (dict|list|None): Colour map or sequence.
        sort (bool): Sort pie slices by value. Default True.
        start_year (int|None): Inclusive start year filter.
        end_year (int|None): Inclusive end year filter.
        date_range (str|None): Date range label for chart subtitle.
    """
    dataset = mda.McdowellDataset('./datasets')

    if data_filter == 'commercial':
        df = _get_classified_cw_satcat(dataset)
        cat_col = 'Commercial_Western_Category'
        mass_col = 'Mass'
        if category_order is None:
            category_order = COMMERCIAL_WESTERN_CATEGORY_ORDER
    elif data_filter == 'govmil':
        df = _get_classified_western_govmil_satcat(dataset)
        cat_col = 'Western_GovMil_Category'
        mass_col = 'Effective_Mass'
        if category_order is None:
            category_order = WESTERN_GOVMIL_CATEGORY_ORDER
    else:
        raise ValueError(f"Unsupported data_filter for western_payload_pie: {data_filter!r}")

    if start_year is not None:
        df = df[df['Launch_Date'].dt.year >= start_year]
    if end_year is not None:
        df = df[df['Launch_Date'].dt.year <= end_year]

    count_by_cat = df.groupby(cat_col).size().reindex(category_order, fill_value=0)
    mass_by_cat = (df.groupby(cat_col)[mass_col].sum() / 1000).reindex(category_order, fill_value=0)
    count_by_cat = count_by_cat[count_by_cat > 0]
    mass_by_cat = mass_by_cat[mass_by_cat > 0]

    date_range_note = f' - {date_range}' if date_range else ''
    subtitle = (
        f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell'
        f' - Data Cutoff: {dataset.date_updated}{date_range_note}'
    )
    mda.ChartUtils.log_and_save_df('csv', output_name_count, output_prefix,
                                   count_by_cat.rename('Count').reset_index())
    mda.ChartUtils.log_and_save_df('csv', output_name_mass, output_prefix,
                                   mass_by_cat.rename('Mass_t').reset_index())
    mda.ChartUtils.plot_pie(
        values=count_by_cat.values, names=count_by_cat.index.tolist(),
        title=f'{chart_title_prefix} Payload Count by Category',
        subtitle=subtitle,
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name_count}.png',
        color_map=color_map, sort=sort,
    )
    mda.ChartUtils.plot_pie(
        values=mass_by_cat.values, names=mass_by_cat.index.tolist(),
        title=f'{chart_title_prefix} Total Launched Mass by Category',
        subtitle=subtitle,
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name_mass}.png',
        color_map=color_map, sort=sort,
    )


def western_small_sat_by_category(
    chart_title_prefix='Western',
    output_prefix='western',
    output_name='western_small_sat_by_year',
    max_mass_kg=600,
    start_year=None,
    end_year=None,
    date_range=None,
    color_map=None,
    include_mass_dist=False,
    mass_dist_output_name='western_small_sat_mass_dist',
    mass_dist_start_year=None,
    mass_dist_end_year=None,
    mass_dist_date_range=None,
    mass_step_size_kg=50,
    include_lv_by_year=False,
    lv_by_year_output_name='western_small_sat_by_year_by_lv',
    lv_top_n=10,
    lv_color_map=None,
    include_customer_by_year=False,
    customer_by_year_output_name='western_small_sat_by_year_by_customer',
    include_customer_mass_dist=False,
    customer_mass_dist_output_name='western_small_sat_mass_dist_by_customer',
    include_org_by_year=False,
    org_by_year_output_name='western_small_sat_by_year_by_org',
    include_org_mass_dist=False,
    org_mass_dist_output_name='western_small_sat_mass_dist_by_org',
    org_top_n=12,
    org_color_map=None,
    include_program_by_year=False,
    program_by_year_output_name='western_small_sat_by_year_by_program',
    include_program_mass_dist=False,
    program_mass_dist_output_name='western_small_sat_mass_dist_by_program',
    program_top_n=12,
    program_color_map=None,
    exclude_large_constellations=False,
    save_raw_df=False,
    raw_df_title=None,
):
    """Stacked bar of western small satellites per year by Simple_Payload_Category.

    Optionally also generates a mass distribution histogram for a secondary year range.
    """
    # Excludes megaconstellations (Starlink, OneWeb) and large government constellations
    # (SDA tranche programmes) which would dwarf genuine small sat demand signals.
    _EXCL_PREFIXES = ('Starlink', 'SDA')
    _EXCL_EXACT = {'OneWeb'}

    def _apply_excl(df):
        p = df['Payload_Program'].fillna('')
        return df[~p.str.startswith(_EXCL_PREFIXES) & ~p.isin(_EXCL_EXACT)].copy()

    dataset = mda.McdowellDataset('./datasets')
    satcat_df = _filter_western_all(dataset.satcat.df.copy())
    satcat_df = satcat_df[satcat_df['Mass'].fillna(0) <= max_mass_kg].copy()
    if exclude_large_constellations:
        satcat_df = _apply_excl(satcat_df)
    satcat_df['Year'] = satcat_df['Launch_Date'].dt.year

    if start_year is not None:
        satcat_df = satcat_df[satcat_df['Year'] >= start_year]
    if end_year is not None:
        satcat_df = satcat_df[satcat_df['Year'] <= end_year]

    if save_raw_df:
        raw_cols = ['Launch_Date', 'Launch_Vehicle_Simplified', 'Payload_Name', 'Owner', 'Mass', 'Simple_Payload_Category', 'Payload_Program', 'Launch_Tag']
        raw_out = satcat_df[[c for c in raw_cols if c in satcat_df.columns]].sort_values('Launch_Date')
        df_name = raw_df_title if raw_df_title else output_name
        mda.ChartUtils.log_and_save_df('dataframe', df_name, output_prefix, raw_out)

    cat_order = ['Observation', 'Communications', 'Science', 'Tech Demo', 'Other']
    satcat_df['Category'] = satcat_df['Simple_Payload_Category'].where(
        satcat_df['Simple_Payload_Category'].isin(cat_order), other='Other'
    ).fillna('Other')

    date_range_note = f' - {date_range}' if date_range else ''
    subtitle = (
        f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell'
        f' - Data Cutoff: {dataset.date_updated}{date_range_note}'
    )
    _color_map = color_map if color_map else mda.ChartUtils.simple_payload_category_color_map

    pivot = satcat_df.groupby(['Year', 'Category']).size().unstack(fill_value=0)
    pivot = pivot.reindex(columns=[c for c in cat_order if c in pivot.columns], fill_value=0)
    mda.ChartUtils.log_and_save_df('csv', output_name, output_prefix, pivot)
    mda.ChartUtils.plot_bar(
        pivot,
        title=f'{chart_title_prefix} Small Satellites Launched per Year by Category',
        subtitle=subtitle,
        x_label='Year',
        y_label='Number of Satellites',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        color_map=_color_map,
        bargap=0.1,
    )

    if include_mass_dist:
        dist_df = _filter_western_all(dataset.satcat.df.copy())
        dist_df = dist_df[dist_df['Mass'].fillna(0) <= max_mass_kg].copy()
        if exclude_large_constellations:
            dist_df = _apply_excl(dist_df)
        dist_df['Year'] = dist_df['Launch_Date'].dt.year
        if mass_dist_start_year is not None:
            dist_df = dist_df[dist_df['Year'] >= mass_dist_start_year]
        if mass_dist_end_year is not None:
            dist_df = dist_df[dist_df['Year'] <= mass_dist_end_year]
        dist_df['Category'] = dist_df['Simple_Payload_Category'].where(
            dist_df['Simple_Payload_Category'].isin(cat_order), other='Other'
        ).fillna('Other')

        bins = list(range(0, max_mass_kg + mass_step_size_kg, mass_step_size_kg))
        mass_labels = [f"{bins[i]}-{bins[i+1]}kg" for i in range(len(bins) - 1)]
        dist_dict = {}
        for cat in cat_order:
            cat_df = dist_df[dist_df['Category'] == cat]
            binned = pd.cut(cat_df['Mass'].fillna(0), bins=bins, labels=mass_labels, include_lowest=True)
            dist_dict[cat] = binned.value_counts().reindex(mass_labels, fill_value=0)
        dist_output_df = pd.DataFrame(dist_dict, index=mass_labels)
        last_nonzero = (dist_output_df.sum(axis=1) > 0).cumsum()
        dist_output_df = dist_output_df.loc[last_nonzero > 0]

        dist_date_range_note = f' - {mass_dist_date_range}' if mass_dist_date_range else ''
        dist_subtitle = (
            f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell'
            f' - Data Cutoff: {dataset.date_updated}{dist_date_range_note}'
        )
        mda.ChartUtils.log_and_save_df('csv', mass_dist_output_name, output_prefix, dist_output_df)
        mda.ChartUtils.plot_bar(
            dist_output_df,
            title=f'{chart_title_prefix} Small Satellite Mass Distribution by Category',
            subtitle=dist_subtitle,
            x_label='Mass (kg)',
            y_label='Number of Satellites',
            output_path=f'examples/outputs/chart/{output_prefix}/{mass_dist_output_name}.png',
            color_map=_color_map,
            bargap=0.1,
        )

    if include_lv_by_year:
        lv_counts = satcat_df['Launch_Vehicle_Simplified'].value_counts()
        top_lvs = lv_counts.nlargest(lv_top_n).index.tolist()
        satcat_df['LV'] = satcat_df['Launch_Vehicle_Simplified'].where(satcat_df['Launch_Vehicle_Simplified'].isin(top_lvs), other='Other')
        lv_order = top_lvs + (['Other'] if (satcat_df['LV'] == 'Other').any() else [])
        lv_pivot = satcat_df.groupby(['Year', 'LV']).size().unstack(fill_value=0)
        lv_pivot = lv_pivot.reindex(columns=[c for c in lv_order if c in lv_pivot.columns], fill_value=0)
        mda.ChartUtils.log_and_save_df('csv', lv_by_year_output_name, output_prefix, lv_pivot)
        _lv_seq = lv_color_map if lv_color_map else mda.ChartUtils.color_sequence_3_12 + ['#9e9e9e']
        _lv_color_map = {lv: _lv_seq[min(i, len(_lv_seq) - 2)] for i, lv in enumerate(top_lvs)}
        if 'Other' in lv_order:
            _lv_color_map['Other'] = _lv_seq[-1]
        mda.ChartUtils.plot_bar(
            lv_pivot,
            title=f'{chart_title_prefix} Small Satellites Launched per Year by Launch Vehicle',
            subtitle=subtitle,
            x_label='Year',
            y_label='Number of Satellites',
            output_path=f'examples/outputs/chart/{output_prefix}/{lv_by_year_output_name}.png',
            color_map=_lv_color_map,
            bargap=0.1,
        )

    _CUSTOMER_CLASS_MAP = {'B': 'Commercial', 'D': 'Military', 'C': 'Government', 'A': 'Government'}
    _CUSTOMER_ORDER = ['Commercial', 'Government', 'Military']

    if include_customer_by_year or include_customer_mass_dist:
        satcat_df['Customer'] = satcat_df['Payload_Class'].map(_CUSTOMER_CLASS_MAP).fillna('Other')

    if include_customer_by_year:
        cust_pivot = satcat_df.groupby(['Year', 'Customer']).size().unstack(fill_value=0)
        cust_pivot = cust_pivot.reindex(columns=[c for c in _CUSTOMER_ORDER if c in cust_pivot.columns], fill_value=0)
        mda.ChartUtils.log_and_save_df('csv', customer_by_year_output_name, output_prefix, cust_pivot)
        mda.ChartUtils.plot_bar(
            cust_pivot,
            title=f'{chart_title_prefix} Small Satellites Launched per Year by Customer',
            subtitle=subtitle,
            x_label='Year',
            y_label='Number of Satellites',
            output_path=f'examples/outputs/chart/{output_prefix}/{customer_by_year_output_name}.png',
            color_map=mda.ChartUtils.payload_operator_color_map,
            bargap=0.1,
        )

    if include_customer_mass_dist:
        cust_dist_df = _filter_western_all(dataset.satcat.df.copy())
        cust_dist_df = cust_dist_df[cust_dist_df['Mass'].fillna(0) <= max_mass_kg].copy()
        if exclude_large_constellations:
            cust_dist_df = _apply_excl(cust_dist_df)
        cust_dist_df['Year'] = cust_dist_df['Launch_Date'].dt.year
        if mass_dist_start_year is not None:
            cust_dist_df = cust_dist_df[cust_dist_df['Year'] >= mass_dist_start_year]
        if mass_dist_end_year is not None:
            cust_dist_df = cust_dist_df[cust_dist_df['Year'] <= mass_dist_end_year]
        cust_dist_df['Customer'] = cust_dist_df['Payload_Class'].map(_CUSTOMER_CLASS_MAP).fillna('Other')
        bins = list(range(0, max_mass_kg + mass_step_size_kg, mass_step_size_kg))
        mass_labels = [f"{bins[i]}-{bins[i+1]}kg" for i in range(len(bins) - 1)]
        cust_dist_dict = {}
        for cust in _CUSTOMER_ORDER:
            c_df = cust_dist_df[cust_dist_df['Customer'] == cust]
            binned = pd.cut(c_df['Mass'].fillna(0), bins=bins, labels=mass_labels, include_lowest=True)
            cust_dist_dict[cust] = binned.value_counts().reindex(mass_labels, fill_value=0)
        cust_dist_output_df = pd.DataFrame(cust_dist_dict, index=mass_labels)
        last_nonzero_c = (cust_dist_output_df.sum(axis=1) > 0).cumsum()
        cust_dist_output_df = cust_dist_output_df.loc[last_nonzero_c > 0]
        dist_date_range_note = f' - {mass_dist_date_range}' if mass_dist_date_range else ''
        cust_dist_subtitle = (
            f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell'
            f' - Data Cutoff: {dataset.date_updated}{dist_date_range_note}'
        )
        mda.ChartUtils.log_and_save_df('csv', customer_mass_dist_output_name, output_prefix, cust_dist_output_df)
        mda.ChartUtils.plot_bar(
            cust_dist_output_df,
            title=f'{chart_title_prefix} Small Satellite Mass Distribution by Customer',
            subtitle=cust_dist_subtitle,
            x_label='Mass (kg)',
            y_label='Number of Satellites',
            output_path=f'examples/outputs/chart/{output_prefix}/{customer_mass_dist_output_name}.png',
            color_map=mda.ChartUtils.payload_operator_color_map,
            bargap=0.1,
        )

    if include_org_by_year or include_org_mass_dist:
        satcat_df['Org'] = _resolve_owner_to_org(satcat_df['Owner'])
        org_counts = satcat_df['Org'].value_counts()
        top_orgs = org_counts.nlargest(org_top_n).index.tolist()
        satcat_df['OrgGroup'] = satcat_df['Org'].where(satcat_df['Org'].isin(top_orgs), other='Other')
        org_order = top_orgs + (['Other'] if (satcat_df['OrgGroup'] == 'Other').any() else [])
        _org_seq = org_color_map if org_color_map else mda.ChartUtils.color_sequence_3_12 + ['#9e9e9e']
        _org_color_map = {org: _org_seq[min(i, len(_org_seq) - 2)] for i, org in enumerate(top_orgs)}
        if 'Other' in org_order:
            _org_color_map['Other'] = _org_seq[-1]

    if include_org_by_year:
        org_pivot = satcat_df.groupby(['Year', 'OrgGroup']).size().unstack(fill_value=0)
        org_pivot = org_pivot.reindex(columns=[c for c in org_order if c in org_pivot.columns], fill_value=0)
        mda.ChartUtils.log_and_save_df('csv', org_by_year_output_name, output_prefix, org_pivot)
        mda.ChartUtils.plot_bar(
            org_pivot,
            title=f'{chart_title_prefix} Small Satellites Launched per Year by Organization',
            subtitle=subtitle,
            x_label='Year',
            y_label='Number of Satellites',
            output_path=f'examples/outputs/chart/{output_prefix}/{org_by_year_output_name}.png',
            color_map=_org_color_map,
            bargap=0.1,
        )

    if include_org_mass_dist:
        org_dist_df = _filter_western_all(dataset.satcat.df.copy())
        org_dist_df = org_dist_df[org_dist_df['Mass'].fillna(0) <= max_mass_kg].copy()
        if exclude_large_constellations:
            org_dist_df = _apply_excl(org_dist_df)
        org_dist_df['Year'] = org_dist_df['Launch_Date'].dt.year
        if mass_dist_start_year is not None:
            org_dist_df = org_dist_df[org_dist_df['Year'] >= mass_dist_start_year]
        if mass_dist_end_year is not None:
            org_dist_df = org_dist_df[org_dist_df['Year'] <= mass_dist_end_year]
        org_dist_df['Org'] = _resolve_owner_to_org(org_dist_df['Owner'])
        org_dist_df['OrgGroup'] = org_dist_df['Org'].where(org_dist_df['Org'].isin(top_orgs), other='Other')
        bins = list(range(0, max_mass_kg + mass_step_size_kg, mass_step_size_kg))
        mass_labels = [f"{bins[i]}-{bins[i+1]}kg" for i in range(len(bins) - 1)]
        org_dist_dict = {}
        for org in org_order:
            o_df = org_dist_df[org_dist_df['OrgGroup'] == org]
            binned = pd.cut(o_df['Mass'].fillna(0), bins=bins, labels=mass_labels, include_lowest=True)
            org_dist_dict[org] = binned.value_counts().reindex(mass_labels, fill_value=0)
        org_dist_output_df = pd.DataFrame(org_dist_dict, index=mass_labels)
        last_nonzero_o = (org_dist_output_df.sum(axis=1) > 0).cumsum()
        org_dist_output_df = org_dist_output_df.loc[last_nonzero_o > 0]
        dist_date_range_note = f' - {mass_dist_date_range}' if mass_dist_date_range else ''
        org_dist_subtitle = (
            f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell'
            f' - Data Cutoff: {dataset.date_updated}{dist_date_range_note}'
        )
        mda.ChartUtils.log_and_save_df('csv', org_mass_dist_output_name, output_prefix, org_dist_output_df)
        mda.ChartUtils.plot_bar(
            org_dist_output_df,
            title=f'{chart_title_prefix} Small Satellite Mass Distribution by Organization',
            subtitle=org_dist_subtitle,
            x_label='Mass (kg)',
            y_label='Number of Satellites',
            output_path=f'examples/outputs/chart/{output_prefix}/{org_mass_dist_output_name}.png',
            color_map=_org_color_map,
            bargap=0.1,
        )

    if include_program_by_year or include_program_mass_dist:
        prog_counts = satcat_df['Payload_Program'].value_counts()
        top_programs = prog_counts.nlargest(program_top_n).index.tolist()
        satcat_df['Program'] = satcat_df['Payload_Program'].where(
            satcat_df['Payload_Program'].isin(top_programs), other='Other'
        ).fillna('Other')
        prog_order = top_programs + (['Other'] if (satcat_df['Program'] == 'Other').any() else [])
        _prog_color_map = program_color_map if program_color_map else mda.ChartUtils.color_sequence_3_12 + ['#9e9e9e']

    if include_program_by_year:
        prog_pivot = satcat_df.groupby(['Year', 'Program']).size().unstack(fill_value=0)
        prog_pivot = prog_pivot.reindex(columns=[c for c in prog_order if c in prog_pivot.columns], fill_value=0)
        mda.ChartUtils.log_and_save_df('csv', program_by_year_output_name, output_prefix, prog_pivot)
        mda.ChartUtils.plot_bar(
            prog_pivot,
            title=f'{chart_title_prefix} Small Satellites Launched per Year by Program',
            subtitle=subtitle,
            x_label='Year',
            y_label='Number of Satellites',
            output_path=f'examples/outputs/chart/{output_prefix}/{program_by_year_output_name}.png',
            color_map=_prog_color_map,
            bargap=0.1,
        )

    if include_program_mass_dist:
        bins = list(range(0, max_mass_kg + mass_step_size_kg, mass_step_size_kg))
        mass_labels = [f"{bins[i]}-{bins[i+1]}kg" for i in range(len(bins) - 1)]
        prog_dist_dict = {}
        for prog in prog_order:
            p_df = satcat_df[satcat_df['Program'] == prog]
            binned = pd.cut(p_df['Mass'].fillna(0), bins=bins, labels=mass_labels, include_lowest=True)
            prog_dist_dict[prog] = binned.value_counts().reindex(mass_labels, fill_value=0)
        prog_dist_df = pd.DataFrame(prog_dist_dict, index=mass_labels)
        last_nonzero_p = (prog_dist_df.sum(axis=1) > 0).cumsum()
        prog_dist_df = prog_dist_df.loc[last_nonzero_p > 0]
        mda.ChartUtils.log_and_save_df('csv', program_mass_dist_output_name, output_prefix, prog_dist_df)
        mda.ChartUtils.plot_bar(
            prog_dist_df,
            title=f'{chart_title_prefix} Small Satellite Mass Distribution by Program',
            subtitle=subtitle,
            x_label='Mass (kg)',
            y_label='Number of Satellites',
            output_path=f'examples/outputs/chart/{output_prefix}/{program_mass_dist_output_name}.png',
            color_map=_prog_color_map,
            bargap=0.1,
        )


_ELECTRON_RL_OWNERS = frozenset({'RLABN', 'RLABLB'})

# Maps primary payload owner code → launch category for dedicated Electron missions
_ELECTRON_OWNER_CATEGORY = {
    # SAR imaging constellations
    'SYNSP': 'Constellation (SAR)', 'CAPSP': 'Constellation (SAR)', 'QPS': 'Constellation (SAR)',
    # Optical / thermal EO constellations
    'BSKG': 'Constellation (Earth obs)', 'ORORA': 'Constellation (Earth obs)',
    'PLAN': 'Constellation (Earth obs)', 'CANON': 'Constellation (Earth obs)',
    # SSA / RF-monitoring constellations
    'HE360': 'Constellation (SSA)', 'UNSEEN': 'Constellation (SSA)',
    # Spire: all variants → Earth obs (weather, maritime, ATC — observation products)
    'SPIRE': 'Constellation (Earth obs)', 'SPIRE/NSTAR': 'Constellation (Earth obs)',
    # IoT / broadband comms constellations
    'KINEIS': 'Constellation (Comms)', 'SWARM': 'Constellation (Comms)',
    'SWARMX': 'Constellation (Comms)', 'SWARNZ': 'Constellation (Comms)',
    'ESPACE': 'Constellation (Comms)', 'ESPRW': 'Constellation (Comms)',
    'ECHOAU': 'Constellation (Comms)', 'TCANL': 'Constellation (Comms)',
    'OCOSB': 'Constellation (Comms)', 'FLEET': 'Constellation (Comms)',
    'MYRI': 'Constellation (Comms)', 'GEOOPT': 'Constellation (Comms)',
    'STARA': 'Constellation (Comms)',
    # Military / DoD
    'STP': 'Military', 'AFSPC': 'Military', 'DARPA2': 'Military', 'SOCOM': 'Military',
    'AERO': 'Military', 'NROC': 'Military', 'USNA': 'Military', 'USNPS': 'Military',
    'SEDENA': 'Military', 'AFOTD4': 'Military', 'AFRL': 'Military', 'SMDC': 'Military',
    # MITLL (MIT Lincoln Lab) operates TROPICS — a NASA Earth science constellation
    'MITLL': 'Constellation (Earth obs)',
    # Government / civil / academic
    'ARC': 'Government', 'GSFC': 'Government', 'JPL': 'Government', 'LARCN': 'Government',
    'GRC': 'Government', 'ESA': 'Government', 'JAXA': 'Government', 'SNSB': 'Government',
    'KAIST': 'Government', 'ADVSP': 'Government', 'BU': 'Government',
    # Dedicated commercial one-offs (tech demos, single commercial payloads)
    'GACO': 'Commercial', 'ASTSC': 'Commercial',
    'ADIG': 'Commercial', 'OHB': 'Commercial',
}


def _classify_electron_launch(sats_df, org_short_map):
    """Return (primary_org_display, category) for one Electron launch's payload rows.

    Rideshare: >5 payloads AND >2 distinct owners AND no single owner >=80% by count.
    Rocket Lab housekeeping payloads (RLABN/RLABLB) are excluded when finding the
    primary owner so they don't mask the actual customer.
    """
    n = len(sats_df)
    owner_counts = sats_df['Owner'].fillna('?').value_counts()
    n_owners = len(owner_counts)

    # Rideshare check
    if n > 5 and n_owners > 2 and (owner_counts.iloc[0] / n) < 0.8:
        return 'Rideshare', 'Rideshare'

    # Primary owner excluding Rocket Lab housekeeping payloads
    non_rl = owner_counts[~owner_counts.index.isin(_ELECTRON_RL_OWNERS)]
    primary = non_rl.index[0] if len(non_rl) > 0 else owner_counts.index[0]

    # Category lookup: try exact code, then first segment of compound codes (e.g. ADVSP/ARC)
    category = _ELECTRON_OWNER_CATEGORY.get(primary)
    if category is None:
        base = primary.split('/')[0]
        category = _ELECTRON_OWNER_CATEGORY.get(base)
    if category is None:
        # Fall back to org class
        category = 'Other'

    # Display name
    if primary in _OWNER_CONSOLIDATION:
        org = _OWNER_CONSOLIDATION[primary]
    else:
        org = org_short_map.get(primary, primary)

    return org, category


def electron_launches(
    chart_title_prefix='Electron',
    output_prefix='electron',
    output_name_by_org='electron_launches_by_org',
    output_name_by_category='electron_launches_by_category',
    start_year=2017,
    end_year=None,
    date_range=None,
    org_top_n=10,
    org_color_map=None,
    category_color_map=None,
    save_raw_df=False,
    raw_df_title=None,
):
    """Per-year bar charts of Electron satellite launches by customer org and by mission category.

    Excludes Hypersonic / suborbital Electron flights (MACH-TB, DYNAMO-A series).
    Rideshare rule: >5 payloads, >2 distinct owners, no owner >=80% of payloads.
    """
    _CATEGORY_ORDER = [
        'Constellation (Earth obs)', 'Constellation (SAR)',
        'Constellation (SSA)', 'Constellation (Comms)',
        'Commercial', 'Rideshare', 'Government', 'Military', 'HASTE', 'Other',
    ]

    dataset = mda.McdowellDataset('./datasets')
    launch_df = dataset.launch.df
    satcat_df = dataset.satcat.df

    # All Electron launches: satellites + HASTE (Hypersonic suborbital)
    el = launch_df[
        (launch_df['Launch_Vehicle_Simplified'] == 'Electron') &
        (launch_df['Category'].str.startswith('Sat', na=False) | (launch_df['Category'] == 'Hypersonic'))
    ].copy()
    el['Year'] = el['Launch_Date'].dt.year
    if start_year:
        el = el[el['Year'] >= start_year]
    if end_year:
        el = el[el['Year'] <= end_year]

    # Load orgs lookup
    orgs = pd.read_csv('datasets/orgs.tsv', sep='\t', low_memory=False).rename(columns={'#Code': 'Code'})
    org_short = orgs.set_index('Code')['ShortName'].to_dict()

    # Payload rows for Electron launches (payload type only)
    el_sats = satcat_df[
        satcat_df['Launch_Tag'].isin(el['Launch_Tag']) &
        (satcat_df['Type'].str.strip().str.startswith('P', na=False))
    ].copy()

    # Classify each launch; HASTE launches have no satcat payload rows
    sat_tags = set(el_sats['Launch_Tag'].unique())
    haste_tags = set(el[el['Category'] == 'Hypersonic']['Launch_Tag'].unique())

    rows = []
    for tag, group in el_sats.groupby('Launch_Tag'):
        org, category = _classify_electron_launch(group, org_short)
        launch_row = el[el['Launch_Tag'] == tag].iloc[0]
        rows.append({
            'Launch_Tag': tag,
            'Year': launch_row['Year'],
            'Mission': launch_row['Mission'],
            'Launch_Date': launch_row['Launch_Date'],
            'Org': org,
            'Category': category,
            'N_Payloads': len(group),
        })
    for tag in haste_tags - sat_tags:
        launch_row = el[el['Launch_Tag'] == tag].iloc[0]
        rows.append({
            'Launch_Tag': tag,
            'Year': launch_row['Year'],
            'Mission': launch_row['Mission'],
            'Launch_Date': launch_row['Launch_Date'],
            'Org': 'HASTE',
            'Category': 'HASTE',
            'N_Payloads': 0,
        })
    launch_classified = pd.DataFrame(rows).sort_values('Launch_Date')

    date_range_note = f' - {date_range}' if date_range else ''
    subtitle = (
        f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell'
        f' - Data Cutoff: {dataset.date_updated}{date_range_note}'
    )

    if save_raw_df:
        df_name = raw_df_title if raw_df_title else output_name_by_org
        mda.ChartUtils.log_and_save_df('dataframe', df_name, output_prefix, launch_classified)

    # --- Chart 1: by customer org ---
    org_counts = launch_classified['Org'].value_counts()
    # Always keep Rideshare as its own slice; top_n for the rest
    non_rs_orgs = org_counts[org_counts.index != 'Rideshare'].nlargest(org_top_n).index.tolist()
    shown_orgs = (['Rideshare'] if 'Rideshare' in org_counts.index else []) + non_rs_orgs
    launch_classified['OrgGroup'] = launch_classified['Org'].where(
        launch_classified['Org'].isin(shown_orgs), other='Other'
    )
    if launch_classified['OrgGroup'].eq('Other').any() and 'Other' not in shown_orgs:
        shown_orgs = shown_orgs + ['Other']

    org_seq = org_color_map if org_color_map else mda.ChartUtils.color_sequence_3_12 + ['#9e9e9e']
    org_cmap = {org: org_seq[min(i, len(org_seq) - 2)] for i, org in enumerate(shown_orgs)}
    if 'Other' in shown_orgs:
        org_cmap['Other'] = org_seq[-1]

    org_pivot = launch_classified.groupby(['Year', 'OrgGroup']).size().unstack(fill_value=0)
    org_pivot = org_pivot.reindex(columns=[c for c in shown_orgs if c in org_pivot.columns], fill_value=0)
    mda.ChartUtils.log_and_save_df('csv', output_name_by_org, output_prefix, org_pivot)
    mda.ChartUtils.plot_bar(
        org_pivot,
        title=f'{chart_title_prefix} Launches per Year by Customer Organization',
        subtitle=subtitle,
        x_label='Year', y_label='Launches',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name_by_org}.png',
        color_map=org_cmap,
        bargap=0.1,
    )

    # --- Chart 2: by mission category ---
    cat_pivot = launch_classified.groupby(['Year', 'Category']).size().unstack(fill_value=0)
    cat_pivot = cat_pivot.reindex(columns=[c for c in _CATEGORY_ORDER if c in cat_pivot.columns], fill_value=0)
    _cat_cmap = category_color_map if category_color_map else mda.ChartUtils.electron_category_color_map
    mda.ChartUtils.log_and_save_df('csv', output_name_by_category, output_prefix, cat_pivot)
    mda.ChartUtils.plot_bar(
        cat_pivot,
        title=f'{chart_title_prefix} Launches per Year by Mission Category',
        subtitle=subtitle,
        x_label='Year', y_label='Launches',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name_by_category}.png',
        color_map=_cat_cmap,
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

    launch_df = dataset.launch.df[['Launch_Tag', 'Launch_Date', 'Launch_Vehicle_Simplified', 'Mission']].copy()
    launch_df = launch_df.merge(launch_category, on='Launch_Tag', how='inner')
    launch_df['Payload_Mass'] = launch_df['Launch_Tag'].map(cw_mass_by_launch).fillna(0)

    launch_df = launch_df[launch_df['Payload_Mass'] > 0].sort_values('Launch_Date')

    # Filter to Small Sat Rideshare only
    launch_df = launch_df[launch_df['Launch_Category'] == 'Small Sat Rideshare']

    if start_year is not None:
        launch_df = launch_df[launch_df['Launch_Date'].dt.year >= start_year]
    if end_year is not None:
        launch_df = launch_df[launch_df['Launch_Date'].dt.year <= end_year]

    lv_order = launch_df.groupby('Launch_Vehicle_Simplified')['Payload_Mass'].sum().sort_values(ascending=False).index.tolist()

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
        lv_df = bar_df[bar_df['Launch_Vehicle_Simplified'] == lv]
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
    count_by_lv = launch_df.groupby('Launch_Vehicle_Simplified').size().reindex(lv_order, fill_value=0)
    mass_by_lv  = (launch_df.groupby('Launch_Vehicle_Simplified')['Payload_Mass'].sum() / 1000).reindex(lv_order, fill_value=0)

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


def _filter_western_govmil(df):
    """Return western non-commercial payload rows (Defense, Civil, Academic)."""
    return df[
        (df['Type'].str.strip().str.startswith('P', na=False)) &
        (~df['Launch_State'].isin(['CN', 'RU', 'SU', 'IR', 'KP'])) &
        (df['Payload_Class'] != 'B') &
        df['Payload_Class'].notna() &
        (df['Payload_Class'].astype(str).str.strip() != '')
    ].copy()


def _filter_western_all(df):
    """Return all western payload rows regardless of class."""
    return df[
        (df['Type'].str.strip().str.startswith('P', na=False)) &
        (~df['Launch_State'].isin(['CN', 'RU', 'SU', 'IR', 'KP']))
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


def _resolve_owner_to_org(owner_series):
    """Map Owner codes to display org names using orgs.tsv ShortName + parent chain + consolidation."""
    orgs = pd.read_csv('datasets/orgs.tsv', sep='\t', low_memory=False).rename(columns={'#Code': 'Code'})
    code_to_short = orgs.set_index('Code')['ShortName'].to_dict()
    code_to_parent = orgs.set_index('Code')['Parent'].to_dict()

    def _resolve(code):
        if code in _OWNER_CONSOLIDATION:
            return _OWNER_CONSOLIDATION[code]
        parent = code_to_parent.get(code, '-')
        if parent and parent != '-':
            if parent in _OWNER_CONSOLIDATION:
                return _OWNER_CONSOLIDATION[parent]
            return code_to_short.get(parent, code_to_short.get(code, code))
        return code_to_short.get(code, code)

    return owner_series.map(_resolve)


def _dominant_category_by_mass(satcat_df, category_col):
    """For each launch, pick the category of the highest Effective_Mass payload."""
    idx = satcat_df.groupby('Launch_Tag')['Effective_Mass'].idxmax()
    return (
        satcat_df.loc[idx, ['Launch_Tag', category_col]]
        .rename(columns={category_col: 'Launch_Category'})
        .reset_index(drop=True)
    )


def _dominant_western_category_per_launch(satcat_df):
    """Like _dominant_category_by_mass on Western_Category but overrides rideshare launches.

    Transporter-style missions carry hundreds of small commercial payloads alongside
    a handful of military sats. The military sat often wins by mass alone, which
    misrepresents the mission. Apply the same rideshare detection as
    _dominant_launch_category: if > _RIDESHARE_THRESHOLD small payloads from
    >= 5 distinct programs, the launch is 'Small Sat Rideshare'.
    """
    _RIDESHARE_PROGRAM_THRESHOLD = 5
    small_mask = satcat_df['Mass'].fillna(0) <= _SMALL_SAT_MASS_KG
    small_df = satcat_df[small_mask]
    unique_programs = small_df.groupby('Launch_Tag')['Payload_Program'].nunique()
    small_count = small_df.groupby('Launch_Tag').size()
    rideshare_tags = set(
        small_count[
            (small_count > _RIDESHARE_THRESHOLD) &
            (unique_programs >= _RIDESHARE_PROGRAM_THRESHOLD)
        ].index
    )
    result = _dominant_category_by_mass(satcat_df, 'Western_Category')
    result.loc[result['Launch_Tag'].isin(rideshare_tags), 'Launch_Category'] = 'Small Sat Rideshare'
    return result



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

    launch_df = dataset.launch.df[['Launch_Tag', 'Launch_Date', 'Launch_Vehicle_Simplified', 'Mission']].copy()
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

def western_orbits_addressable_by_mass(
    chart_title_prefix='Western',
    output_prefix='western',
    leo_max_kg=20000,
    meo_max_kg=6000,
    gto_max_kg=8000,
    geo_max_kg=5000,
    heo_max_kg=None,
    beo_max_kg=None,
    min_mass_kg=0,
    max_mass_kg=5000,
    mass_step_size_kg=200,
    start_year=None,
    end_year=None,
    date_range=None,
    chart_title=None,
    save_raw_df=False,
    raw_df_title=None,
    include_type_chart=False,
    include_category_chart=False,
    include_lv_chart=False,
    lv_top_n=8,
    lv_color_map=None,
    include_country_chart=False,
    country_top_n=10,
    country_color_map=None,
):
    """Bar chart: western launches by orbit, each orbit capped at its own max payload mass."""
    output_name = f'{output_prefix}_orbits_addressable_by_mass'
    dataset = mda.McdowellDataset('./datasets')

    satcat_df = _filter_western_all(dataset.satcat.df.copy())
    satcat_df = satcat_df[~satcat_df['Payload_Program'].fillna('').str.startswith('Starlink')].copy()
    satcat_df = _load_psatcat_orbit(satcat_df, dataset.launch.df)
    satcat_df = _apply_effective_mass(satcat_df)
    satcat_df = _classify_western_all_categories(satcat_df)
    satcat_df['Launch_Orbit'] = satcat_df['Derived_Orbit']
    launch_df = _build_launch_df(satcat_df, 'Launch_Orbit', dataset, start_year, end_year)

    orbit_max = {
        'LEO': leo_max_kg,
        'MEO': meo_max_kg,
        'GTO': gto_max_kg,
        'GEO': geo_max_kg,
        'HEO': heo_max_kg if heo_max_kg is not None else gto_max_kg,
        'BEO': beo_max_kg if beo_max_kg is not None else max_mass_kg,
        'Unknown': max_mass_kg,
    }
    bins = list(range(min_mass_kg, max_mass_kg + mass_step_size_kg, mass_step_size_kg))
    mass_labels = [f"{bins[i]}-{bins[i+1]}kg" for i in range(len(bins) - 1)]
    orbit_order = [o for o in WESTERN_ORBIT_ORDER if o in launch_df['Launch_Category'].unique()]

    output_dict = {}
    qual_parts = []
    for orbit in orbit_order:
        cap = min(orbit_max.get(orbit, max_mass_kg), max_mass_kg)
        orbit_df = launch_df[
            (launch_df['Launch_Category'] == orbit) &
            (launch_df['Payload_Mass'] >= min_mass_kg) &
            (launch_df['Payload_Mass'] <= cap)
        ]
        qual_parts.append(orbit_df)
        binned = pd.cut(orbit_df['Payload_Mass'], bins=bins, labels=mass_labels, include_lowest=True)
        output_dict[orbit] = binned.value_counts().reindex(mass_labels, fill_value=0)

    qual_launch_df = pd.concat(qual_parts, ignore_index=True) if qual_parts else pd.DataFrame()

    output_df = pd.DataFrame(output_dict, index=mass_labels)
    last_nonzero = (output_df.sum(axis=1) > 0).cumsum()
    output_df = output_df.loc[last_nonzero > 0]
    mda.ChartUtils.log_and_save_df('csv', output_name, output_prefix, output_df)

    if save_raw_df and not qual_launch_df.empty:
        launch_western_cat = _dominant_western_category_per_launch(satcat_df).rename(
            columns={'Launch_Category': 'Western_Category'}
        )
        raw_df = qual_launch_df.drop_duplicates('Launch_Tag').merge(
            launch_western_cat, on='Launch_Tag', how='left'
        )
        raw_df = raw_df[['Launch_Date', 'Launch_Vehicle_Simplified', 'Mission', 'Launch_Category', 'Payload_Mass', 'Western_Category', 'Launch_Tag']]
        raw_df = raw_df.rename(columns={'Launch_Category': 'Orbit', 'Payload_Mass': 'Total_Payload_Mass_kg'})
        raw_df = raw_df.sort_values('Launch_Date')
        df_name = raw_df_title if raw_df_title else f'{output_name}_launches'
        mda.ChartUtils.log_and_save_df('dataframe', df_name, output_prefix, raw_df)

    date_range_note = f' - {date_range}' if date_range else ''
    subtitle = (
        f'Christopher Kalitin 2026 - Data Source: Jonathan McDowell'
        f' - Data Cutoff: {dataset.date_updated}{date_range_note}'
    )
    _heo = heo_max_kg if heo_max_kg is not None else gto_max_kg
    _beo = beo_max_kg if beo_max_kg is not None else max_mass_kg
    cap_note = (
        f'LEO<=>{leo_max_kg//1000}t  MEO<=>{meo_max_kg//1000}t'
        f'  GTO<=>{gto_max_kg//1000}t  GEO<=>{geo_max_kg//1000}t'
        f'  HEO<=>{_heo//1000}t  BEO<=>{_beo//1000}t'
    )
    mda.ChartUtils.plot_bar(
        output_df,
        title=(f"{chart_title} - Orbit" if chart_title else f'{chart_title_prefix} Addressable Orbits by Payload Mass'),
        subtitle=f'{subtitle}  |  {cap_note}',
        x_label='Total Payload Mass (kg)',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        color_map=mda.ChartUtils.western_orbit_color_map,
        bargap=0.1,
    )

    if include_type_chart and not qual_launch_df.empty:
        _commercial_cats = set(COMMERCIAL_WESTERN_CATEGORY_ORDER)
        def _simplified_type(cat):
            if cat in _commercial_cats:
                return 'Commercial'
            if cat in ('Military LEO', 'Military non-LEO'):
                return 'Military'
            if cat in ('Government LEO', 'Government non-LEO', 'ISS'):
                return 'Government'
            return 'Unknown'

        launch_western_cat = _dominant_western_category_per_launch(satcat_df).rename(
            columns={'Launch_Category': 'Western_Category'}
        )
        type_launch_df = qual_launch_df.merge(launch_western_cat, on='Launch_Tag', how='left')
        type_launch_df['Launch_Type'] = type_launch_df['Western_Category'].map(_simplified_type).fillna('Unknown')

        type_order = ['Commercial', 'Government', 'Military']
        type_color_map = mda.ChartUtils.payload_operator_color_map
        type_dict = {}
        for ltype in type_order:
            ltype_df = type_launch_df[type_launch_df['Launch_Type'] == ltype]
            binned = pd.cut(ltype_df['Payload_Mass'], bins=bins, labels=mass_labels, include_lowest=True)
            type_dict[ltype] = binned.value_counts().reindex(mass_labels, fill_value=0)

        type_output_df = pd.DataFrame(type_dict, index=mass_labels)
        last_nonzero_t = (type_output_df.sum(axis=1) > 0).cumsum()
        type_output_df = type_output_df.loc[last_nonzero_t > 0]
        mda.ChartUtils.log_and_save_df('csv', f'{output_name}_by_launch_type', output_prefix, type_output_df)

        type_title = (f"{chart_title} - Customer" if chart_title else f'{chart_title_prefix} Addressable Launches by Type')
        mda.ChartUtils.plot_bar(
            type_output_df,
            title=type_title,
            subtitle=f'{subtitle}  |  {cap_note}',
            x_label='Total Payload Mass (kg)',
            y_label='Number of Launches',
            output_path=f'examples/outputs/chart/{output_prefix}/{output_name}_by_launch_type.png',
            color_map=type_color_map,
            bargap=0.1,
        )

    if include_category_chart and not qual_launch_df.empty:
        launch_western_cat = _dominant_western_category_per_launch(satcat_df).rename(
            columns={'Launch_Category': 'Western_Category'}
        )
        cat_launch_df = qual_launch_df.merge(launch_western_cat, on='Launch_Tag', how='left')
        cat_order = [c for c in WESTERN_NET_CATEGORY_ORDER if c in cat_launch_df['Western_Category'].unique()]
        cat_dict = {}
        for cat in cat_order:
            cat_sub = cat_launch_df[cat_launch_df['Western_Category'] == cat]
            binned = pd.cut(cat_sub['Payload_Mass'], bins=bins, labels=mass_labels, include_lowest=True)
            cat_dict[cat] = binned.value_counts().reindex(mass_labels, fill_value=0)
        cat_output_df = pd.DataFrame(cat_dict, index=mass_labels)
        last_nonzero_c = (cat_output_df.sum(axis=1) > 0).cumsum()
        cat_output_df = cat_output_df.loc[last_nonzero_c > 0]
        mda.ChartUtils.log_and_save_df('csv', f'{output_name}_by_category', output_prefix, cat_output_df)
        cat_title = (
            f"{chart_title} - Category" if chart_title
            else f'{chart_title_prefix} Addressable Launches by Category'
        )
        mda.ChartUtils.plot_bar(
            cat_output_df,
            title=cat_title,
            subtitle=f'{subtitle}  |  {cap_note}',
            x_label='Total Payload Mass (kg)',
            y_label='Number of Launches',
            output_path=f'examples/outputs/chart/{output_prefix}/{output_name}_by_category.png',
            color_map=mda.ChartUtils.western_net_category_color_map,
            bargap=0.1,
        )

    if include_lv_chart and not qual_launch_df.empty:
        lv_counts = qual_launch_df['Launch_Vehicle_Simplified'].value_counts()
        top_lvs = lv_counts.nlargest(lv_top_n).index.tolist()
        lv_df = qual_launch_df.copy()
        lv_df['LV'] = lv_df['Launch_Vehicle_Simplified'].where(lv_df['Launch_Vehicle_Simplified'].isin(top_lvs), other='Other')
        lv_order = top_lvs + (['Other'] if (lv_df['LV'] == 'Other').any() else [])

        lv_dict = {}
        for lv in lv_order:
            lv_sub = lv_df[lv_df['LV'] == lv]
            binned = pd.cut(lv_sub['Payload_Mass'], bins=bins, labels=mass_labels, include_lowest=True)
            lv_dict[lv] = binned.value_counts().reindex(mass_labels, fill_value=0)

        lv_output_df = pd.DataFrame(lv_dict, index=mass_labels)
        last_nonzero_lv = (lv_output_df.sum(axis=1) > 0).cumsum()
        lv_output_df = lv_output_df.loc[last_nonzero_lv > 0]
        mda.ChartUtils.log_and_save_df('csv', f'{output_name}_by_lv', output_prefix, lv_output_df)

        lv_title = (f"{chart_title} - Vehicle" if chart_title else f'{chart_title_prefix} Addressable Launches by Launch Vehicle')
        _lv_color_map = lv_color_map if lv_color_map else mda.ChartUtils.color_sequence_3_8 + ['#434343']
        mda.ChartUtils.plot_bar(
            lv_output_df,
            title=lv_title,
            subtitle=f'{subtitle}  |  {cap_note}',
            x_label='Total Payload Mass (kg)',
            y_label='Number of Launches',
            output_path=f'examples/outputs/chart/{output_prefix}/{output_name}_by_lv.png',
            color_map=_lv_color_map,
            bargap=0.1,
        )

    if include_country_chart and not qual_launch_df.empty:
        country_map = satcat_df.drop_duplicates('Launch_Tag').set_index('Launch_Tag')['Launch_State']
        country_df = qual_launch_df.copy()
        country_df['Country'] = country_df['Launch_Tag'].map(country_map).map(_LAUNCH_STATE_NAMES).fillna('Unknown')
        country_counts = country_df['Country'].value_counts()
        top_countries = country_counts.nlargest(country_top_n).index.tolist()
        country_df['Country'] = country_df['Country'].where(country_df['Country'].isin(top_countries), other='Other')
        country_order = top_countries + (['Other'] if (country_df['Country'] == 'Other').any() else [])
        country_dict = {}
        for country in country_order:
            c_sub = country_df[country_df['Country'] == country]
            binned = pd.cut(c_sub['Payload_Mass'], bins=bins, labels=mass_labels, include_lowest=True)
            country_dict[country] = binned.value_counts().reindex(mass_labels, fill_value=0)
        country_output_df = pd.DataFrame(country_dict, index=mass_labels)
        last_nonzero_co = (country_output_df.sum(axis=1) > 0).cumsum()
        country_output_df = country_output_df.loc[last_nonzero_co > 0]
        mda.ChartUtils.log_and_save_df('csv', f'{output_name}_by_country', output_prefix, country_output_df)
        country_title = (f"{chart_title} - Country" if chart_title else f'{chart_title_prefix} Addressable Launches by Country')
        _country_color_map = country_color_map if country_color_map else mda.ChartUtils.color_sequence_2_8 + ['#434343']
        mda.ChartUtils.plot_bar(
            country_output_df,
            title=country_title,
            subtitle=f'{subtitle}  |  {cap_note}',
            x_label='Total Payload Mass (kg)',
            y_label='Number of Launches',
            output_path=f'examples/outputs/chart/{output_prefix}/{output_name}_by_country.png',
            color_map=_country_color_map,
            bargap=0.1,
        )
