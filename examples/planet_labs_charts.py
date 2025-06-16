import standard_chart_generation as scg
import mcdowell_dataset_analysis as mda

chart_title_prefix = "Planet Labs"
output_prefix = "planet_labs"
owners_list = ["PLABS", "PLABST", "PLAN", "COSMOG"] # This is all Planet Labs owners in the dataset, see https://x.com/planet4589/status/1931869110608265350

program_simplification_dict = {
    "Flock 1": ["Flock-1/I", "Flock-1/S"],
    "Flock 2": ["Flock-2/I", "Flock-2/S"],
    "Flock 3": ["Flock-3"],
    "Flock 4": ["Flock-4"],
}

program_order = ['Flock Dove', 'Flock 1', 'Flock 2', 'Flock 3', 'Skysat', 'Flock 4', 'Pelican', 'Tanager']

planet_labs_country_color_map = {
    "Russia": "#A10B0B",  # Brighter red from Russian flag, vivid yet distinct
    "United States": "#0B4C97",  # Lighter navy blue, flag-inspired, high contrast
    "Japan": "#E02F2C",  # Bright red for the sun, distinct from Russia’s red
    "India": "#FFA024",  # Saffron, unchanged, vibrant and readable
    "New Zealand": "#09910F",  # Emerald green, brighter for landscapes, chart-friendly
    "French Guiana": "#2891E7"  # Medium blue, French flag-inspired, distinct from U.S.
}

scg.owner_payloads_vs_year_by_category(
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    owners_list=owners_list,
    category="Launch Country",
    color_map=planet_labs_country_color_map,
)

scg.owner_payloads_vs_year_by_category(
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    owners_list=owners_list,
    category="Launch Vehicle",
    color_map=mda.ChartUtils.color_sequence_2_10,
)

scg.owner_payloads_vs_year_by_category(
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    owners_list=owners_list,
    category="Orbit",
    color_map=mda.ChartUtils.orbit_color_map,
)

scg.owner_payloads_vs_year_by_program(
    chart_title_prefix=chart_title_prefix,
    output_prefix=output_prefix,
    owners_list=owners_list,
    color_map=mda.ChartUtils.color_sequence_2_10,
    programing_simplification_dict=program_simplification_dict,
    program_order=program_order,
)

# More charts
# apogee vs inclination by program
# apogee vs date by program
# inclination vs date by program

# More work required to find launches Planet Labs was on

# Could be fun to get TLEs vs. time and plot it all out, but would have to be for a good different project