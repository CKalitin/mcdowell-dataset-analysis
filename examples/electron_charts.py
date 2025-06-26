import standard_chart_generation as scg

scg.generate_launch_vehicle_charts(
    launch_vehicle_simplified_name="Electron",
    chart_title_prefix="Electron",
    output_prefix="electron",
    mass_step_size_kg=10,
)

scg.generate_launch_vehicle_scatter_plots(
    launch_vehicle_simplified_name="Electron",
    chart_title_prefix="Electron",
    output_prefix="electron",
    mass_step_size_kg=10,
)