import standard_chart_generation as scg

launch_vehicle_simplified_name = "Falcon 9"
chart_title_prefix = "Falcon 9"
output_prefix = "f9"

"""scg.generate_launch_vehicle_charts(
    launch_vehicle_simplified_name=launch_vehicle_simplified_name,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    year_x_tick_step_size=1,
    month_x_tick_step_size=12,
)"""

scg.generate_launch_vehicle_scatter_plots(
    launch_vehicle_simplified_name=launch_vehicle_simplified_name,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
)
