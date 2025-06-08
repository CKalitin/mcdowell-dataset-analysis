import mcdowell_dataset_analysis as mda
import copy
import pandas as pd

dataset = mda.McdowellDataset("./datasets")

output_name = f"global_payloads_vs_year_by_simple_payload_category"

simple_payload_categories = mda.Translation.payload_category_to_simple_payload_category.values()

# Only include payloads with a simple payload category, which probably means orbital payloads
mda.Filters.filter_by_simple_payload_category(dataset.satcat, simple_payload_categories)
"""
dataframes = mda.ChartUtils.bin_dataset_into_dictionary_by_filter_function(
    dataset.satcat,
    filter_function=mda.Filters.filter_by_simple_payload_category,
    filter_function_parameters_list=bin_labels,
    value_col="Simple_Payload_Category",
    bins=bin_labels,
    bin_labels=bin_labels,
)"""

dataset.satcat.df['Launch_Year'] = dataset.satcat.df['Launch_Date'].dt.year

dataframes = {}
dataframes = mda.ChartUtils.group_dataset_into_dictionary_by_filter_function(
    dataset.satcat,
    filter_function=mda.Filters.filter_by_simple_payload_category,
    groups=simple_payload_categories,
    groupby_col="Launch_Year",
    count_values=True,
)

output_df = mda.ChartUtils.combine_dictionary_of_dataframes(dataframes)

output_df.to_csv(f"examples/outputs/csv/{output_name}.csv", index=True)
print(f"CSV file '{output_name}.csv' has been created.")

mda.ChartUtils.plot_bar(
    output_df,
    title="Global Payloads vs Year by Simple Payload Category",
    subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
    x_label="Year",
    y_label="Number of Payloads",
    output_path=f'examples/outputs/chart/{output_name}.png',
    color_map=mda.ChartUtils.simple_payload_category_color_map,
    bargap=0.0,
    x_tick0=0,
    x_tick_step_size=5
)