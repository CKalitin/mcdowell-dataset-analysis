import standard_chart_generation as scg

launch_vehicle_simplified_name = ['Titan 2', 'Titan 3', 'Titan 4']
chart_title_prefix = 'Titan Orbital'
output_prefix = 'titan'

scg.generate_launch_vehicle_charts(
    launch_vehicle_simplified_name=launch_vehicle_simplified_name,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    year_x_tick_step_size=5,
    month_x_tick_step_size=60,
)

scg.generate_launch_vehicle_scatter_plots(
    launch_vehicle_simplified_name=launch_vehicle_simplified_name,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
)

scg.generate_launch_vehicle_family_charts(
    launch_vehicle_simplified_name=launch_vehicle_simplified_name,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    year_x_tick_step_size=5,
)