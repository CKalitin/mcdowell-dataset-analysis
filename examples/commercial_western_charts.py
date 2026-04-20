import standard_chart_generation as scg

# --- Commercial western ---
scg.commercial_western_payload_categories_pie(
    chart_title_prefix='Commercial Western',
    output_prefix='western',
    date_range='2020-2026',
)

scg.commercial_western_launches_vs_mass_by_category(
    chart_title_prefix='Commercial Western',
    output_prefix='western',
    mass_step_size_kg=1000,
    start_year=2020,
    date_range='2020-2026',
)

scg.western_launches_vs_mass_by_lv(
    chart_title_prefix='Western',
    output_prefix='western',
    mass_step_size_kg=1000,
    start_year=2020,
    date_range='2020-2026',
)

scg.western_launches_vs_mass_by_lv_and_orbit(
    chart_title_prefix='Western',
    output_prefix='western',
    start_year=2020,
    date_range='2020-2026',
)

scg.western_small_sat_mass_distribution_by_lv(
    chart_title_prefix='Western',
    output_prefix='western',
    start_year=2020,
    date_range='2020-2026',
)

scg.commercial_western_rideshare_by_lv(
    chart_title_prefix='Commercial Western',
    output_prefix='western',
    mass_step_size_kg=1000,
    start_year=2020,
    date_range='2020-2026',
)

# --- Western by orbit (all launches) ---
scg.western_launches_vs_mass_by_orbit(
    chart_title_prefix='Western',
    output_prefix='western',
    mass_step_size_kg=1000,
    start_year=2020,
    date_range='2020-2026',
)

# --- Western gov/mil ---
scg.western_govmil_payload_categories_pie(
    chart_title_prefix='Western Gov/Mil',
    output_prefix='western',
    date_range='2020-2026',
)

scg.western_govmil_launches_vs_mass_by_category(
    chart_title_prefix='Western Gov/Mil',
    output_prefix='western',
    mass_step_size_kg=1000,
    start_year=2020,
    date_range='2020-2026',
)

# --- Net western (all launches combined) ---
scg.western_net_by_orbit_pie(
    chart_title_prefix='Western',
    output_prefix='western',
    start_year=2020,
    date_range='2020-2026',
)

scg.western_net_launches_vs_mass_by_category(
    chart_title_prefix='Western',
    output_prefix='western',
    mass_step_size_kg=1000,
    start_year=2020,
    date_range='2020-2026',
)
