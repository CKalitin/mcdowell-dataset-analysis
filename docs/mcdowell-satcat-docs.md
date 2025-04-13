# filter_by_sat_type_coarse
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

# preprocess_satcat_df

### Date Columns:
We create the following date columns from the original SATCAT data (in pandas datetime format):
- Launch Date (Launch_Date_Pandas)
- Separation Date (Separation_Date_Pandas) - separation from the launch vehicle
- Decay Date (Decay_Date_Pandas)
- Canonical Orbit Date (Canonical_Orbit_Date_Pandas) - date of the first TLE in the catalog

Context for canonical orbit date:  
The following set of fields (ODate, Perigee, Apogee, Inc, OpOrbit, OQUAL) describe a 'canonical orbit'. The orbit of an object changes with time due to atmospheric drag and other perturbations, and in some cases it changes drastically due to active manuevering. I pick one orbit (the `canonical orbit') that is representative of the spacecraft's early operations, after initial positioning, to include in the catalog. But detailed analysis should consult detailed orbital data versus time for each object, from the Space-Track TLEs or other sources. 

Source: https://planet4589.org/space/gcat/web/cat/cols.html