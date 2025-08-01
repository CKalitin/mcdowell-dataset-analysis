import standard_chart_generation as scg

launch_vehicle_simplified_name = "Falcon Heavy"
chart_title_prefix = "Falcon Heavy"
output_prefix = "fh"

scg.generate_launch_vehicle_charts(
    launch_vehicle_simplified_name=launch_vehicle_simplified_name,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    year_x_tick_step_size=1,
    month_x_tick_step_size=12,
)
