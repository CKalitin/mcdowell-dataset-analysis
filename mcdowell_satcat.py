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
        
        dtypes = {
            "JCAT": str,
            "SatcatLaunch_Tag": str,
            "Piece": str,
            "Type": str,
            "Name": str,
            "PLName": str,
            "LDate": str, # Load as string to clean later
            "Parent": str,
            "SDate": str,
            "Primary": str,
            "DDate": str,
            "Status": str,
            "Dest": str,
            "Owner": str,
            "State": str,
            "Manufacturer": str,
            "Bus": str,
            "Motor": str,
            "Mass": str, # Handle ? and mixed types
            "DryMass": str,
            "TotMass": str,
            "Length": str,
            "Diamete": str, # Note: 'Diamete' seems misspelled in dataset
            "Span": str,
            "Shape": str,
            "ODate": str,
            "Perigee": str,
            "Apogee": str,
            "Inc": str,
            "OpOrbitOQU": str,
            "AltNames": str
        }
        
        self.satcat_df = pd.read_csv(self.file_path, sep="\t", encoding="utf-8", dtype=dtypes, low_memory=False)
        
        self.preprocess_satcat_df()

    def preprocess_satcat_df(self):
        """
        Create new columns from existing columns in satcat dataframe to make it more pandas friendly.
        """
        
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
        self.satcat_df["Launch_Date_Pandas"] = pd.to_datetime(self.satcat_df["LDate"], format="%Y %b %d", errors="coerce")
        self.satcat_df["Separation_Date_Pandas"] = pd.to_datetime(self.satcat_df["SDate"], format="%Y %b %d", errors="coerce")
        self.satcat_df["Decay_Date_Pandas"] = pd.to_datetime(self.satcat_df["DDate"], format="%Y %b %d", errors="coerce")
        self.satcat_df["Canonical_Orbit_Date_Pandas"] = pd.to_datetime(self.satcat_df["ODate"], format="%Y %b %d", errors="coerce") # This is the date on which the orbit data was taken

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
            self.satcat_df = self.satcat_df[self.satcat_df["Launch_Date_Pandas"] >= start_date]
        
        if end_date is not None:
            self.satcat_df = self.satcat_df[self.satcat_df["Launch_Date_Pandas"] <= end_date]

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
            self.satcat_df = self.satcat_df[self.satcat_df["Decay_Date_Pandas"] >= start_date]
        
        if end_date is not None:
            self.satcat_df = self.satcat_df[self.satcat_df["Decay_Date_Pandas"] <= end_date]


pd.set_option('display.max_columns', None)
        
dataset = McDowellSatcat()
dataset.filter_by_launch_date(start_date="2000-01-01", end_date="2000-02-01")

print(dataset.satcat_df.head(20))  # Display the first few rows of the DataFrame for verification
