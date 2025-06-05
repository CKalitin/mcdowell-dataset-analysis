import standard_chart_generation as scg

launch_vehicle_family = "Titan"
chart_title_prefix = 'Titan'
output_prefix = 'titan'

scg.launches_vs_mass_by_orbit(
    launch_vehicle_family=launch_vehicle_family,
    mass_step_size_kg=1000,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    mass_suffix='t',
    mass_divisor=1000,
)

scg.total_mass_vs_mass_by_orbit(
    launch_vehicle_family=launch_vehicle_family,
    mass_step_size_kg=1000,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    mass_suffix='t',
    mass_divisor=1000,
)

scg.launches_vs_mass_by_general_launch_payload_type(
    launch_vehicle_family=launch_vehicle_family,
    mass_step_size_kg=1000,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    mass_suffix='t',
    mass_divisor=1000,
)

scg.total_mass_vs_mass_by_general_launch_payload_type(
    launch_vehicle_family=launch_vehicle_family,
    mass_step_size_kg=1000,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    mass_suffix='t',
    mass_divisor=1000,
)

scg.launches_vs_month_by_general_launch_payload_type(
    launch_vehicle_family=launch_vehicle_family,
    start_year=1979,
    end_year=2025,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    x_tick_step_size=60,
)

scg.launches_vs_month_by_orbit(
    launch_vehicle_family=launch_vehicle_family,
    start_year=1979,
    end_year=2025,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    x_tick_step_size=60,
)

scg.launches_vs_year_by_general_launch_payload_type(
    launch_vehicle_family=launch_vehicle_family,
    start_year=1979,
    end_year=2025,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    x_tick_step_size=5,
)

scg.launches_vs_year_by_orbit(
    launch_vehicle_family=launch_vehicle_family,
    start_year=1979,
    end_year=2025,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    x_tick_step_size=5,
)
