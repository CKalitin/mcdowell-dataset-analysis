import mcdowell_dataset_analysis as mda

def launches_vs_mass_by_orbit(mass_step_size_kg, chart_title_prefix, output_prefix, launch_vehicle_simplified_name=None, launch_vehicle_family=None, mass_suffix='t', mass_divisor=1000):
    """Generate a chart showing the number of launches by payload mass range by orbit.
    Eg. How many launches were 2-3 tonnes and LEO, how many 6-7 tonnes and GTO, etc.

    Args:
        mass_step_size_kg (int): Step size in kg for the mass bins (eg. 1000 gives bins of 0-1000 kg, 1000-2000 kg, etc.)
        chart_title_prefix (str): Prefix for the chart title (should be the prettified name of the launch vehicle) (eg. 'Falcon 9') 
        output_prefix (str): Simplified name of LV for output files (eg. 'f9' for Falcon 9 gives "f9_launches_vs_mass_by_orbit")
        launch_vehicle_simplified_name (str, optional): Launch vehicle to filter by
        launch_vehicle_family (str, optional): Family of launch vehicle to filter by. If not none, then filtering will be done by family instead of the launch_vehicle field.
        mass_suffix (str, optional): Suffix for the mass labels (default is 't' for tonnes, use 'kg' if you want). Defaults to 't'.
        mass_divisor (int, optional): Divisor for the mass values in the chart (default is 1000 to convert kg to tonnes). Defaults to 1000.
    """
    
    output_name = f"{output_prefix}_launches_vs_mass_by_orbit"

    # Initialize dataset
    dataset = mda.McdowellDataset("./datasets")

    # Filter for Falcon 9 orbital and deep space launches
    mda.Filters.filter_by_launch_category(dataset.launch, ['O', 'D'])  # Filter for orbital and deep space launches
    if launch_vehicle_family is not None:
        mda.Filters.filter_by_launch_vehicle_family(dataset.launch, launch_vehicle_family)
    else:
        mda.Filters.filter_by_launch_vehicle_name_simplified(dataset.launch, launch_vehicle_simplified_name)

    max_mass = int(dataset.launch.df['Payload_Mass'].max())

    # Define orbit types and bins
    orbits = ['LEO', 'SSO', 'MEO', 'GTO', 'GEO', 'HEO', 'BEO']
    bins = list(range(0, max_mass+mass_step_size_kg, mass_step_size_kg)) # +mass_step_size_kg bc. range is exclusive
    mass_labels = [f"{int(bins[i]/mass_divisor)}-{int(bins[i+1]/mass_divisor)}{mass_suffix}" for i in range(len(bins)-1)]

    # Create a dictionary with key orbits and values are dataframes for each orbit showing the number of launches per payload mass range
    orbit_dataframes = mda.ChartUtils.bin_dataset_into_dictionary_by_filter_function(
        dataset=dataset.launch,
        filter_function=mda.Filters.filter_by_orbit,
        filter_function_parameters_list=orbits,
        value_col='Payload_Mass',
        bins=bins,
        bin_labels=mass_labels
    )

    # Create dictionary with columns that are the orbits and values are the mass ranges
    output_df = mda.ChartUtils.combine_dictionary_of_dataframes(orbit_dataframes)

    # Save to CSV
    output_df.to_csv(f'examples/outputs/csv/{output_name}.csv', index=True)
    print(f"CSV file '{output_name}.csv' has been created.")

    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Launches vs. Payload Mass by Orbit',
        subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label=f'Payload Mass Range ({mass_suffix})',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{output_name}.png',
        color_map=mda.ChartUtils.orbit_color_map,
        bargap=0.1,
    )

def total_mass_vs_mass_by_orbit(mass_step_size_kg, chart_title_prefix, output_prefix, launch_vehicle_simplified_name=None, launch_vehicle_family=None, mass_suffix='t', mass_divisor=1000):
    """Generate a chart showing the distribution of total launched mass versus payload mass range by orbit.
    Eg. How many launches were 2-3 tonnes and LEO, how many 6-7 tonnes and GTO, etc.

    Args:
        mass_step_size_kg (int): Step size in kg for the mass bins (eg. 1000 gives bins of 0-1000 kg, 1000-2000 kg, etc.)
        chart_title_prefix (str): Prefix for the chart title (should be the prettified name of the launch vehicle) (eg. 'Falcon 9') 
        output_prefix (str): Simplified name of LV for output files (eg. 'f9' for Falcon 9 gives "f9_total_mass_vs_mass_by_orbit")
        launch_vehicle_simplified_name (str, optional): Launch vehicle to filter by
        launch_vehicle_family (str, optional): Family of launch vehicle to filter by. If not none, then filtering will be done by family instead of the launch_vehicle field.
        mass_suffix (str, optional): Suffix for the mass labels (default is 't' for tonnes, use 'kg' if you want). Defaults to 't'.
        mass_divisor (int, optional): Divisor for the mass values in the chart (default is 1000 to convert kg to tonnes). Defaults to 1000.
    """
    
    output_name = f"{output_prefix}_total_mass_vs_mass_by_orbit"

    # Initialize dataset
    dataset = mda.McdowellDataset()

    mda.Filters.filter_by_launch_category(dataset.launch, ['O', 'D'])  # Filter for orbital and deep space launches
    if launch_vehicle_family is not None:
        mda.Filters.filter_by_launch_vehicle_family(dataset.launch, launch_vehicle_family)
    else:
        mda.Filters.filter_by_launch_vehicle_name_simplified(dataset.launch, launch_vehicle_simplified_name)

    max_mass = int(dataset.launch.df['Payload_Mass'].max())

    # Define orbit types in desired order
    orbits = ['LEO', 'SSO', 'MEO', 'GTO', 'GEO', 'HEO', 'BEO']
    bins = list(range(0, max_mass+mass_step_size_kg, mass_step_size_kg)) # +mass_step_size_kg bc. range is exclusive
    mass_labels = [f"{int(bins[i]/mass_divisor)}-{int(bins[i+1]/mass_divisor)}{mass_suffix}" for i in range(len(bins)-1)]

    orbit_dataframes = mda.ChartUtils.bin_dataset_into_dictionary_by_filter_function(
        dataset=dataset.launch,
        filter_function=mda.Filters.filter_by_orbit,
        filter_function_parameters_list=orbits,
        value_col='Payload_Mass',
        bins=bins,
        bin_labels=mass_labels,
        count_values=False,
        bin_column = 'Mass_Range'
    )

    orbit_masses = {}
    for orbit_dataframe_key in orbit_dataframes.keys():
        total_mass = orbit_dataframes[orbit_dataframe_key].groupby('Mass_Range', observed=False)['Payload_Mass'].sum() # Sum mass in payload range for this orbit
        total_mass = total_mass.reindex(mass_labels, fill_value=0)
        orbit_masses[orbit_dataframe_key] = total_mass/mass_divisor

    output_df = mda.ChartUtils.combine_dictionary_of_dataframes(orbit_masses)

    # Save to CSV
    output_df.to_csv(f'examples/outputs/csv/{output_name}.csv', index=True)
    print(f"CSV file '{output_name}.csv' has been created.")

    # Plot stacked bar chart
    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Net Payload Mass vs Mass Range by Orbit',
        subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label=f'Payload Mass Range ({mass_suffix})',
        y_label=f'Total Payload Mass ({mass_suffix})',
        output_path=f'examples/outputs/chart/{output_name}.png',
        color_map=mda.ChartUtils.orbit_color_map,
        bargap=0.1
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
    output_df.to_csv(f'examples/outputs/csv/{output_name}.csv', index=True)
    print(f"CSV file '{output_name}.csv' has been created.")

    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Launches vs. Payload Mass by Payload Type',
        subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label=f'Payload Mass Range ({mass_suffix})',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{output_name}.png',
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
    output_df.to_csv(f'examples/outputs/csv/{output_name}.csv', index=True)
    print(f"CSV file '{output_name}.csv' has been created.")

    # Plot stacked bar chart
    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Net Payload Mass vs Mass Range by Payload Type',
        subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label=f'Payload Mass Range ({mass_suffix})',
        y_label=f'Total Payload Mass ({mass_suffix})',
        output_path=f'examples/outputs/chart/{output_name}.png',
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

    output_name = f"{output_prefix}_launches_vs_month_by_orbit_{start_year}_{end_year}"

    # After getting the start and end years, filter the dataset by launch date
    mda.Filters.filter_by_launch_date(dataset.launch, start_date=f'{start_year}-01-01', end_date=f'{end_year}-12-31')
    
    # Encode launch month as year*12 + months to get total months since Jesus instead of years since Jesus
    dataset.launch.df['Launch_Month'] = dataset.launch.df['Launch_Date'].dt.year*12 + dataset.launch.df['Launch_Date'].dt.month
    
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

    output_df.to_csv(f'examples/outputs/csv/{output_name}.csv', index=True)
    print(f"CSV file '{output_name}.csv' has been created.")

    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Launches vs. Month by Orbit',
        subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label='Date',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{output_name}.png',
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

    output_name = f"{output_prefix}_launches_vs_month_by_general_launch_payload_type_{start_year}_{end_year}"

    # After getting the start and end years, filter the dataset by launch date
    mda.Filters.filter_by_launch_date(dataset.launch, start_date=f'{start_year}-01-01', end_date=f'{end_year}-12-31')
    
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
    
    output_df.to_csv(f'examples/outputs/csv/{output_name}.csv', index=True)
    print(f"CSV file '{output_name}.csv' has been created.")
    
    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Launches vs. Month by Payload Type',
        subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label='Date',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{output_name}.png',
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

    output_name = f"{output_prefix}_launches_vs_year_by_orbit_{start_year}_{end_year}"

    # After getting the start and end years, filter the dataset by launch date
    mda.Filters.filter_by_launch_date(dataset.launch, start_date=f'{start_year}-01-01', end_date=f'{end_year}-12-31')
    
    # Encode launch month as year*12 + months to get total months since Jesus instead of years since Jesus
    dataset.launch.df['Launch_Year'] = dataset.launch.df['Launch_Date'].dt.year
    
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
    
    output_df.to_csv(f'examples/outputs/csv/{output_name}.csv', index=True)
    print(f"CSV file '{output_name}.csv' has been created.")
    
    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Launches vs. Year by Orbit',
        subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label='Year',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{output_name}.png',
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

    output_name = f"{output_prefix}_launches_vs_year_by_general_launch_payload_type_{start_year}_{end_year}"

    # After getting the start and end years, filter the dataset by launch date
    mda.Filters.filter_by_launch_date(dataset.launch, start_date=f'{start_year}-01-01', end_date=f'{end_year}-12-31')
    
    # Encode launch month as year*12 + months to get total months since Jesus instead of years since Jesus
    dataset.launch.df['Launch_Year'] = dataset.launch.df['Launch_Date'].dt.year
    
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
    
    output_df.to_csv(f'examples/outputs/csv/{output_name}.csv', index=True)
    print(f"CSV file '{output_name}.csv' has been created.")
    
    mda.ChartUtils.plot_bar(
        output_df,
        title=f'{chart_title_prefix} Launches vs. Year by  Payload Type',
        subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
        x_label='Year',
        y_label='Number of Launches',
        output_path=f'examples/outputs/chart/{output_name}.png',
        color_map=mda.ChartUtils.general_launch_payload_type_color_map,
        bargap=0.1,
        x_tick_step_size=x_tick_step_size,
    )


