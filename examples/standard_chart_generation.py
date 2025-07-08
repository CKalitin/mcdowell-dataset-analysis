import mcdowell_dataset_analysis as mda
import os
from datetime import datetime

def generate_launch_vehicle_charts(launch_vehicle_simplified_name, chart_title_prefix, output_prefix, mass_step_size_kg=1000, year_x_tick_step_size=1, month_x_tick_step_size=1):
    mass_suffix = "t" if mass_step_size_kg == 1000 else "kg"
    mass_divisor = 1000 if mass_step_size_kg == 1000 else 1

    launches_vs_mass_by_orbit(
        launch_vehicle_simplified_name=launch_vehicle_simplified_name,
        mass_step_size_kg=mass_step_size_kg,
        chart_title_prefix=chart_title_prefix,
        output_prefix=output_prefix,
        mass_suffix=mass_suffix,
        mass_divisor=mass_divisor,
    )

    total_mass_vs_mass_by_orbit(
        launch_vehicle_simplified_name=launch_vehicle_simplified_name,
        mass_step_size_kg=mass_step_size_kg,
        chart_title_prefix=chart_title_prefix,
        output_prefix=output_prefix,
        mass_suffix=mass_suffix,
        mass_divisor=mass_divisor,
    )

    launches_vs_mass_by_general_launch_payload_type(
        launch_vehicle_simplified_name=launch_vehicle_simplified_name,
        mass_step_size_kg=mass_step_size_kg,
        chart_title_prefix=chart_title_prefix,
        output_prefix=output_prefix,
        mass_suffix=mass_suffix,
        mass_divisor=mass_divisor,
    )

    total_mass_vs_mass_by_general_launch_payload_type(
        launch_vehicle_simplified_name=launch_vehicle_simplified_name,
        mass_step_size_kg=mass_step_size_kg,
        chart_title_prefix=chart_title_prefix,
        output_prefix=output_prefix,
        mass_suffix=mass_suffix,
        mass_divisor=mass_divisor,
    )

    launches_vs_month_by_general_launch_payload_type(
        launch_vehicle_simplified_name=launch_vehicle_simplified_name,
        chart_title_prefix=chart_title_prefix,
        output_prefix=output_prefix,
        x_tick_step_size=month_x_tick_step_size,
    )

    launches_vs_month_by_orbit(
        launch_vehicle_simplified_name=launch_vehicle_simplified_name,
        chart_title_prefix=chart_title_prefix,
        output_prefix=output_prefix,
        x_tick_step_size=month_x_tick_step_size,
    )

    launches_vs_year_by_general_launch_payload_type(
        launch_vehicle_simplified_name=launch_vehicle_simplified_name,
        chart_title_prefix=chart_title_prefix,
        output_prefix=output_prefix,
        x_tick_step_size=year_x_tick_step_size,
    )

    launches_vs_year_by_orbit(
        launch_vehicle_simplified_name=launch_vehicle_simplified_name,
        chart_title_prefix=chart_title_prefix,
        output_prefix=output_prefix,
        x_tick_step_size=year_x_tick_step_size,
    )

def generate_launch_vehicle_scatter_plots(launch_vehicle_simplified_name, chart_title_prefix, output_prefix, mass_step_size_kg=1000):
    mass_suffix = "t" if mass_step_size_kg == 1000 else "kg"
    mass_divisor = 1000 if mass_step_size_kg == 1000 else 1
    
    launch_apogee_vs_inclination_by_filter_scatter(
        chart_title_prefix=chart_title_prefix,
        output_prefix=output_prefix,
        series_column='Simple_Orbit',
        filter_function=mda.Filters.filter_by_launch_vehicle_name_simplified,
        filter_function_parameter=launch_vehicle_simplified_name,
        series_title='Orbit',
        color_map=mda.ChartUtils.orbit_color_map,
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
        color_map=mda.ChartUtils.orbit_color_map
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
        color_map=mda.ChartUtils.orbit_color_map
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
        y_scaling_factor=1
    )

def generate_launch_vehicle_family_charts(launch_vehicle_simplified_name, chart_title_prefix, output_prefix, mass_step_size_kg=1000, year_x_tick_step_size=1, color_map=mda.ChartUtils.color_sequence_2_8):
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
    )
    

def launches_vs_mass_by_filter(chart_title_prefix, output_prefix, chart_title_suffix, output_suffix, filter_function, filter_function_parameters_list, filter_function_additional_parameter=None, mass_step_size_kg=1000, launch_vehicle_simplified_name=None, launch_vehicle_family=None, color_map=None, mass_suffix='t', mass_divisor=100):
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

    mda.Filters.filter_by_launch_category(dataset.launch, ['O', 'D'])  # Filter for orbital and deep space launches
    if launch_vehicle_family is not None:
        mda.Filters.filter_by_launch_vehicle_family(dataset.launch, launch_vehicle_family)
    else:
        mda.Filters.filter_by_launch_vehicle_name_simplified(dataset.launch, launch_vehicle_simplified_name)

    os.makedirs(f'examples/outputs/raw_dataframes/{output_prefix}', exist_ok=True)
    dataset.launch.df.to_csv(f'examples/outputs/raw_dataframes/{output_prefix}/raw_dataframe_{output_name}.csv', index=False) # Save the filtered dataframe to CSV
    print(f"Dataframe 'raw_dataframe_{output_name}.csv' has been created.")
    
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

    # Create dictionary with columns that are the orbits and values are the mass ranges
    output_df = mda.ChartUtils.combine_dictionary_of_dataframes(dataframes)

    # Save to CSV
    os.makedirs(f'examples/outputs/csv/{output_prefix}', exist_ok=True)
    output_df.to_csv(f'examples/outputs/csv/{output_prefix}/{output_name}.csv', index=True)
    print(f"CSV file '{output_name}.csv' has been created.")

    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Launches vs. Payload Mass by {chart_title_suffix}',
        subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label=f'Payload Mass Range ({mass_suffix})',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        color_map=color_map,
        bargap=0.1,
    )
    
def launches_vs_mass_by_orbit(mass_step_size_kg, chart_title_prefix, output_prefix, launch_vehicle_simplified_name=None, launch_vehicle_family=None, mass_suffix='t', mass_divisor=1000):
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
        mass_divisor=mass_divisor
    )

def total_mass_vs_mass_by_filter(chart_title_prefix, output_prefix, chart_title_suffix, output_suffix, filter_function, filter_function_parameters_list, filter_function_additional_parameter=None, mass_step_size_kg=1000, launch_vehicle_simplified_name=None, launch_vehicle_family=None, color_map=None, mass_suffix='t', mass_divisor=1000):
    """
    Generate a chart showing the distribution of total launched mass versus payload mass range by a given filter function (e.g., launch vehicle, launch category, etc.).
    """
    output_name = f"{output_prefix}_total_mass_vs_mass_by_{output_suffix}"

    # Initialize dataset
    dataset = mda.McdowellDataset("./datasets")

    mda.Filters.filter_by_launch_category(dataset.launch, ['O', 'D'])  # Filter for orbital and deep space launches
    if launch_vehicle_family is not None:
        mda.Filters.filter_by_launch_vehicle_family(dataset.launch, launch_vehicle_family)
    else:
        mda.Filters.filter_by_launch_vehicle_name_simplified(dataset.launch, launch_vehicle_simplified_name)

    os.makedirs(f'examples/outputs/raw_dataframes/{output_prefix}', exist_ok=True)
    dataset.launch.df.to_csv(f'examples/outputs/raw_dataframes/{output_prefix}/raw_dataframe_{output_name}.csv', index=False)
    print(f"Dataframe 'raw_dataframe_{output_name}.csv' has been created.")

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

    total_masses = {}
    for key in dataframes.keys():
        total_mass = dataframes[key].groupby('Mass_Range', observed=False)['Payload_Mass'].sum()
        total_mass = total_mass.reindex(mass_labels, fill_value=0)
        total_masses[key] = total_mass / mass_divisor

    output_df = mda.ChartUtils.combine_dictionary_of_dataframes(total_masses)

    os.makedirs(f'examples/outputs/csv/{output_prefix}/', exist_ok=True)
    output_df.to_csv(f'examples/outputs/csv/{output_prefix}/{output_name}.csv', index=True)
    print(f"CSV file '{output_name}.csv' has been created.")

    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Net Payload Mass vs Mass Range by {chart_title_suffix}',
        subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label=f'Payload Mass Range ({mass_suffix})',
        y_label=f'Total Payload Mass ({mass_suffix})',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        color_map=color_map,
        bargap=0.1
    )
    
def total_mass_vs_mass_by_orbit(mass_step_size_kg, chart_title_prefix, output_prefix, launch_vehicle_simplified_name=None, launch_vehicle_family=None, mass_suffix='t', mass_divisor=1000):
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
        mass_divisor=mass_divisor
    )

def launches_vs_mass_by_general_launch_payload_type(mass_step_size_kg, chart_title_prefix, output_prefix, launch_vehicle_simplified_name=None, launch_vehicle_family=None, mass_suffix='t', mass_divisor=1000):
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
    mda.Filters.filter_by_launch_category(dataset.launch, ['O', 'D'])
    if launch_vehicle_family is not None:
        mda.Filters.filter_by_launch_vehicle_family(dataset.launch, launch_vehicle_family)
    else:
        mda.Filters.filter_by_launch_vehicle_name_simplified(dataset.launch, launch_vehicle_simplified_name)

    os.makedirs(f'examples/outputs/raw_dataframes/{output_prefix}', exist_ok=True)
    dataset.launch.df.to_csv(f'examples/outputs/raw_dataframes/{output_prefix}/raw_dataframe_{output_name}.csv', index=False) # Save the filtered dataframe to CSV
    print(f"Dataframe 'raw_dataframe_{output_name}.csv' has been created.")
    
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

    os.makedirs(f'examples/outputs/csv/{output_prefix}/', exist_ok=True)
    output_df.to_csv(f'examples/outputs/csv/{output_prefix}/{output_name}.csv', index=True)
    print(f"CSV file '{output_name}.csv' has been created.")

    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Launches vs. Payload Mass by Payload Type',
        subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label=f'Payload Mass Range ({mass_suffix})',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        color_map=mda.ChartUtils.general_launch_payload_type_color_map,
        bargap=0.1,
    )

def total_mass_vs_mass_by_general_launch_payload_type(mass_step_size_kg, chart_title_prefix, output_prefix, launch_vehicle_simplified_name=None, launch_vehicle_family=None, mass_suffix='t', mass_divisor=1000):
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
    mda.Filters.filter_by_launch_category(dataset.launch, ['O', 'D'])
    if launch_vehicle_family is not None:
        mda.Filters.filter_by_launch_vehicle_family(dataset.launch, launch_vehicle_family)
    else:
        mda.Filters.filter_by_launch_vehicle_name_simplified(dataset.launch, launch_vehicle_simplified_name)

    os.makedirs(f'examples/outputs/raw_dataframes/{output_prefix}', exist_ok=True)
    dataset.launch.df.to_csv(f'examples/outputs/raw_dataframes/{output_prefix}/raw_dataframe_{output_name}.csv', index=False) # Save the filtered dataframe to CSV
    print(f"Dataframe 'raw_dataframe_{output_name}.csv' has been created.")
    
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

    os.makedirs(f'examples/outputs/csv/{output_prefix}/', exist_ok=True)
    output_df.to_csv(f'examples/outputs/csv/{output_prefix}/{output_name}.csv', index=True)
    print(f"CSV file '{output_name}.csv' has been created.")

    # Plot stacked bar chart
    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Net Payload Mass vs Mass Range by Payload Type',
        subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label=f'Payload Mass Range ({mass_suffix})',
        y_label=f'Total Payload Mass ({mass_suffix})',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        color_map=mda.ChartUtils.general_launch_payload_type_color_map,
        bargap=0.1
    )

def launches_vs_month_by_orbit(chart_title_prefix, output_prefix, launch_vehicle_simplified_name=None, launch_vehicle_family=None, all_vehicles=False, x_tick_step_size=12, start_year=None, end_year=None):
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
    
    os.makedirs(f'examples/outputs/raw_dataframes/{output_prefix}', exist_ok=True)
    dataset.launch.df.to_csv(f'examples/outputs/raw_dataframes/{output_prefix}/raw_dataframe_{output_name}.csv', index=False) # Save the filtered dataframe to CSV
    print(f"Dataframe 'raw_dataframe_{output_name}.csv' has been created.")
    
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
    
    os.makedirs(f'examples/outputs/csv/{output_prefix}/', exist_ok=True)
    output_df.to_csv(f'examples/outputs/csv/{output_prefix}/{output_name}.csv', index=True)
    print(f"CSV file '{output_name}.csv' has been created.")

    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Launches vs. Month by Orbit',
        subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label='Date',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        color_map=mda.ChartUtils.orbit_color_map,
        bargap=0.0,
        x_tick0=0,
        x_tick_step_size=x_tick_step_size
    )
    
def launches_vs_month_by_general_launch_payload_type(chart_title_prefix, output_prefix, launch_vehicle_simplified_name=None, launch_vehicle_family=None, all_vehicles=False, x_tick_step_size=12, start_year=None, end_year=None):
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
    
    os.makedirs(f'examples/outputs/raw_dataframes/{output_prefix}', exist_ok=True)
    dataset.launch.df.to_csv(f'examples/outputs/raw_dataframes/{output_prefix}/raw_dataframe_{output_name}.csv', index=False) # Save the filtered dataframe to CSV
    print(f"Dataframe 'raw_dataframe_{output_name}.csv' has been created.")
    
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
    
    os.makedirs(f'examples/outputs/csv/{output_prefix}/', exist_ok=True)
    output_df.to_csv(f'examples/outputs/csv/{output_prefix}/{output_name}.csv', index=True)
    print(f"CSV file '{output_name}.csv' has been created.")
    
    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Launches vs. Month by Payload Type',
        subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label='Date',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        color_map=mda.ChartUtils.general_launch_payload_type_color_map,
        bargap=0.0,
        x_tick0=0,
        x_tick_step_size=x_tick_step_size
    )
    
def launches_vs_year_by_orbit(chart_title_prefix, output_prefix, launch_vehicle_simplified_name=None, launch_vehicle_family=None, all_vehicles=False, x_tick_step_size=1, start_year=None, end_year=None, ):
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
    
    os.makedirs(f'examples/outputs/raw_dataframes/{output_prefix}', exist_ok=True)
    dataset.launch.df.to_csv(f'examples/outputs/raw_dataframes/{output_prefix}/raw_dataframe_{output_name}.csv', index=False) # Save the filtered dataframe to CSV
    print(f"Dataframe 'raw_dataframe_{output_name}.csv' has been created.")
    
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
    
    os.makedirs(f'examples/outputs/csv/{output_prefix}/', exist_ok=True)
    output_df.to_csv(f'examples/outputs/csv/{output_prefix}/{output_name}.csv', index=True)
    print(f"CSV file '{output_name}.csv' has been created.")
    
    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Launches vs. Year by Orbit',
        subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label='Year',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        color_map=mda.ChartUtils.orbit_color_map,
        bargap=0.1,
        x_tick_step_size=x_tick_step_size
    )

def launches_vs_year_by_general_launch_payload_type(chart_title_prefix, output_prefix, launch_vehicle_simplified_name=None, launch_vehicle_family=None, all_vehicles=False, x_tick_step_size=1, start_year=None, end_year=None):
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
    
    os.makedirs(f'examples/outputs/raw_dataframes/{output_prefix}', exist_ok=True)
    dataset.launch.df.to_csv(f'examples/outputs/raw_dataframes/{output_prefix}/raw_dataframe_{output_name}.csv', index=False) # Save the filtered dataframe to CSV
    print(f"Dataframe 'raw_dataframe_{output_name}.csv' has been created.")
    
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
    
    os.makedirs(f'examples/outputs/csv/{output_prefix}/', exist_ok=True)
    output_df.to_csv(f'examples/outputs/csv/{output_prefix}/{output_name}.csv', index=True)
    print(f"CSV file '{output_name}.csv' has been created.")
    
    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Launches vs. Year by Payload Type',
        subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label='Year',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        color_map=mda.ChartUtils.general_launch_payload_type_color_map,
        bargap=0.1,
        x_tick_step_size=x_tick_step_size,
    )
    
def launches_vs_year_by_filter(chart_title_prefix, output_prefix, chart_title_suffix, output_suffix, filter_function, filter_function_parameters_list, filter_function_additional_parameter=None, launch_vehicle_simplified_name=None, launch_vehicle_family=None, all_vehicles=False, x_tick_step_size=1, color_map=None, start_year=None, end_year=None):
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
    """
    
    # Initialize dataset
    dataset = mda.McdowellDataset("./datasets")

    # Filter the base dataset
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

    os.makedirs(f'examples/outputs/raw_dataframes/{output_prefix}', exist_ok=True)
    dataset.launch.df.to_csv(f'examples/outputs/raw_dataframes/{output_prefix}/raw_dataframe_{output_name}.csv', index=False)
    print(f"Dataframe 'raw_dataframe_{output_name}.csv' has been created.")

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

    output_df = mda.ChartUtils.combine_dictionary_of_dataframes(dataframes)

    os.makedirs(f'examples/outputs/csv/{output_prefix}/', exist_ok=True)
    output_df.to_csv(f'examples/outputs/csv/{output_prefix}/{output_name}.csv', index=True)
    print(f"CSV file '{output_name}.csv' has been created.")

    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Launches vs. Year by {chart_title_suffix}',
        subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
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

    os.makedirs(f'examples/outputs/raw_dataframes/{output_prefix}', exist_ok=True)
    dataset.satcat.df.to_csv(f'examples/outputs/raw_dataframes/{output_prefix}/raw_dataframe_{output_name}.csv', index=False) # Save the filtered dataframe to CSV
    print(f"Dataframe 'raw_dataframe_{output_name}.csv' has been created.")
    
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
        
    os.makedirs(f'examples/outputs/csv/{output_prefix}/', exist_ok=True)
    output_df.to_csv(f'examples/outputs/csv/{output_prefix}/{output_name}.csv', index=True)
    print(f"CSV file '{output_name}.csv' has been created.")

    mda.ChartUtils.plot_bar(
        output_df,
        title=f"{chart_title_prefix} Payloads vs Year by Program",
        subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
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

    os.makedirs(f'examples/outputs/raw_dataframes/{output_prefix}', exist_ok=True)
    dataset.satcat.df.to_csv(f'examples/outputs/raw_dataframes/{output_prefix}/raw_dataframe_{output_name}.csv', index=False) # Save the filtered dataframe to CSV
    print(f"Dataframe 'raw_dataframe_{output_name}.csv' has been created.")
    
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

    os.makedirs(f'examples/outputs/csv/{output_prefix}/', exist_ok=True)
    output_df.to_csv(f'examples/outputs/csv/{output_prefix}/{output_name}.csv', index=True)
    print(f"CSV file '{output_name}.csv' has been created.")

    mda.ChartUtils.plot_bar(
        output_df,
        title=f"{chart_title_prefix} Payloads vs Year by {category}",
        subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label="Year",
        y_label="Number of Payloads",
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        bargap=0.0,
        color_map=color_map,
    )

def launch_value_vs_date_by_filter_scatter(chart_title_prefix, output_prefix, value_column, series_column, filter_function, filter_function_parameter, filter_function_additional_parameter=None, x_axis_title_suffix="", value_title=None, series_title=None, color_map=None, x_tick_step_size=None, start_year=None, end_year=None, y_scaling_factor=1):
    """
    Plot launches per date with a specified value column (e.g., Apogee, Mass, etc.) and series column (e.g., Launch Pad, Launch Vehicle, etc.) by filtering the dataset with a filter function.

    The value_column is plotted on the y-axis, and the series_column is used to split the data into different series.

    Args:
        chart_title_prefix (str): Prefix for the chart title (e.g., 'Falcon 9').
        output_prefix (str): Prefix for output file names.
        value_column (str): Name of the column to use for the y-axis values (e.g., 'Apogee').
        series_column (str): Name of the column to use for grouping series (e.g., 'Launch_Pad').
        filter_function (callable): Function to filter the dataset. Should accept the dataset as its first argument.
        filter_function_parameters (Any): Parameters to pass to the filter_function.
        color_map (dict, optional): Dictionary mapping series names to colors. Defaults to None.
        x_tick_step_size (int, optional): Step size for x-axis ticks. Defaults to 1.
        start_year (int, optional): Start year for the data. Defaults to None (uses earliest year in dataset).
        end_year (int, optional): End year for the data. Defaults to None (uses latest year in dataset).
    
    Interesting note:
    Because we're using raw dates and not a launch date field or something, we can't set x tick step size and get anything that makes sense. It's not a continuous dx in the dataset since some launches are hours apart and some are months.
    """
    
    dataset = mda.McdowellDataset()
    
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

    os.makedirs(f'examples/outputs/raw_dataframes/{output_prefix}', exist_ok=True)
    filtered_df.to_csv(f'examples/outputs/raw_dataframes/{output_prefix}/raw_dataframe_{output_name}.csv', index=False) # Save the filtered dataframe to CSV
    print(f"Dataframe 'raw_dataframe_{output_name}.csv' has been created.")
    
    filtered_df = filtered_df[['Launch_Date', value_column, series_column]].dropna(subset=[value_column])
    filtered_df = filtered_df[filtered_df[value_column] != 0] # Remove 0 values

    pivoted_df = mda.ChartUtils.pivot_dataframe(filtered_df, 'Launch_Date', series_column, value_column) # Pivot for plotting

    # Reorder in the order of the color map
    if color_map is not None:
        cols = list(color_map.keys())
        cols = [col for col in cols if col in pivoted_df.columns] # Remove keys that are not in the pivoted_df columns
        cols.insert(0, "Launch_Date")  # Ensure Launch_Date is always included as the first column
        pivoted_df = pivoted_df.reindex(columns=cols)
    
    os.makedirs(f'examples/outputs/csv/{output_prefix}/', exist_ok=True)
    pivoted_df.to_csv(f'examples/outputs/csv/{output_prefix}/{output_name}.csv', index=False)
    print(f"CSV file '{output_name}.csv' has been created.")

    if value_title is None:
        value_title = value_column.replace("_", " ").title()
    if series_title is None:
        series_title = series_column.replace("_", " ").title()
        
    mda.ChartUtils.plot_scatter(
        pivoted_df,
        x_col='Launch_Date',
        y_cols=pivoted_df.columns[1:], # Skip date line? pls fix
        title=f'{chart_title_prefix} Launches {value_title} vs. Date by {series_title}',
        subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label='Launch Date',
        y_label=f'{value_title} {x_axis_title_suffix}',
        dot_diameter=10,
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        color_map=color_map,
        y_scaling_factor=y_scaling_factor,
        x_tick_step_size=x_tick_step_size
    )
    
def launch_apogee_vs_inclination_by_filter_scatter(chart_title_prefix, output_prefix, series_column, filter_function, filter_function_parameter, filter_function_additional_parameter=None, series_title=None, color_map=None, start_year=None, end_year=None):
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
    
    os.makedirs(f'examples/outputs/raw_dataframes/{output_prefix}', exist_ok=True)
    filtered_df.to_csv(f'examples/outputs/raw_dataframes/{output_prefix}/raw_dataframe_{output_name}.csv', index=False) # Save the filtered dataframe to CSV
    print(f"Dataframe 'raw_dataframe_{output_name}.csv' has been created.")
    
    pivoted_df = mda.ChartUtils.pivot_dataframe(filtered_df, index_col='Inc', column_col=series_column, value_col='Apogee') # Pivot for plotting

    # Reorder in the order of the color map
    if color_map is not None:
        cols = list(color_map.keys())
        cols = [col for col in cols if col in pivoted_df.columns] # Remove keys that are not in the pivoted_df columns
        cols.insert(0, 'Inc')  # Ensure 'Inc' is always included as the first column
        pivoted_df = pivoted_df.reindex(columns=cols)

    os.makedirs(f'examples/outputs/csv/{output_prefix}/', exist_ok=True)
    pivoted_df.to_csv(f'examples/outputs/csv/{output_prefix}/{output_name}.csv')
    print(f"CSV file '{output_name}.csv' has been created.")

    if series_title is None:
        series_title = series_column.replace("_", " ").title()
    
    mda.ChartUtils.plot_scatter(
        pivoted_df,
        x_col='Inc',
        y_cols=pivoted_df.columns,
        title=f'{chart_title_prefix} Launches Apogee vs Inclination by {series_title}',
        subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
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
    
    os.makedirs(f'examples/outputs/raw_dataframes/{output_prefix}', exist_ok=True)
    filtered_df.to_csv(f'examples/outputs/raw_dataframes/{output_prefix}/raw_dataframe_{output_name}.csv', index=False)
    print(f"Dataframe 'raw_dataframe_{output_name}.csv' has been created.")
    
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
    
    os.makedirs(f'examples/outputs/csv/{output_prefix}/', exist_ok=True)
    output_df.to_csv(f'examples/outputs/csv/{output_prefix}/{output_name}.csv', index=True)
    print(f"CSV file '{output_name}.csv' has been created.")
    
    mda.ChartUtils.plot_bar(
        output_df,
        title=f"{chart_title_prefix} Payloads vs Year by {chart_title_suffix}",
        subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label="Year",
        y_label="Number of Payloads",
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        bargap=0.0,
        x_tick_step_size=x_tick_step_size,
        color_map=color_map,
    )


def payloads_vs_mass_by_filter(chart_title_prefix, output_prefix, chart_title_suffix, output_suffix, filter_function, filter_function_parameters_list, filter_function_additional_parameter=None, mass_step_size_kg=1000, launch_vehicle_simplified_name=None, launch_vehicle_family=None, color_map=None, mass_suffix='t', mass_divisor=100, country=None, max_mass=None):
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

    os.makedirs(f'examples/outputs/raw_dataframes/{output_prefix}', exist_ok=True)
    dataset.satcat.df.to_csv(f'examples/outputs/raw_dataframes/{output_prefix}/raw_dataframe_{output_name}.csv', index=False) # Save the filtered dataframe to CSV
    print(f"Dataframe 'raw_dataframe_{output_name}.csv' has been created.")
    
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
    os.makedirs(f'examples/outputs/csv/{output_prefix}', exist_ok=True)
    output_df.to_csv(f'examples/outputs/csv/{output_prefix}/{output_name}.csv', index=True)
    print(f"CSV file '{output_name}.csv' has been created.")

    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Launches vs. Payload Mass by {chart_title_suffix}',
        subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label=f'Payload Mass Range ({mass_suffix})',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{output_prefix}/{output_name}.png',
        color_map=color_map,
        bargap=0.1,
    )