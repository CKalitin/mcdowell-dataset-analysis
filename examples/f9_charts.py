import standard_chart_generation as scg

scg.launches_vs_mass_by_orbit(
    launch_vehicle_simplified_name='Falcon 9',
    mass_step_size_kg=1000,
    chart_title_prefix='Falcon 9',
    output_prefix='f9'
)

scg.total_mass_vs_mass_by_orbit(
    launch_vehicle_simplified_name='Falcon 9',
    mass_step_size_kg=1000,
    chart_title_prefix='Falcon 9',
    output_prefix='f9'
)

scg.launches_vs_mass_by_general_launch_payload_type(
    launch_vehicle_simplified_name='Falcon 9',
    mass_step_size_kg=1000,
    chart_title_prefix='Falcon 9',
    output_prefix='f9'
)

scg.total_mass_vs_mass_by_general_launch_payload_type(
    launch_vehicle_simplified_name='Falcon 9',
    mass_step_size_kg=1000,
    chart_title_prefix='Falcon 9',
    output_prefix='f9'
)

scg.launches_vs_month_by_general_launch_payload_type(
    launch_vehicle_simplified_name='Falcon 9',
    start_year=2010,
    end_year=2025,
    chart_title_prefix='Falcon 9',
    output_prefix="f9",
)

scg.launches_vs_month_by_orbit(
    launch_vehicle_simplified_name='Falcon 9',
    start_year=2010,
    end_year=2025,
    chart_title_prefix="Falcon 9",
    output_prefix="f9",
)

scg.launches_vs_year_by_general_launch_payload_type(
    launch_vehicle_simplified_name='Falcon 9',
    start_year=2010,
    end_year=2025,
    chart_title_prefix='Falcon 9',
    output_prefix="f9",
)

scg.launches_vs_year_by_orbit(
    launch_vehicle_simplified_name='Falcon 9',
    start_year=2010,
    end_year=2025,
    chart_title_prefix='Falcon 9',
    output_prefix="f9",
)
