import mcdowell_dataset_analysis as mda
import pandas as pd

launch = mda.Launch()
satcat = mda.Satcat()

launch.process_satcat_dependent_columns(satcat.df)
satcat.process_launch_dependent_columns(launch.df)

mda.Filters.filter_by_launch_date(launch, start_date="2000-01-01", end_date="2020-01-01")
mda.Filters.filter_by_launch_site_raw(satcat, "VSFB")

#pd.set_option('display.max_columns', 200)
print(satcat.df.head(20))
satcat.reload()
print(satcat.df.head(20))