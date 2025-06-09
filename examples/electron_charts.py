import standard_chart_generation as scg
import mcdowell_dataset_analysis as mda

launch_vehicle_simplified_name = "Electron"
chart_title_prefix = 'Electron'
output_prefix = 'electron'

"""scg.launches_vs_mass_by_orbit(
    launch_vehicle_simplified_name=launch_vehicle_simplified_name,
    mass_step_size_kg=10,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    mass_suffix='kg',
    mass_divisor=1,
)

scg.total_mass_vs_mass_by_orbit(
    launch_vehicle_simplified_name=launch_vehicle_simplified_name,
    mass_step_size_kg=10,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    mass_suffix='kg',
    mass_divisor=1,
)

scg.launches_vs_mass_by_general_launch_payload_type(
    launch_vehicle_simplified_name=launch_vehicle_simplified_name,
    mass_step_size_kg=10,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    output_prefix='electron',
    mass_suffix='kg',
    mass_divisor=1,
)

scg.total_mass_vs_mass_by_general_launch_payload_type(
    launch_vehicle_simplified_name=launch_vehicle_simplified_name,
    mass_step_size_kg=10,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    mass_suffix='kg',
    mass_divisor=1,
)

scg.launches_vs_month_by_general_launch_payload_type(
    launch_vehicle_simplified_name=launch_vehicle_simplified_name,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
)

scg.launches_vs_month_by_orbit(
    launch_vehicle_simplified_name=launch_vehicle_simplified_name,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
)

scg.launches_vs_year_by_general_launch_payload_type(
    launch_vehicle_simplified_name=launch_vehicle_simplified_name,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
)

scg.launches_vs_year_by_orbit(
    launch_vehicle_simplified_name=launch_vehicle_simplified_name,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
)"""

scg.launch_apogee_vs_inclination_by_filter_scatter(
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    series_column='Simple_Orbit',
    filter_function=mda.Filters.filter_by_launch_vehicle_name_simplified,
    filter_function_parameter=launch_vehicle_simplified_name,
    series_title='Orbit',
    color_map=mda.ChartUtils.orbit_color_map
)

scg.launch_value_vs_date_by_filter_scatter(
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

scg.launch_value_vs_date_by_filter_scatter(
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

scg.launch_value_vs_date_by_filter_scatter(
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    value_column='Payload_Mass',
    series_column='Simple_Orbit',
    filter_function=mda.Filters.filter_by_launch_vehicle_name_simplified,
    filter_function_parameter=launch_vehicle_simplified_name,
    x_axis_title_suffix="(kg)",
    value_title='Payload Mass',
    series_title='Orbit',
    color_map=mda.ChartUtils.orbit_color_map,
    y_scaling_factor=1
)