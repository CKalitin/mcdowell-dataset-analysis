import standard_chart_generation as scg
import mcdowell_dataset_analysis as mda

launch_vehicle_simplified_name = ['Delta 1', 'Delta 2', 'Delta 3', 'Delta 4M', 'Delta 4H']
chart_title_prefix = 'Delta Orbital'
output_prefix = 'delta'

scg.launches_vs_mass_by_orbit(
    launch_vehicle_simplified_name=launch_vehicle_simplified_name,
    mass_step_size_kg=1000,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    mass_suffix='t',
    mass_divisor=1000,
)

scg.launches_vs_mass_by_general_launch_payload_type(
    launch_vehicle_simplified_name=launch_vehicle_simplified_name,
    mass_step_size_kg=1000,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    mass_suffix='t',
    mass_divisor=1000,
)

scg.launches_vs_mass_by_filter(
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    chart_title_suffix='Launch Vehicle',
    output_suffix='launch_vehicle',
    filter_function=mda.Filters.filter_by_launch_vehicle_name_simplified,
    filter_function_parameters_list=launch_vehicle_simplified_name,
    launch_vehicle_simplified_name=launch_vehicle_simplified_name,
    mass_step_size_kg=1000,
    color_map=mda.ChartUtils.color_sequence_2_6,
    mass_suffix='t',
    mass_divisor=1000,
)

scg.total_mass_vs_mass_by_orbit(
    launch_vehicle_simplified_name=launch_vehicle_simplified_name,
    mass_step_size_kg=1000,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    mass_suffix='t',
    mass_divisor=1000,
)

scg.total_mass_vs_mass_by_general_launch_payload_type(
    launch_vehicle_simplified_name=launch_vehicle_simplified_name,
    mass_step_size_kg=1000,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    mass_suffix='t',
    mass_divisor=1000,
)

scg.total_mass_vs_mass_by_filter(
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    chart_title_suffix='Launch Vehicle',
    output_suffix='launch_vehicle',
    filter_function=mda.Filters.filter_by_launch_vehicle_name_simplified,
    filter_function_parameters_list=launch_vehicle_simplified_name,
    launch_vehicle_simplified_name=launch_vehicle_simplified_name,
    mass_step_size_kg=1000,
    color_map=mda.ChartUtils.color_sequence_2_6,
    mass_suffix='t',
    mass_divisor=1000,
)

scg.launches_vs_month_by_general_launch_payload_type(
    launch_vehicle_simplified_name=launch_vehicle_simplified_name,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    x_tick_step_size=60,
)

scg.launches_vs_month_by_orbit(
    launch_vehicle_simplified_name=launch_vehicle_simplified_name,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    x_tick_step_size=60,
)

scg.launches_vs_year_by_general_launch_payload_type(
    launch_vehicle_simplified_name=launch_vehicle_simplified_name,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    x_tick_step_size=5,
)

scg.launches_vs_year_by_orbit(
    launch_vehicle_simplified_name=launch_vehicle_simplified_name,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    x_tick_step_size=5,
)

scg.launches_vs_year_by_filter(
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    chart_title_suffix='Launch Vehicle',
    output_suffix='launch_vehicle',
    filter_function=mda.Filters.filter_by_launch_vehicle_name_simplified,
    filter_function_parameters_list=launch_vehicle_simplified_name,
    launch_vehicle_simplified_name=launch_vehicle_simplified_name,
    x_tick_step_size=5,
    color_map=mda.ChartUtils.color_sequence_2_6,
)