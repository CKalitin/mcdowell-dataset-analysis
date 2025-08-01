import standard_chart_generation as scg
import mcdowell_dataset_analysis as mda

scg.launch_value_vs_date_by_filter_scatter(
    chart_title_prefix="Electron",
    output_prefix="electron",
    value_column='Apogee',
    series_column='Simple_Orbit',
    filter_function=mda.Filters.filter_by_launch_vehicle_name_simplified,
    filter_function_parameter="Electron",
    x_axis_title_suffix="(km)",
    value_title='Apogee',
    series_title='Orbit',
    color_map=mda.ChartUtils.orbit_color_map
)

scg.generate_launch_vehicle_charts(
    launch_vehicle_simplified_name="Electron",
    chart_title_prefix="Electron",
    output_prefix="electron",
    mass_step_size_kg=10,
    year_x_tick_step_size=1,
    month_x_tick_step_size=12,
)

scg.generate_launch_vehicle_scatter_plots(
    launch_vehicle_simplified_name="Electron",
    chart_title_prefix="Electron",
    output_prefix="electron",
    mass_step_size_kg=10,
)