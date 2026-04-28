import standard_chart_generation as scg

# For Jacob Keeton https://x.com/CKalitin/status/2047190844718105019
# --- Launch cadence comparison ---
scg.launch_cadence_cumulative(
    output_prefix='western',
    output_name='launch_cadence_cumulative',
    chart_title='Cumulative Orbital Launches Since First Flight',
    max_years=10,
    color_map=scg.mda.ChartUtils.color_sequence_3_8,
)

# --- Orbits addressable by mass ---
scg.western_orbits_addressable_by_mass(
    chart_title_prefix='Western',
    chart_title="Launches Addressable by NordSpace's Titan",
    output_prefix='western',
    output_name='nordspace_titan_addressable_by_mass',
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
    include_nordspace_category_chart=True,
)

# --- Electron launches ---
scg.electron_launches(
    chart_title_prefix='Electron',
    output_prefix='western',
    output_name_by_category='electron_launches_by_category',
    start_year=2017,
    org_top_n=10,
    org_color_map=scg.mda.ChartUtils.color_sequence_3_12 + ['#9e9e9e'],
    include_haste=True,
    save_raw_df=True,
    raw_df_title='electron_launches_classified',
)

scg.electron_launches(
    chart_title_prefix='Electron',
    output_prefix='western',
    output_name_by_org='electron_launches_by_org_no_hypersonic',
    output_name_by_category='electron_launches_by_category_no_hypersonic',
    start_year=2017,
    org_top_n=10,
    org_color_map=scg.mda.ChartUtils.color_sequence_3_12 + ['#9e9e9e'],
    include_haste=False,
)

# --- Small sat 2018-2025 (megaconstellations excluded) ---
scg.western_small_sat_by_category(
    chart_title_prefix='Western',
    output_prefix='western',
    output_name='western_small_sat_by_year_and_category_2018_2025',
    max_mass_kg=300,
    start_year=2018,
    end_year=2025,
    date_range='2018-2025',
    color_map=scg.mda.ChartUtils.simple_payload_category_color_map,
    exclude_large_constellations=True,
    save_raw_df=True,
    raw_df_title='western_small_sat_2018_2025_raw',
    include_mass_dist=True,
    mass_dist_output_name='western_small_sat_mass_dist_2018_2025',
    mass_dist_start_year=2018,
    mass_dist_end_year=2025,
    mass_dist_date_range='2018-2025',
    mass_step_size_kg=10,
    include_lv_by_year=True,
    lv_by_year_output_name='western_small_sat_by_year_by_lv_2018_2025',
    lv_top_n=10,
    lv_color_map=scg.mda.ChartUtils.color_sequence_3_12 + ['#9e9e9e'],
    include_customer_by_year=True,
    customer_by_year_output_name='western_small_sat_by_year_by_customer_2018_2025',
    include_customer_mass_dist=True,
    customer_mass_dist_output_name='western_small_sat_mass_dist_by_customer_2018_2025',
    include_org_by_year=True,
    org_by_year_output_name='western_small_sat_by_year_by_org_2018_2025',
    include_org_mass_dist=True,
    org_mass_dist_output_name='western_small_sat_mass_dist_by_org_2018_2025',
    org_top_n=12,
    org_color_map=scg.mda.ChartUtils.color_sequence_3_12 + ['#9e9e9e'],
)

# --- Small sat by category ---
scg.western_small_sat_by_category(
    chart_title_prefix='Western',
    output_prefix='western',
    output_name='western_small_sat_by_year_and_category',
    max_mass_kg=300,
    start_year=2000,
    end_year=2017,
    date_range='2000-2017',
    color_map=scg.mda.ChartUtils.simple_payload_category_color_map,
    include_mass_dist=True,
    mass_dist_output_name='western_small_sat_mass_dist_2000_2017',
    mass_dist_start_year=2000,
    mass_dist_end_year=2017,
    mass_dist_date_range='2000-2017',
    mass_step_size_kg=10,
    include_lv_by_year=True,
    lv_by_year_output_name='western_small_sat_by_year_by_lv_2000_2017',
    lv_top_n=10,
    lv_color_map=scg.mda.ChartUtils.color_sequence_3_12 + ['#9e9e9e'],
    include_customer_by_year=True,
    customer_by_year_output_name='western_small_sat_by_year_by_customer_2000_2017',
    include_customer_mass_dist=True,
    customer_mass_dist_output_name='western_small_sat_mass_dist_by_customer_2000_2017',
    include_org_by_year=True,
    org_by_year_output_name='western_small_sat_by_year_by_org_2000_2017',
    include_org_mass_dist=True,
    org_mass_dist_output_name='western_small_sat_mass_dist_by_org_2000_2017',
    org_top_n=12,
    org_color_map=scg.mda.ChartUtils.color_sequence_3_12 + ['#9e9e9e'],
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
