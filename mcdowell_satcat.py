import pandas as pd
import numpy as np

class McDowellSatcat:
    """
    This contains all functions required for using McDowell's satellite catalog dataset. This includes filtering the dataset by year, etc.
    """

    def __init__(self, file_path="datasets/satcat.tsv"):
        """
        Load the raw satcat dataset into a pandas DataFrame.
        
        satcat.tsv column descriptions: https://planet4589.org/space/gcat/web/cat/cols.html
        """
        
        self.file_path = file_path
        
        self.satcat_df = pd.read_csv(self.file_path, sep="\t", encoding="utf-8", low_memory=False)
        
        self.preprocess_satcat_df()

    def preprocess_satcat_df(self):
        """
        Create new columns from existing columns in satcat dataframe to make it more pandas friendly.
        Lots of string manipulation to get the dates into a format that pandas can understand.
        """

        # Strip Launch_Tags
        self.satcat_df["Launch_Tag"] = self.satcat_df["Launch_Tag"].astype(str).str.upper().str.strip()
        
        # Replace double space "  " with single space " " - Sputnik 1 edge case!
        self.satcat_df["LDate"] = self.satcat_df["LDate"].str.replace(r"\s{2,}", " ", regex=True).str.strip()
        self.satcat_df["SDate"] = self.satcat_df["SDate"].str.replace(r"\s{2,}", " ", regex=True).str.strip()
        self.satcat_df["DDate"] = self.satcat_df["DDate"].str.replace(r"\s{2,}", " ", regex=True).str.strip()
        self.satcat_df["ODate"] = self.satcat_df["ODate"].str.replace(r"\s{2,}", " ", regex=True).str.strip()
    
        # Remove problematic characters from date columns (?, -) and handle NaN
        self.satcat_df["LDate"] = self.satcat_df["LDate"].fillna("").str.replace(r"[?-]", "", regex=True).str.strip()
        self.satcat_df["SDate"] = self.satcat_df["SDate"].fillna("").str.replace(r"[?-]", "", regex=True).str.strip()
        self.satcat_df["DDate"] = self.satcat_df["DDate"].fillna("").str.replace(r"[?-]", "", regex=True).str.strip()
        self.satcat_df["ODate"] = self.satcat_df["ODate"].fillna("").str.replace(r"[?-]", "", regex=True).str.strip()
        
        # Only include characters before the third space in all date columns (Remove hour/min/sec as unneeded and messes with data frame time formatting)
        self.satcat_df["LDate"] = self.satcat_df["LDate"].str.split(" ", n=3).str[:3].str.join(" ").str.strip()
        self.satcat_df["SDate"] = self.satcat_df["SDate"].str.split(" ", n=3).str[:3].str.join(" ").str.strip()
        self.satcat_df["DDate"] = self.satcat_df["DDate"].str.split(" ", n=3).str[:3].str.join(" ").str.strip()
        self.satcat_df["ODate"] = self.satcat_df["ODate"].str.split(" ", n=3).str[:3].str.join(" ").str.strip()
        
        # Add " 1" to the end of all dates that only contain year and month (assuming this is all 8 character dates) eg. "2023 Feb" -> "2023 Feb 1"
        self.satcat_df["LDate"] = self.satcat_df["LDate"].where(self.satcat_df["LDate"].str.len() != 8, self.satcat_df["LDate"] + " 1")
        self.satcat_df["SDate"] = self.satcat_df["SDate"].where(self.satcat_df["SDate"].str.len() != 8, self.satcat_df["SDate"] + " 1")
        self.satcat_df["DDate"] = self.satcat_df["DDate"].where(self.satcat_df["DDate"].str.len() != 8, self.satcat_df["DDate"] + " 1")
        self.satcat_df["ODate"] = self.satcat_df["ODate"].where(self.satcat_df["ODate"].str.len() != 8, self.satcat_df["ODate"] + " 1")
        
        # Convert Mcdowell's Vague date format to pandas datetime format
        self.satcat_df["LDate"] = pd.to_datetime(self.satcat_df["LDate"], format="%Y %b %d", errors="coerce")
        self.satcat_df["SDate"] = pd.to_datetime(self.satcat_df["SDate"], format="%Y %b %d", errors="coerce")
        self.satcat_df["DDate"] = pd.to_datetime(self.satcat_df["DDate"], format="%Y %b %d", errors="coerce")
        self.satcat_df["ODate"] = pd.to_datetime(self.satcat_df["ODate"], format="%Y %b %d", errors="coerce") # This is the date on which the orbit data was taken

        # Convert mass to float (in kg) and handle NaN
        self.satcat_df["Mass"] = pd.to_numeric(self.satcat_df["Mass"], errors="coerce").fillna(0)
        self.satcat_df["DryMass"] = pd.to_numeric(self.satcat_df["DryMass"], errors="coerce").fillna(0)
        self.satcat_df["TotMass"] = pd.to_numeric(self.satcat_df["TotMass"], errors="coerce").fillna(0)
        
        # Create Simplified Orbit Column
        # Orbits: https://planet4589.org/space/gcat/web/intro/orbits.html
        self.satcat_df["Simplified_Orbit"] = self.satcat_df["OpOrbit"].str.split(" ", n=1).str[0].str.strip()
        self.satcat_df["Simplified_Orbit"] = self.satcat_df["Simplified_Orbit"].replace(
            {
                "ATM": "SO",      # Atmospheric
                "SO": "SO",        # Suborbital
                "TA": "SO",        # Trans-Atmospheric
                "LLEO/E": "LEO",   # Lower LEO/Equatorial
                "LLEO/I": "LEO",   # Lower LEO/Intermediate
                "LLEO/P": "SSO",   # Lower LEO/Polar
                "LLEO/S": "SSO",   # Lower LEO/Sun-Sync
                "LLEO/R": "LEO",   # Lower LEO/Retrograde
                "LEO/E": "LEO",    # Upper LEO/Equatorial
                "LEO/I": "LEO",    # Upper LEO/Intermediate
                "LEO/P": "SSO",    # Upper LEO/Polar
                "LEO/S": "SSO",    # Upper LEO/Sun-Sync
                "LEO/R": "LEO",    # Upper LEO/Retrograde
                "MEO": "MEO",      # Medium Earth Orbit
                "HEO": "HEO",      # Highly Elliptical Orbit
                "HEO/M": "HEO",    # Molniya
                "GTO": "GTO",      # Geotransfer
                "GEO/S": "GEO",    # Stationary
                "GEO/I": "GEO",    # Inclined GEO
                "GEO/T": "GEO",    # Synchronous
                "GEO/D": "GEO",    # Drift GEO
                "GEO/SI": "GEO",   # Inclined GEO (same as GEO/I)
                "GEO/ID": "GEO",   # Inclined Drift
                "GEO/NS": "GEO",   # Near-sync
                "VHEO": "HEO",    # Very High Earth Orbit
                "DSO": "BEO",      # Deep Space Orbit
                "CLO": "BEO",      # Cislunar/Translunar
                "EEO": "BEO",      # Earth Escape
                "HCO": "BEO",      # Heliocentric
                "PCO": "BEO",      # Planetocentric
                "SSE": "BEO"       # Solar System Escape
            }
        )
        
    def filter_by_sat_type_coarse(self, sat_types):
        """
        Remove all launches that are not in the given launch categories.
        Args:
            launch_categories: List of launch categories to filter by. eg. ["P", "R"]
        """
        
        # vectorized operation to filter the DataFrame
        # Faster than a for loop for some reason, kind vibe coding here tbh
        self.satcat_df = self.satcat_df[
            self.satcat_df["Type"].str[0].isin(sat_types)
        ]
        
    def filter_by_launch_date(self, start_date=None, end_date=None):
        """
        Remove all launches that are not in the given date range (inclusive range).
        Args:
            start_date: Start date to filter by. eg. "2000-01-01"
            end_date: End date to filter by. eg. "2020-01-01"
        """
        
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
        
        if start_date is not None:
            self.satcat_df = self.satcat_df[self.satcat_df["LDate"] >= start_date]
        
        if end_date is not None:
            self.satcat_df = self.satcat_df[self.satcat_df["LDate"] <= end_date]

    def filter_by_decay_date(self, start_date=None, end_date=None):
        """
        Remove all launches that are not in the given date range (inclusive range).
        Args:
            start_date: Start date to filter by. eg. "2000-01-01"
            end_date: End date to filter by. eg. "2020-01-01"
        """
        
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
        
        if start_date is not None:
            self.satcat_df = self.satcat_df[self.satcat_df["DDate"] >= start_date]
        
        if end_date is not None:
            self.satcat_df = self.satcat_df[self.satcat_df["DDate"] <= end_date]

    # TODO:
    # Create a separate filter script so they are synced between satcat and launch
    
if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
            
    dataset = McDowellSatcat()
    dataset.filter_by_launch_date(start_date="2000-01-01", end_date="2000-02-01")
    dataset.filter_by_sat_type_coarse(["P"])

    print(dataset.satcat_df.head(20))  # Display the first few rows of the DataFrame for verification
