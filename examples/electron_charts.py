import standard_chart_generation as scg

scg.launches_vs_mass_by_orbit(
    launch_vehicle_simplified_name='Electron',
    mass_step_size_kg=10,
    chart_title_prefix='Electron',
    output_prefix='electron',
    mass_suffix='kg',
    mass_divisor=1,
)

scg.total_mass_vs_mass_by_orbit(
    launch_vehicle_simplified_name='Electron',
    mass_step_size_kg=10,
    chart_title_prefix='Electron',
    output_prefix='electron',
    mass_suffix='kg',
    mass_divisor=1,
)

scg.launches_vs_mass_by_general_launch_payload_type(
    launch_vehicle_simplified_name='Electron',
    mass_step_size_kg=10,
    chart_title_prefix='Electron',
    output_prefix='electron',
    mass_suffix='kg',
    mass_divisor=1,
)

scg.total_mass_vs_mass_by_general_launch_payload_type(
    launch_vehicle_simplified_name='Electron',
    mass_step_size_kg=10,
    chart_title_prefix='Electron',
    output_prefix='electron',
    mass_suffix='kg',
    mass_divisor=1,
)

scg.launches_vs_month_by_general_launch_payload_type(
    launch_vehicle_simplified_name='Electron',
    start_year=2017,
    end_year=2025,
    chart_title_prefix='Electron',
    output_prefix='electron',
)

scg.launches_vs_month_by_orbit(
    launch_vehicle_simplified_name='Electron',
    start_year=2017,
    end_year=2025,
    chart_title_prefix='Electron',
    output_prefix='electron',
)

scg.launches_vs_year_by_general_launch_payload_type(
    launch_vehicle_simplified_name='Electron',
    start_year=2017,
    end_year=2025,
    chart_title_prefix='Electron',
    output_prefix='electron',
)

scg.launches_vs_year_by_orbit(
    launch_vehicle_simplified_name='Electron',
    start_year=2017,
    end_year=2025,
    chart_title_prefix='Electron',
    output_prefix='electron',
)
