import standard_chart_generation as scg

# --- Orbits addressable by mass ---
scg.western_orbits_addressable_by_mass(
    chart_title_prefix='Western',
    chart_title="Orbits Addressable By NordSpace's Titan",
    output_prefix='western',
    leo_max_kg=5000,
    meo_max_kg=3000,
    gto_max_kg=2000,
    geo_max_kg=1000,
    heo_max_kg=1000,
    beo_max_kg=1000,
    min_mass_kg=200,
    max_mass_kg=5000,
    mass_step_size_kg=200,
    start_year=2020,
    date_range='2020-2026',
    save_raw_df=True,
    raw_df_title='nordspace_titan_addressable_payload_list',
    include_type_chart=True,
    include_category_chart=True,
    include_lv_chart=True,
    include_country_chart=True,
)

# --- Commercial western ---
scg.western_payload_pie(
    chart_title_prefix='Commercial Western',
    output_prefix='western',
    output_name_count='western_payload_category_count_pie',
    output_name_mass='western_payload_category_mass_pie',
    data_filter='commercial',
    color_map=scg.mda.ChartUtils.commercial_western_category_color_map,
    start_year=2020,
    date_range='2020-2026',
)

scg.western_launches_vs_mass(
    chart_title_prefix='Commercial Western',
    output_prefix='western',
    output_name='western_launches_vs_mass_by_category',
    data_filter='commercial',
    group_by='category',
    color_map=scg.mda.ChartUtils.commercial_western_category_color_map,
    mass_step_size_kg=1000,
    max_mass_kg=20000,
    start_year=2020,
    date_range='2020-2026',
    save_raw_df=True,
)

scg.western_launches_vs_mass(
    chart_title_prefix='Western',
    output_prefix='western',
    output_name='western_launches_vs_mass_by_lv',
    data_filter='all',
    group_by='lv',
    top_n=8,
    color_map=scg.mda.ChartUtils.color_sequence_3_8 + ['#434343'],
    mass_step_size_kg=1000,
    max_mass_kg=20000,
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

scg.western_launches_vs_mass(
    chart_title_prefix='Western',
    output_prefix='western',
    output_name='western_launches_vs_mass_200kg_by_lv',
    data_filter='all',
    group_by='lv',
    top_n=8,
    color_map=scg.mda.ChartUtils.color_sequence_3_8 + ['#434343'],
    min_mass_kg=0,
    max_mass_kg=5000,
    mass_step_size_kg=200,
    start_year=2020,
    date_range='2020-2026',
    save_raw_df=True,
)

scg.western_launches_vs_mass(
    chart_title_prefix='Western',
    output_prefix='western',
    output_name='western_launches_vs_mass_200kg_by_orbit',
    data_filter='all',
    group_by='orbit',
    color_map=scg.mda.ChartUtils.western_orbit_color_map,
    min_mass_kg=0,
    max_mass_kg=5000,
    mass_step_size_kg=200,
    start_year=2020,
    date_range='2020-2026',
)

scg.western_launches_vs_mass(
    chart_title_prefix='Western',
    output_prefix='western',
    output_name='western_small_sat_mass_distribution_by_lv',
    data_filter='all',
    group_by='lv',
    top_n=8,
    color_map=scg.mda.ChartUtils.color_sequence_3_8 + ['#434343'],
    min_mass_kg=0,
    max_mass_kg=1000,
    mass_step_size_kg=50,
    start_year=2020,
    date_range='2020-2026',
    save_raw_df=True,
)

# --- Western by orbit (all launches) ---
scg.western_launches_vs_mass(
    chart_title_prefix='Western',
    output_prefix='western',
    output_name='western_launches_vs_mass_by_orbit',
    data_filter='all',
    group_by='orbit',
    color_map=scg.mda.ChartUtils.western_orbit_color_map,
    mass_step_size_kg=1000,
    max_mass_kg=20000,
    include_pies=True,
    start_year=2020,
    date_range='2020-2026',
    save_raw_df=True,
)

# --- Western gov/mil ---
scg.western_payload_pie(
    chart_title_prefix='Western Gov/Mil',
    output_prefix='western',
    output_name_count='western_govmil_payload_category_count_pie',
    output_name_mass='western_govmil_payload_category_mass_pie',
    data_filter='govmil',
    color_map=scg.mda.ChartUtils.western_govmil_category_color_map,
    sort=False,
    date_range='2020-2026',
    start_year=2020,
)

scg.western_launches_vs_mass(
    chart_title_prefix='Western Gov/Mil',
    output_prefix='western',
    output_name='western_govmil_launches_vs_mass_by_category',
    data_filter='govmil',
    group_by='category',
    color_map=scg.mda.ChartUtils.western_govmil_category_color_map,
    mass_step_size_kg=1000,
    max_mass_kg=20000,
    include_pies=True,
    sort_pie=False,
    start_year=2020,
    date_range='2020-2026',
    save_raw_df=True,
)

# --- Net western (all launches combined) ---
scg.western_launches_vs_mass(
    chart_title_prefix='Western',
    output_prefix='western',
    output_name='western_net_launches_by_orbit',
    data_filter='all',
    group_by='orbit',
    color_map=scg.mda.ChartUtils.western_orbit_color_map,
    pies_only=True,
    start_year=2020,
    date_range='2020-2026',
)

scg.western_launches_vs_mass(
    chart_title_prefix='Western',
    output_prefix='western',
    output_name='western_net_launches_vs_mass_by_category',
    data_filter='net',
    group_by='category',
    color_map=scg.mda.ChartUtils.western_net_category_color_map,
    mass_step_size_kg=1000,
    max_mass_kg=20000,
    include_pies=True,
    start_year=2020,
    date_range='2020-2026',
)
