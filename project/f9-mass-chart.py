import mcdowell_dataset_analysis as mda
import pandas as pd
import numpy as np
import copy

dataset = mda.McdowellDataset()

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Example: Generate a CSV for a chart of launches vs. payload mass range with each orbit type as a separate column

# First, sort by orbital launches from America
# Next, separate dataframe into each orbit type (columns)
# Next for each dataframe count the number of launches in each payload mass range (rows)
# Finally, join the dataframes together into a single dataframe with the payload mass range as the index and the orbit types as columns

mda.Filters.filter_by_launch_category(dataset.launch, ['O', 'D']) # Filter for orbital and deep space launches
mda.Filters.filter_by_launch_vehicle_family(dataset.launch, 'Falcon9') # Filter for F9 and F9 Heavy

#print(dataset.launch.df.value_counts('Simple_Orbit'))
#print(dataset.launch.df.value_counts('Simple_Orbit').sum())

#print(dataset.launch.df.head(500))

#orbits = dataset.launch.df['Simple_Orbit'].unique()
#orbits = orbits[pd.notna(orbits)].tolist()  # Remove NaN values from the unique orbits and convert to python list
orbits = ['LEO','SSO','MEO','GTO','GEO','HEO','BEO'] # Just do it manually to get the order I want

# Separate the dataframe into many dataframes for each orbit type (columns)
orbit_dfs = {}
for orbit in orbits:
    orbit_df = copy.copy(dataset.launch)
    mda.Filters.filter_by_orbit(orbit_df, orbit)
    orbit_dfs[orbit] = orbit_df

# Count the number of launches in each payload mass range (rows)
bins = [0,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000,12000,13000,14000,15000,16000,17000,18000,19000,20000]
mass_labels = ['0-1T','1-2T','2-3T','3-4T','4-5T','5-6T','6-7T','7-8T','8-9T','9-10T','10-11T','11-12T','12-13T','13-14T','14-15T','15-16T','16-17T','17-18T','18-19T','19-20T']

orbit_counts = {}

for orbit, orbit_df in orbit_dfs.items():
    orbit_counts[orbit] = pd.cut(orbit_df.df['Payload_Mass'], bins=bins, labels=mass_labels, include_lowest=True).value_counts()
    orbit_counts[orbit] = orbit_counts[orbit].reindex(mass_labels)  # Reindex to ensure all mass ranges in the right order

# Now create a new dataframe with the payload mass range as the index and the orbit types as columns
# Y axis should be mass ranges, x axis should be orbit types

output_df = pd.DataFrame(index=mass_labels, columns=orbits)
output_df = pd.concat(orbit_counts.values(), axis=1) # Concatenate the dataframes along the columns
output_df.columns = orbit_counts.keys()
#output_df = output_df.drop(index=1).reset_index(drop=True)

print(output_df.head(20))

output_df.to_csv('output.csv', index=True) # Save the dataframe to a CSV file