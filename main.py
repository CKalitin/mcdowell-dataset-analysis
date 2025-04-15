import mcdowell_dataset_analysis as mda
import pandas as pd

launch_dataset = mda.Launch()
satcat_dataset = mda.Satcat()

launch_dataset.process_satcat_dependent_columns(satcat_dataset)
satcat_dataset.process_launch_dependent_columns(launch_dataset)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

print(type(launch_dataset))

mda.Filters.filter_by_launch_date(launch_dataset, start_date="1957-10-01", end_date="1958-10-25")
mda.Filters.filter_by_launch_category(launch_dataset, launch_categories=["O"])
mda.Filters.filter_by_launch_success_fraction(launch_dataset, "S")

print(launch_dataset.df.head(20))  # Display the first few rows of the DataFrame for verification