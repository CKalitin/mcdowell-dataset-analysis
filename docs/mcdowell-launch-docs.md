# process_satcat_dependent_columns()
Create columns in launch_df derived from satcat data:
- Payload_Mass: Sum of masses for all payloads in a launch
- Canonical_Orbit_Parameters: Dictionary of canonical orbit data from satcat
Args:
    satcat_df: DataFrame containing the satcat class. Note this isn't the mcdowell_satcat class

Create Payload_Mass column in launch_df that takes the sum of the masses of all payloads on the launch.
Note that this filters for only payloads (ie. with the "P" sat_type_coarse) and ignores any other types of objects (eg. "R" for rocket bodies).

Create canonical orbit parameters columns in launch_df that takes the canonical orbit data from the satcat_df and creates a dictionary of the following columns.
The canonical orbit parameters are intial orbit parameters taken for the payloads after launch. These are meant to be representative of the payloads' orbits after launch and are not updated with time. It's not a completely exact science, but it's a good approximation.

The columns are:
- ODate: Date on which the canonical orbit data was taken (in pandas datetime format)
- Perigee: Perigee altitude in km
- Apogee: Apogee altitude in km
- Inclination: Inclination in degrees
- OpOrbit: Orbit type (e.g. "GEO", "LEO", "HEO", "MEO", "SSO", "GTO", "TLI", "HLO", "HCO", "HPO")

# filter_by_launch_category()

Remove all launches that are not in the given launch categories.

Args:
    launch_categories: List of launch categories to filter by. eg. ["O", "S", "D"]

### Launch Categories:  
O: Orbital  
S: Suborbital (non-missile)  
D: Deep Space  
M: Military Missile  
T: Test Rocket  
A: Atmospheric Rocket  
H: High Altitude Sounding Rocket  
R: Reentry Test  
X: Launch from Non-Earth World  
Y: Suborbital Spaceplane (Human Crew)  

### Notes:  
- Categories O and D are reliable.  
- Other categories may not be consistently assigned.  
- Primarily used to distinguish orbital from non-orbital launches.  

Source: https://planet4589.org/space/gcat/web/launch/lcols.html

# filter_by_launch_success_fraction()
Remove all launches that are not in the given launch success fractions.

Args:
1. launch_success_fractions: List of launch success fractions to filter by. eg. ["S", "f"]

### Launch Success Fraction:  
S: Success (propulsive success, regardless of payload data)  
F: Failure  
U: Unknown  
E: Pad Explosion (no launch, included for completeness)  

Source: https://planet4589.org/space/gcat/web/launch/lcols.html

# filter_by_launch_date()
Remove all launches that are not in the given date range (inclusive range).

Args:
1. start_date: Start date to filter by. eg. "2000-01-01"
2. end_date: End date to filter by. eg. "2020-01-01"