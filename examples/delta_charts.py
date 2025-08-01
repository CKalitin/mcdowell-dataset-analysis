import standard_chart_generation as scg
import mcdowell_dataset_analysis as mda

launch_vehicle_simplified_name = ['Delta 1', 'Delta 2', 'Delta 3', 'Delta 4M', 'Delta 4H']
chart_title_prefix = 'Delta Orbital'
output_prefix = 'delta'

scg.generate_launch_vehicle_charts(
    launch_vehicle_simplified_name=launch_vehicle_simplified_name,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    year_x_tick_step_size=5,
    month_x_tick_step_size=60,
)

scg.generate_launch_vehicle_family_charts(
    launch_vehicle_simplified_name=launch_vehicle_simplified_name,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    year_x_tick_step_size=5,
)