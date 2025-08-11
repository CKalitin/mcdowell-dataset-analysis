import mcdowell_dataset_analysis as mda
from mcdowell_dataset_analysis import standard_chart_generation as scg
import pandas as pd

chart_title_prefix = 'Kuiper'
output_prefix = 'kuiper'
series_column = 'Launch_Vehicle_Simplified'
filter_function_parameter = 'Kuiper'
color_map = mda.ChartUtils.color_sequence_2_8

# Note Kuiper mass is incorrect in this dataset: https://x.com/ulalaunch/status/1917293762016846126

# Atlas V launch had 27 sats at 34000 lb (15422 kg). 571 kg per sat

# Open satcat.tsv and for every payload whose 'bus' column contains 'Kuiper', replace the mass at 571
satcat_path = 'datasets/satcat.tsv'
df = pd.read_csv(satcat_path, sep='\t')
kuiper_mask = df['Bus'].str.contains('Kuiper', case=False, na=False)
df.loc[kuiper_mask, 'Mass'] = 571
df.to_csv(satcat_path, sep='\t', index=False)

scg.launch_apogee_vs_inclination_by_filter_scatter(
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    series_column=series_column,
    filter_function=mda.Filters.filter_by_flight,
    filter_function_parameter=filter_function_parameter,
    series_title='Vehicle',
    color_map=color_map
)

scg.launch_value_vs_date_by_filter_scatter(
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    value_column='Apogee',
    series_column=series_column,
    filter_function=mda.Filters.filter_by_flight,
    filter_function_parameter=filter_function_parameter,
    x_axis_title_suffix="(km)",
    value_title='Apogee',
    series_title='Vehicle',
    color_map=color_map
)

scg.launch_value_vs_date_by_filter_scatter(
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    value_column='Inc',
    series_column=series_column,
    filter_function=mda.Filters.filter_by_flight,
    filter_function_parameter=filter_function_parameter,
    x_axis_title_suffix="(degrees)",
    value_title='Inclination',
    series_title='Vehicle',
    color_map=color_map
)

scg.launch_value_vs_date_by_filter_scatter(
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    value_column='Payload_Mass',
    series_column=series_column,
    filter_function=mda.Filters.filter_by_flight,
    filter_function_parameter=filter_function_parameter,
    x_axis_title_suffix="(t)",
    value_title='Payload Mass',
    series_title='Vehicle',
    color_map=color_map,
    y_scaling_factor=1e-3
)