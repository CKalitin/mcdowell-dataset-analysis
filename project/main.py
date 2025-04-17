import mcdowell_dataset_analysis as mda
import pandas as pd

dataset = mda.McdowellDataset()

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#mda.Filters.filter_by_launch_vehicle_family(dataset.satcat, launch_vehicle_families=["Falcon9"])
mda.Filters.filter_by_launch_date(dataset.satcat, start_date="1957-10-01", end_date="1958-10-25")
#mda.Filters.filter_by_launch_category(dataset.launch, launch_categories=["O"])
#mda.Filters.filter_by_launch_success_fraction(dataset.launch, "S")

print(dataset.satcat.df.head(20))  # Display the first few rows of the DataFrame for verification