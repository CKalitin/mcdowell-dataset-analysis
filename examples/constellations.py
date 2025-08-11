import mcdowell_dataset_analysis as mda
from mcdowell_dataset_analysis import standard_chart_generation as scg

scg.cumulative_payloads_by_filter_vs_date_since_first_payload(
    chart_title_prefix="Constellations",
    output_prefix="constellation_payloads",
    filter_function=mda.Filters.filter_column_by_contains,
    filter_function_parameters_list=["Starlink", "OneWeb", "Kuiper"],#, "Iridium SV", "Iridium Next SV"],
    filter_function_additional_parameter="PLName",
    series_names=["Starlink", "OneWeb", "Kuiper"],#, "Iridium", "Iridium Next"],
    start_year=2020,
    end_year=2025,
    line_width=4,
)

scg.cumulative_payloads_by_filter_vs_date_since_first_payload(
    chart_title_prefix="Constellations",
    output_prefix="constellation_payloads",
    filter_function=mda.Filters.filter_column_by_contains,
    filter_function_parameters_list=["Starlink", "OneWeb", "Kuiper"],#, "Iridium SV", "Iridium Next SV"],
    filter_function_additional_parameter="PLName",
    series_names=["Starlink", "OneWeb", "Kuiper"],#, "Iridium", "Iridium Next"],
    start_year=2020,
    end_year=2025,
    line_width=4,
    max_days_since_first=1000,
)

scg.cumulative_payloads_by_filter_vs_date_since_first_payload(
    chart_title_prefix="Constellations",
    output_prefix="constellation_payloads",
    filter_function=mda.Filters.filter_column_by_contains,
    filter_function_parameters_list=["Starlink", "OneWeb", "Kuiper"],#, "Iridium SV", "Iridium Next SV"],
    filter_function_additional_parameter="PLName",
    series_names=["Starlink", "OneWeb", "Kuiper"],#, "Iridium", "Iridium Next"],
    start_year=2020,
    end_year=2025,
    y_axis_type='log',
    line_width=4,
)

scg.cumulative_payloads_by_filter_vs_date_since_first_payload(
    chart_title_prefix="Constellations",
    output_prefix="constellation_payloads",
    filter_function=mda.Filters.filter_column_by_contains,
    filter_function_parameters_list=["Starlink", "OneWeb", "Kuiper"],#, "Iridium SV", "Iridium Next SV"],
    filter_function_additional_parameter="PLName",
    series_names=["Starlink", "OneWeb", "Kuiper"],#, "Iridium", "Iridium Next"],
    start_year=2020,
    end_year=2025,
    y_axis_type='log',
    line_width=4,
    max_days_since_first=1000,
)