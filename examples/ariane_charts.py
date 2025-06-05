import standard_chart_generation as scg

scg.launches_vs_mass_by_orbit(
    launch_vehicle_family=["Ariane", "Ariane5"],
    mass_step_size_kg=1000,
    chart_title_prefix='Ariane',
    output_prefix='ariane',
    mass_suffix='t',
    mass_divisor=1000,
)

scg.total_mass_vs_mass_by_orbit(
    launch_vehicle_family=["Ariane", "Ariane5"],
    mass_step_size_kg=1000,
    chart_title_prefix='Ariane',
    output_prefix='ariane',
    mass_suffix='t',
    mass_divisor=1000,
)

scg.launches_vs_mass_by_general_launch_payload_type(
    launch_vehicle_family=["Ariane", "Ariane5"],
    mass_step_size_kg=1000,
    chart_title_prefix='Ariane',
    output_prefix='ariane',
    mass_suffix='t',
    mass_divisor=1000,
)

scg.total_mass_vs_mass_by_general_launch_payload_type(
    launch_vehicle_family=["Ariane", "Ariane5"],
    mass_step_size_kg=1000,
    chart_title_prefix='Ariane',
    output_prefix='ariane',
    mass_suffix='t',
    mass_divisor=1000,
)

scg.launches_vs_month_by_general_launch_payload_type(
    launch_vehicle_family=["Ariane", "Ariane5"],
    start_year=1979,
    end_year=2025,
    chart_title_prefix='Ariane',
    output_prefix='ariane',
    x_tick_step_size=60,
)

scg.launches_vs_month_by_orbit(
    launch_vehicle_family=["Ariane", "Ariane5"],
    start_year=1979,
    end_year=2025,
    chart_title_prefix='Ariane',
    output_prefix='ariane',
    x_tick_step_size=60,
)

scg.launches_vs_year_by_general_launch_payload_type(
    launch_vehicle_family=["Ariane", "Ariane5"],
    start_year=1979,
    end_year=2025,
    chart_title_prefix='Ariane',
    output_prefix='ariane',
    x_tick_step_size=5,
)

scg.launches_vs_year_by_orbit(
    launch_vehicle_family=["Ariane", "Ariane5"],
    start_year=1979,
    end_year=2025,
    chart_title_prefix='Ariane',
    output_prefix='ariane',
    x_tick_step_size=5,
)
