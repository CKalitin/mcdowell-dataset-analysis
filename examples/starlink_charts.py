import mcdowell_dataset_analysis as mda
import standard_chart_generation as scg

scg.launch_value_vs_date_by_filter_scatter(
    chart_title_prefix='Starlink',
    output_prefix='starlink',
    value_column='Apogee',
    series_column='Launch_Pad',
    filter_function=mda.Filters.filter_by_mission,
    filter_function_parameter='Starlink', # Filter for Starlink missions
    x_axis_title_suffix="(km)",
    value_title='Apogee',
    series_title='Pad',
    color_map=mda.ChartUtils.f9_site_color_map
)

scg.launch_value_vs_date_by_filter_scatter(
    chart_title_prefix='Starlink',
    output_prefix='starlink',
    value_column='Inc',
    series_column='Launch_Pad',
    filter_function=mda.Filters.filter_by_mission,
    filter_function_parameter='Starlink',
    x_axis_title_suffix="(degrees)",
    value_title='Inclination',
    series_title='Pad',
    color_map=mda.ChartUtils.f9_site_color_map
)

scg.launch_value_vs_date_by_filter_scatter(
    chart_title_prefix='Starlink',
    output_prefix='starlink',
    value_column='Payload_Mass',
    series_column='Launch_Pad',
    filter_function=mda.Filters.filter_by_mission,
    filter_function_parameter='Starlink',
    x_axis_title_suffix="(t)",
    value_title='Payload Mass',
    series_title='Pad',
    color_map=mda.ChartUtils.f9_site_color_map,
    y_scaling_factor=1e-3
)