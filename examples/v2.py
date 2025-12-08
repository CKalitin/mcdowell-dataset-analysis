import mcdowell_dataset_analysis as mda
import standard_chart_generation as scg
from datetime import datetime

chart_title_prefix = "V2"
output_prefix = "v2"
launch_vehicle_simplified_name = ['A-4', 'V-2']

def charts_by_filter(filter_function, filter_function_parameters_list, chart_title_suffix, output_suffix, filter_function_additional_parameter=None):
    scg.launches_vs_year_by_filter(
        chart_title_prefix=chart_title_prefix,
        output_prefix=output_prefix,
        chart_title_suffix=chart_title_suffix,
        output_suffix=output_suffix,
        filter_function=filter_function,
        filter_function_parameters_list=filter_function_parameters_list,
        filter_function_additional_parameter=filter_function_additional_parameter,
        launch_vehicle_simplified_name=launch_vehicle_simplified_name,
        x_tick_step_size=1,
        color_map=mda.ChartUtils.color_sequence_2_6,
        filter_out_suborbital=False,
    )
    
    scg.launches_vs_month_by_filter(
        chart_title_prefix=chart_title_prefix,
        output_prefix=output_prefix,
        chart_title_suffix=chart_title_suffix,
        output_suffix=output_suffix,
        filter_function=filter_function,
        filter_function_parameters_list=filter_function_parameters_list,
        filter_function_additional_parameter=filter_function_additional_parameter,
        launch_vehicle_simplified_name=launch_vehicle_simplified_name,
        x_tick_step_size=6,
        color_map=mda.ChartUtils.color_sequence_2_6,
        filter_out_suborbital=False,
    )
      
scg.launch_value_vs_date_by_filter_scatter(
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    value_column="Apogee",
    series_column="Launch_Vehicle_Simplified",
    filter_function=mda.Filters.filter_by_launch_vehicle_name_simplified,
    filter_function_parameter=launch_vehicle_simplified_name,
    x_axis_title_suffix='',
    value_title='Apogee (km)',
    series_title='Launch Vehicle',
    color_map=mda.ChartUtils.color_sequence_2_10,
    x_axis_type='date',
    filter_out_suborbital=False,
)

charts_by_filter(
    filter_function=mda.Filters.filter_by_launch_vehicle_name_simplified,
    filter_function_parameters_list=launch_vehicle_simplified_name,
    chart_title_suffix='Launch Vehicle',
    output_suffix='launch_vehicle',
)

categories = ['Test', 'Weapon', 'Training', 'Scientific']

charts_by_filter(
    filter_function=mda.Filters.filter_column_by_exact,
    filter_function_parameters_list=categories,
    filter_function_additional_parameter='V2_Payload_Category',
    chart_title_suffix='Category',
    output_suffix='category',
)

# Category Counts for A-4 and V-2 Launches
# Test                        : 269
# Weapon                      : 216
# Training                    : 81
# Solar UV/CR                 : 4
# CR                          : 4
# Solar UV                    : 4
# Aeron                       : 4
# CR/Ionos                    : 3
# Aeron/Solar X/Bio           : 2
# CR/Aeron                    : 2
# Solar UV,X/CR               : 2
# Solar UV/Ionos              : 2
# Test/CR                     : 2
# Solar UV,X/Aeron            : 1
# Ionos/Solar X/Aeron/IR      : 1
# CR/Solar EUV/Bio            : 1
# Ionos/Meteorites            : 1
# Ionos/Solar X/Bio           : 1
# Solar X/CR/Aeron            : 1
# Solar X/Ionos               : 1
# Aeron/CR                    : 1
# Test/Photo/Aeron            : 1
# Solar X/Ionos/Meteorites    : 1
# Solar X/Ionos/Biology       : 1
# Ionos/Solar X/Biology       : 1
# Solar EUV/X                 : 1
# Ionos/Aeron/Solar X         : 1
# Aeron/Ionos/Solar UV        : 1
# Solar X/Ionos/Aeron/Bio     : 1
# Solar X/Biology             : 1
# Test/Solar UV,X             : 1
# Solar X/Ionos/Bio           : 1
# Aeron/B field               : 1
# Solar X/Aeron               : 1
# Solar UV/Aeron              : 1
# CR/Solar UV                 : 1
# Test/Aeron                  : 1
# Solar UV/CR/Ionos           : 1
# Ionos/Bio                   : 1
# CR/Meteor test              : 1
# Aeron/Ionos                 : 1
# Ionos                       : 1
# Test/Photo/Solar X/Aeron    : 1