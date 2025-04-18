import mcdowell_dataset_analysis as mda
import pandas as pd

dataset = mda.McdowellDataset()

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#mda.Filters.filter_by_launch_vehicle_family(dataset.satcat, launch_vehicle_families=["Falcon9"])
mda.Filters.filter_by_launch_date(dataset.launch, start_date="2023-10-01")
mda.Filters.filter_by_launch_category(dataset.launch, launch_categories=["O"])
#mda.Filters.filter_by_launch_success_fraction(dataset.launch, "S")
#mda.Filters.filter_by_launch_vehicle_family(dataset.launch, launch_vehicle_families=["Electron"])

mda.Filters.filter_by_state_code(dataset.launch, state_codes=["IN"])

# sort by satellite type category, only payload
#mda.Filters.filter_by_sat_type_coarse(dataset.satcat, sat_types=["P"])
#mda.Filters.filter_by_payload_category_raw(dataset.satcat, payload_categories=["NAV"])
#mda.Filters.filter_by_inclination(dataset.satcat, min_inclination=75, max_inclination=90)  # Example values for perigee
#mda.Filters.filter_by_payload_program_raw(dataset.launch, payload_programs=["OneWeb"])

#print(dataset.launch.df.head(20))  # Display the first few rows of the DataFrame for verification

print(dataset.translation.org_to_state_code["IN-AP"])
print(dataset.translation.state_code_to_state_name[dataset.translation.org_to_state_code["IN-AP"]])