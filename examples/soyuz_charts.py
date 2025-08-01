import standard_chart_generation as scg

launch_vehicle_simplified_name = "Soyuz"
chart_title_prefix = 'Soyuz'
output_prefix = 'soyuz'

scg.generate_launch_vehicle_charts(
    launch_vehicle_simplified_name=launch_vehicle_simplified_name,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    year_x_tick_step_size=5,
    month_x_tick_step_size=60,
)
