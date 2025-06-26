import standard_chart_generation as scg
import mcdowell_dataset_analysis as mda

launch_vehicle_simplified_name = ["Ariane 1", "Ariane 2", "Ariane 3", "Ariane 4", "Ariane 5", "Ariane 6"]
chart_title_prefix = 'Ariane'
output_prefix = 'ariane'

scg.generate_launch_vehicle_charts(
    launch_vehicle_simplified_name=launch_vehicle_simplified_name,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
)

scg.generate_launch_vehicle_family_charts(
    launch_vehicle_simplified_name=launch_vehicle_simplified_name,
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
)