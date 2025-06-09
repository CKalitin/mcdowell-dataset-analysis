import standard_chart_generation as scg
import mcdowell_dataset_analysis as mda

chart_title_prefix = "Planet Labs"
output_prefix = "planet_labs"
owners_list = ["PLABS", "PLAN", "COSMOG"]

# ["PLABS", "PLAN", "COSMOG"] is all Planet Labs owners in the dataset, see https://x.com/planet4589/status/1931869110608265350

program_simplification_dict = {
    "Flock 1": ["Flock-1/I", "Flock-1/S"],
    "Flock 2": ["Flock-2/I", "Flock-2/S"],
    "Flock 3": ["Flock-3"],
    "Flock 4": ["Flock-4"],
    "PlanetIQ": ["Planetiq"],
}

program_order = ['Flock Dove', 'Flock 1', 'Flock 2', 'Flock 3', 'Skysat', 'Flock 4', 'PlanetIQ', 'Pelican', 'Tanager']

scg.owner_payloads_vs_year_by_program(
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    owners_list=owners_list,
    color_map=mda.ChartUtils.color_sequence_2_10,
    programing_simplification_dict=program_simplification_dict,
    program_order=program_order,
)

scg.owner_payloads_vs_year_by_orbit(
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    owners_list=owners_list,
    color_map=mda.ChartUtils.orbit_color_map,
)

scg.owner_payloads_vs_year_by_launch_vehicle(
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    owners_list=owners_list,
    color_map=mda.ChartUtils.color_sequence_2_10,
)

# More charts
# payloads vs year by program
# payloads vs year by orbit
# apogee vs inclination by program
# apogee vs date by program
# inclination vs date by program
# mass vs date by program

# More work required to find launches Planet Labs was on