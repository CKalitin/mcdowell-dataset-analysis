import pandas as pd
import mcdowell_satcat
import mcdowell_launch

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
        """
        
        if (type(dataset_class) != mcdowell_launch.Launch):
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
        """
        
        if (type(dataset_class) != mcdowell_launch.Launch):
            raise ValueError("launch dataset expected by filter_by_launch_success_fraction(). Cannot sort by launch success fraction in satcat dataset.")
        
        if (type(launch_success_fractions) == str):
            launch_success_fractions = [launch_success_fractions]
        
        dataset_class.df = dataset_class.df[
            dataset_class.df["Launch_Code"].str[1].isin(launch_success_fractions)
        ]

    def filter_by_launch_vehicle(dataset_class, launch_vehicles):
        """
        Remove all launches that are not in the given launch vehicles.
        Args:
            launch_vehicles: List of launch vehicles to filter by. eg. ["Electron", "Falcon 9"]
        """
        
        if (type(launch_vehicles) == str):
            launch_vehicles = [launch_vehicles]
        
        dataset_class.df = dataset_class.df[
            dataset_class.df["LV_Type"].isin(launch_vehicles)
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

    # TODO:
    # filter by launch country (state code), harder for launch since no country code, need sites! TODO: add site codes dataset
    # filter by simple category
    # filter by satellite category!
    # filter by simple orbit
    # filter by apogee
    # filter by perigee
    # filter by inclination
    # filter by launch pad
    # filter by satellite program (requires adding another dataset, psatcat)

    def filter_by_sat_type_coarse(dataset_class, sat_types):
        """
        Remove all launches that are not in the given launch categories.
        Args:
            launch_categories: List of launch categories to filter by. eg. ["P", "R"]
        """

        if (type(dataset_class) != mcdowell_satcat.Satcat):
            raise ValueError("satcat dataset expected by filter_by_sat_type_coarse(). Cannot sort by sat type in launch dataset.")
        
        if (type(sat_types) == str):
            sat_types = [sat_types]
        
        # vectorized operation to filter the DataFrame
        # Faster than a for loop for some reason, kind vibe coding here tbh
        dataset_class.df = dataset_class.df[
            dataset_class.df["Type"].str[0].isin(sat_types)
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
        
        if (type(dataset_class) != mcdowell_satcat.Satcat):
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
        
        if (type(dataset_class) != mcdowell_satcat.Satcat):
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
        
        if (type(dataset_class) != mcdowell_satcat.Satcat):
            raise ValueError("satcat dataset class expected by filter_by_orbit_canonical_date(). Cannot sort by orbit canonical date in launch dataset.")
        
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
        
        if start_date is not None:
            dataset_class.df = dataset_class.df[dataset_class.df["Orbit_Canonical_Date"] >= start_date]
        
        if end_date is not None:
            dataset_class.df = dataset_class.df[dataset_class.df["Orbit_Canonical_Date"] <= end_date]

if __name__ == "__main__":
    pd.set_option('display.max_columns', 200)

    satcat = mcdowell_satcat.Satcat()
    launch = mcdowell_launch.Launch()

    launch.process_satcat_dependent_columns(satcat.df)
    satcat.process_launch_dependent_columns(launch.df)

    Filters.filter_by_launch_pad(satcat, ["LC39A"])

    print(satcat.df.head(20))  # Display the first few rows of the DataFrame for verification