# filter_by_launch_category:

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

# filter_by_launch_success_fraction
Remove all launches that are not in the given launch success fractions.

Args:
1. launch_success_fractions: List of launch success fractions to filter by. eg. ["S", "f"]

### Launch Success Fraction:  
S: Success (propulsive success, regardless of payload data)  
F: Failure  
U: Unknown  
E: Pad Explosion (no launch, included for completeness)  

Source: https://planet4589.org/space/gcat/web/launch/lcols.html

# filter_by_date
Remove all launches that are not in the given date range (inclusive range).

Args:
1. start_date: Start date to filter by. eg. "2000-01-01"
2. end_date: End date to filter by. eg. "2020-01-01"