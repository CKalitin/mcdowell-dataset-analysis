import mcdowell_dataset_analysis as mda
import pandas as pd

launch_dataset = mda.Launch()
satcat_dataset = mda.Satcat()

launch_dataset.process_satcat_dependent_columns(satcat_dataset)
satcat_dataset.process_launch_dependent_columns(launch_dataset)

mda.Filters.filter_by_launch_date(launch_dataset, start_date="2017-01-01", end_date="2025-01-01")
mda.Filters.filter_by_mass(launch_dataset, min_mass=5000, max_max=10000)
mda.Filters.filter_by_launch_vehicle(launch_dataset, launch_vehicles=["Falcon 9"])
mda.Filters.filter_by_orbit(launch_dataset, orbits=["GEO"])

pd.set_option('display.max_columns', 200)
print(launch_dataset.df.head(20))