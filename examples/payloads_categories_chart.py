import standard_chart_generation as scg
import mcdowell_dataset_analysis as mda

chart_title_prefix = "Observation"
output_prefix = "observation"

scg.payloads_filtered_vs_year_by_filter(
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    chart_title_suffix="Orbit",
    output_suffix="orbit",
    initial_filter_functions=[mda.Filters.filter_by_simple_payload_category],
    initial_filter_function_parameters_list=["Observation"],
    filter_function=mda.Filters.filter_by_orbit,
    filter_function_parameters_list=mda.ChartUtils.orbit_color_map.keys(),
    x_tick_step_size=5,
    color_map=mda.ChartUtils.orbit_color_map,
)