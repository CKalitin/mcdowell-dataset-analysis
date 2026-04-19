import standard_chart_generation as scg

scg.commercial_western_payload_categories_pie(
    chart_title_prefix='Commercial Western',
    output_prefix='commercial_western',
    start_year=2020,
)

scg.commercial_western_launches_vs_mass_by_category(
    chart_title_prefix='Commercial Western',
    output_prefix='commercial_western',
    mass_step_size_kg=1000,
    start_year=2020,
)
