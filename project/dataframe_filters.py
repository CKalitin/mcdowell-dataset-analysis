import pandas as pd
import dataset_satcat
import dataset_launch

# TODO:
# filter by launch country (state code), harder for launch since no country code, need sites! TODO: add site codes dataset
# filter by satellite program (requires adding another dataset, psatcat)
# filter by simplified launch site
# filter by simplified launch pad
    
class Filters:
    """
    This class contains all functions required for filtering the datasets. This includes filtering by date, launch vehicle, launch site, etc.
    """

    def __init__(self):
        pass

    def filter_by_launch_category(dataset_class, launch_categories):
        """
        Remove all launches that are not in the given launch categories.
        Args:
            launch_categories: List of launch categories to filter by. eg. ["O", "R", "M"]
            
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
        Source: https://planet4589.org/space/gcat/web/launch/lcols.html  
        """
        
        if (type(dataset_class) != dataset_launch.Launch):
            raise ValueError("launch dataset expected by filter_by_launch_category(). Cannot sort by launch category in satcat dataset.")
        
        if (type(launch_categories) == str):
            launch_categories = [launch_categories]
        
        # vectorized operation to filter the DataFrame
        # Faster than a for loop for some reason, kind vibe coding here tbh
        dataset_class.df = dataset_class.df[
            dataset_class.df["Launch_Code"].str[0].isin(launch_categories)
        ]
        
    def filter_by_launch_success_fraction(dataset_class, launch_success_fractions):
        """
        Remove all launches that are not in the given launch success fractions.
        Args:
            launch_success_fractions: List of launch success fractions to filter by. eg. ["S", "F"]
            
        S: Success (propulsive success, regardless of payload data)  
        F: Failure  
        U: Unknown  
        E: Pad Explosion (no launch, included for completeness)  
        Source: https://planet4589.org/space/gcat/web/launch/lcols.html
        """
        
        if (type(dataset_class) != dataset_launch.Launch):
            raise ValueError("launch dataset expected by filter_by_launch_success_fraction(). Cannot sort by launch success fraction in satcat dataset.")
        
        if (type(launch_success_fractions) == str):
            launch_success_fractions = [launch_success_fractions]
        
        dataset_class.df = dataset_class.df[
            dataset_class.df["Launch_Code"].str[1].isin(launch_success_fractions)
        ]

    def filter_by_launch_vehicle_raw(dataset_class, launch_vehicles):
        """
        Remove all launches that are not in the given launch vehicles.
        Args:
            launch_vehicles: List of launch vehicles to filter by. eg. ["Kosmos 11K65M", "Falcon 9", "Starship V1.0 Ship"]
        Launch Vehicle List: https://planet4589.org/space/gcat/data/tables/lv.html
        """
        
        if (type(launch_vehicles) == str):
            launch_vehicles = [launch_vehicles]
        
        dataset_class.df = dataset_class.df[
            dataset_class.df["LV_Type"].isin(launch_vehicles)
        ]
        
    def filter_by_launch_vehicle_family(dataset_class, launch_vehicle_families):
        """
        Remove all launches that are not in the given launch vehicle families.
        Args:
            launch_vehicle_families: List of launch vehicles to filter by. eg. ["Electron", "Falcon9"]
        Launch Vehicle Family List: https://planet4589.org/space/gcat/data/tables/family.html  
        Launch Vehicle List (With Family): https://planet4589.org/space/gcat/data/tables/lv.html
        """
        
        if (type(launch_vehicle_families) == str):
            launch_vehicle_families = [launch_vehicle_families]
        
        dataset_class.df = dataset_class.df[
            dataset_class.df["Launch_Vehicle_Family"].isin(launch_vehicle_families)
        ]

    def filter_by_launch_site_raw(dataset_class, launch_sites):
        """
        Remove all launches that are not in the given launch sites.
        Args:
            launch_sites: List of launch sites to filter by. eg. ["VFSB", "KSC"]
        """
        
        if (type(launch_sites) == str):
            launch_sites = [launch_sites]
            
        dataset_class.df = dataset_class.df[
            dataset_class.df["Launch_Site"].isin(launch_sites)
        ]

    def filter_by_launch_pad_raw(dataset_class, launch_pads):
        """
        Remove all launches that are not in the given launch pads.
        Args:
            launch_pads: List of launch pads to filter by. eg. ["SLC4E", "LC39A"]
        """
        
        if (type(launch_pads) == str):
            launch_pads = [launch_pads]
        
        dataset_class.df = dataset_class.df[
            dataset_class.df["Launch_Pad"].isin(launch_pads)
        ]

    def filter_by_sat_type_coarse(dataset_class, sat_types):
        """
        Remove all launches that are not in the given launch categories.
        Args:
            launch_categories: List of launch categories to filter by. eg. ["P", "R"]
        """

        if (type(dataset_class) != dataset_satcat.Satcat):
            raise ValueError("satcat dataset expected by filter_by_sat_type_coarse(). Cannot sort by sat type in launch dataset.")
        
        if (type(sat_types) == str):
            sat_types = [sat_types]
        
        # vectorized operation to filter the DataFrame
        # Faster than a for loop for some reason, kind vibe coding here tbh
        dataset_class.df = dataset_class.df[
            dataset_class.df["Type"].str[0].isin(sat_types)
        ]
    
    def filter_by_payload_category_raw(dataset_class, payload_categories):
        """
        Remove all launches that are not in the given payload types.
        Args:
            payload_categories: List of payload types to filter by. eg. ["Other", "Communications"]
        """
        
        if (type(dataset_class) != dataset_satcat.Satcat):
            raise ValueError("satcat dataset expected by filter_by_payload_category_raw(). Cannot sort by sat type in launch dataset.")
        
        if (type(payload_categories) == str):
            payload_categories = [payload_categories]
        
        # vectorized operation to filter the DataFrame
        # Faster than a for loop for some reason, kind vibe coding here tbh
        dataset_class.df = dataset_class.df[
            dataset_class.df["Payload_Category"].isin(payload_categories)
        ]
    
    def filter_by_simple_payload_category(dataset_class, payload_categories):
        """
        Remove all launches that are not in the given payload types.
        Args:
            payload_categories: List of payload types to filter by. eg. ["Other", "Communications"]
        """
        
        if (type(dataset_class) != dataset_satcat.Satcat):
            raise ValueError("satcat dataset expected by filter_by_simple_payload_type(). Cannot sort by sat type in launch dataset.")
        
        if (type(payload_categories) == str):
            payload_categories = [payload_categories]
        
        # vectorized operation to filter the DataFrame
        # Faster than a for loop for some reason, kind vibe coding here tbh
        dataset_class.df = dataset_class.df[
            dataset_class.df["Simple_Payload_Category"].isin(payload_categories)
        ]
        
    def filter_by_launch_date(dataset_class, start_date=None, end_date=None):
        """
        Remove all launches that are not in the given date range (inclusive range).
        Args:
            start_date: Start date to filter by. eg. "2000-01-01"
            end_date: End date to filter by. eg. "2020-01-01"
        """
        
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
        
        if start_date is not None:
            dataset_class.df = dataset_class.df[dataset_class.df["Launch_Date"] >= start_date]
        
        if end_date is not None:
            dataset_class.df = dataset_class.df[dataset_class.df["Launch_Date"] <= end_date]

    def filter_by_separation_date(dataset_class, start_date=None, end_date=None):
        """
        Remove all launches that are not in the given date range (inclusive range).
        Args:
            start_date: Start date to filter by. eg. "2000-01-01"
            end_date: End date to filter by. eg. "2020-01-01"
        """
        
        if (type(dataset_class) != dataset_satcat.Satcat):
            raise ValueError("satcat dataset expected by filter_by_separation_date(). Cannot sort by separation date in launch dataset.")
        
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
        
        if start_date is not None:
            dataset_class.df = dataset_class.df[dataset_class.df["Separation_Date"] >= start_date]
        
        if end_date is not None:
            dataset_class.df = dataset_class.df[dataset_class.df["Separation_Date"] <= end_date]

    def filter_by_decay_date(dataset_class, start_date=None, end_date=None):
        """
        Remove all launches that are not in the given date range (inclusive range).
        Args:
            start_date: Start date to filter by. eg. "2000-01-01"
            end_date: End date to filter by. eg. "2020-01-01"
        """
        
        if (type(dataset_class) != dataset_satcat.Satcat):
            raise ValueError("satcat dataset  expected by filter_by_decay_date(). Cannot sort by decay date in launch dataset.")
        
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
        
        if start_date is not None:
            dataset_class.df = dataset_class.df[dataset_class.df["Decay_Date"] >= start_date]
        
        if end_date is not None:
            dataset_class.df = dataset_class.df[dataset_class.df["Decay_Date"] <= end_date]

    def filter_by_orbit_canonical_date(dataset_class, start_date=None, end_date=None):
        """
        Remove all launches that are not in the given date range (inclusive range).
        Args:
            start_date: Start date to filter by. eg. "2000-01-01"
            end_date: End date to filter by. eg. "2020-01-01"
        """
        
        if (type(dataset_class) != dataset_satcat.Satcat):
            raise ValueError("satcat dataset class expected by filter_by_orbit_canonical_date(). Cannot sort by orbit canonical date in launch dataset.")
        
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
        
        if start_date is not None:
            dataset_class.df = dataset_class.df[dataset_class.df["Orbit_Canonical_Date"] >= start_date]
        
        if end_date is not None:
            dataset_class.df = dataset_class.df[dataset_class.df["Orbit_Canonical_Date"] <= end_date]
    
    def filter_by_mass(dataset_class, min_mass=None, max_max=None):
        """
        Remove all launches or satellties that are not in the given mass range (inclusive range).
        Args:
            dataset_class: launch or satcat
            min_mass (float, optional): Minimum mass (inclusive). Defaults to None.
            max_max (float, optional): Maximum mass (inclusive). Defaults to None.
        """
        
        mass_col = "Payload_Mass"
        if (type(dataset_class) == dataset_satcat.Satcat):
            mass_col = "Mass"
            
        if min_mass is not None:
            dataset_class.df = dataset_class.df[dataset_class.df[mass_col] >= min_mass]
        
        if max_max is not None:
            dataset_class.df = dataset_class.df[dataset_class.df[mass_col] <= max_max]
            
    def filter_by_orbit_raw(dataset_class, orbits):
        """
        Remove all launches that are not in the given orbit. This uses Jonathan McDowell's raw orbit tags. Eg. "LLEO/I", "VHEO", "DSO", "GEO/NS"
        See https://planet4589.org/space/gcat/web/intro/orbits.html for more information.
        Args:
            dataset_class: launch or satcat
            orbit (string or string array): orbit tag, see: https://planet4589.org/space/gcat/web/intro/orbits.html
        """
        
        if type(orbits) == str:
            orbits = [orbits]
        
        dataset_class.df = dataset_class.df[
            dataset_class.df["OpOrbit"].isin(orbits)
        ]

    def filter_by_orbit(dataset_class, orbits):
        """
        Remove all launches that are not in the given orbit. This uses simple orbit categories. Eg. "LEO", "MEO", "GTO", "BEO"
        Args:
            dataset_class: launch or satcat
            orbits (string or string array): simple orbit tags 
        """
        
        if type(orbits) == str:
            orbits = [orbits]
            
        dataset_class.df = dataset_class.df[
            dataset_class.df["Simple_Orbit"].isin(orbits)
        ]

    def filter_by_apogee(dataset_class, min_apogee=None, max_apogee=None):
        """
        Remove all launches that are not in the given apogee range (inclusive range).
        Args:
            dataset_class: launch or satcat
            min_apogee (float, optional): Minimum apogee (inclusive). Defaults to None.
            max_apogee (float, optional): Maximum apogee (inclusive). Defaults to None.
        """
        
        if min_apogee is not None:
            dataset_class.df = dataset_class.df[dataset_class.df["Apogee"] >= min_apogee]
        
        if max_apogee is not None:
            dataset_class.df = dataset_class.df[dataset_class.df["Apogee"] <= max_apogee]
    
    def filter_by_perigee(dataset_class, min_perigee=None, max_perigee=None):
        """
        Remove all launches that are not in the given perigee range (inclusive range).
        Args:
            dataset_class: launch or satcat
            min_perigee (float, optional): Minimum perigee (inclusive). Defaults to None.
            max_perigee (float, optional): Maximum perigee (inclusive). Defaults to None.
        """
        
        if min_perigee is not None:
            dataset_class.df = dataset_class.df[dataset_class.df["Perigee"] >= min_perigee]
        
        if max_perigee is not None:
            dataset_class.df = dataset_class.df[dataset_class.df["Perigee"] <= max_perigee]

    def filter_by_inclination(dataset_class, min_inclination=None, max_inclination=None):
        """
        Remove all launches that are not in the given inclination range (inclusive range).
        Args:
            dataset_class: launch or satcat
            min_inclination (float, optional): Minimum inclination (inclusive). Defaults to None.
            max_inclination (float, optional): Maximum inclination (inclusive). Defaults to None.
        """
        
        if min_inclination is not None:
            dataset_class.df = dataset_class.df[dataset_class.df["Inc"] >= min_inclination]
        
        if max_inclination is not None:
            dataset_class.df = dataset_class.df[dataset_class.df["Inc"] <= max_inclination]
    

# For testing
if __name__ == "__main__":
    pd.set_option('display.max_columns', 200)

    satcat = dataset_satcat.Satcat()
    launch = dataset_launch.Launch()

    launch.process_satcat_dependent_columns(satcat.df)
    satcat.process_launch_dependent_columns(launch.df)

    Filters.filter_by_launch_pad(satcat, ["LC39A"])

    print(satcat.df.head(20))  # Display the first few rows of the DataFrame for verification