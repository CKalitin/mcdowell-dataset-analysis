# preprocess_satcat_df()
Create new columns from existing columns in satcat dataframe to make it more pandas friendly.
Lots of string manipulation to get the dates into a format that pandas can understand.

Strip Launch_Tags so that it's synced with the Launch dataframe.
Fix Dates.
Convert mass to floats (in kg) and handle NaN.

### Date Columns:
We create the following date columns from the original SATCAT data (in pandas datetime format):
- Launch Date (LDate)
- Separation Date (SDate) - separation from the launch vehicle
- Decay Date (DDate)
- Canonical Orbit Date (ODate) - date of the first TLE in the catalog

Context for canonical orbit date:  
The following set of fields (ODate, Perigee, Apogee, Inc, OpOrbit, OQUAL) describe a 'canonical orbit'. The orbit of an object changes with time due to atmospheric drag and other perturbations, and in some cases it changes drastically due to active manuevering. I pick one orbit (the `canonical orbit') that is representative of the spacecraft's early operations, after initial positioning, to include in the catalog. But detailed analysis should consult detailed orbital data versus time for each object, from the Space-Track TLEs or other sources. 

Source: https://planet4589.org/space/gcat/web/cat/cols.html

# filter_by_sat_type_coarse()
Remove all launches that are not in the given launch categories.

Args:
    launch_categories: List of launch categories to filter by. eg. ["P", "R"]

### SatType Coarse Categories:  
P: Payload
C: Component
R: Launch vehicle stage
D: Fragmentation debris
S: Suborbital payload (e.g. sounding rocket payload or missile reentry vehicle)
X: Catalog entry that has been deleted (used in auxcat etc.)
Z: Spurious catalog entry (was in SATCAT, perhaps in TLEs, but there was no real object)

# filter_by_launch_date() & filter_by_decay_date()
Remove all launches that are not in the given date range (inclusive range).

Args:
1. start_date: Start date to filter by. eg. "2000-01-01"
2. end_date: End date to filter by. eg. "2020-01-01"