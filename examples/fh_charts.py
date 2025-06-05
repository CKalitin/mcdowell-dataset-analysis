import standard_chart_generation as scg

scg.launches_vs_mass_by_orbit(
    launch_vehicle_simplified_name='Falcon Heavy',
    mass_step_size_kg=1000,
    chart_title_prefix='Falcon Heavy',
    output_prefix='fh',
    launch_vehicle_family=None
)

scg.total_mass_vs_mass_by_orbit(
    launch_vehicle_simplified_name='Falcon Heavy',
    mass_step_size_kg=1000,
    chart_title_prefix='Falcon Heavy',
    output_prefix='fh',
    launch_vehicle_family=None
)