import standard_chart_generation as scg

# --- Commercial western ---
scg.commercial_western_payload_categories_pie(
    chart_title_prefix='Commercial Western',
    output_prefix='commercial_western',
)

scg.commercial_western_launches_vs_mass_by_category(
    chart_title_prefix='Commercial Western',
    output_prefix='commercial_western',
    mass_step_size_kg=1000,
    start_year=2020,
)

# --- Western by orbit (all launches) ---
scg.western_launches_vs_mass_by_orbit(
    chart_title_prefix='Western',
    output_prefix='western',
    mass_step_size_kg=1000,
    start_year=2020,
)

# --- Western gov/mil ---
scg.western_govmil_payload_categories_pie(
    chart_title_prefix='Western Gov/Mil',
    output_prefix='western',
)

scg.western_govmil_launches_vs_mass_by_category(
    chart_title_prefix='Western Gov/Mil',
    output_prefix='western',
    mass_step_size_kg=1000,
    start_year=2020,
)

# --- Net western (all launches combined) ---
scg.western_net_by_orbit_pie(
    chart_title_prefix='Western',
    output_prefix='western',
    start_year=2020,
)

scg.western_net_launches_vs_mass_by_category(
    chart_title_prefix='Western',
    output_prefix='western',
    mass_step_size_kg=1000,
    start_year=2020,
)
