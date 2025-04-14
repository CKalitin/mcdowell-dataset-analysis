import mcdowell_dataset_analysis as mda
import pandas as pd

launch_dataset = mda.Launch()
satcat_dataset = mda.Satcat()

launch_dataset.process_satcat_dependent_columns(satcat_dataset)
satcat_dataset.process_launch_dependent_columns(launch_dataset)

mda.Filters.filter_by_launch_date(launch_dataset, start_date="2000-01-01", end_date="2020-01-01")
mda.Filters.filter_by_launch_site_raw(satcat_dataset, "VSFB")

#pd.set_option('display.max_columns', 200)
print(satcat_dataset.df.head(20))
satcat_dataset.reload()
print(satcat_dataset.df.head(20))