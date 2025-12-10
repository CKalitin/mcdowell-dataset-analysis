import mcdowell_dataset_analysis as mda
import os

dataset = mda.McdowellDataset("./datasets")

output_name = f"global_payloads_vs_year_by_simple_payload_category"

simple_payload_categories = mda.Translation.payload_category_to_simple_payload_category.values()

# Only include payloads with a simple payload category, which probably means orbital payloads
mda.Filters.filter_by_simple_payload_category(dataset.satcat, simple_payload_categories)

dataset.satcat.df['Launch_Year'] = dataset.satcat.df['Launch_Date'].dt.year

os.makedirs(f'examples/outputs/raw_dataframes/global', exist_ok=True)
dataset.satcat.df.to_csv(f'examples/outputs/raw_dataframes/global/{output_name}.csv', index=False)
print(f"Dataframe 'raw_dataframe_{output_name}.csv' has been created.")

dataframes = mda.ChartUtils.group_dataset_into_dictionary_by_filter_function(
    dataset.satcat,
    filter_function=mda.Filters.filter_by_simple_payload_category,
    groups=simple_payload_categories,
    groupby_col="Launch_Year",
    count_values=True,
)

output_df = mda.ChartUtils.combine_dictionary_of_dataframes(dataframes)

os.makedirs(f'examples/outputs/csv/global', exist_ok=True)
output_df.to_csv(f"examples/outputs/csv/global/{output_name}.csv", index=True)
print(f"CSV file '{output_name}.csv' has been created.")

os.makedirs(f'examples/outputs/chart/global', exist_ok=True)
mda.ChartUtils.plot_bar(
    output_df,
    title="Global Payloads vs Year by Simple Payload Category",
    subtitle=f'Christopher Kalitin 2025 - Data Source: Jonathan McDowell - Data Cutoff: {dataset.date_updated}',
    x_label="Year",
    y_label="Number of Payloads",
    output_path=f'examples/outputs/chart/global/{output_name}.png',
    color_map=mda.ChartUtils.simple_payload_category_color_map,
    bargap=0.0,
    x_tick0=0,
    x_tick_step_size=5
)