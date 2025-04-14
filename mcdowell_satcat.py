import pandas as pd
import numpy as np
import mcdowell_launch

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
        
        self.df = pd.read_csv(self.file_path, sep="\t", encoding="utf-8", low_memory=False) # load csv into dataframe
        
        self.preprocess_satcat_df()

    def preprocess_satcat_df(self):
        """
        Create new columns from existing columns in satcat dataframe to make it more pandas friendly.
        Lots of string manipulation to get the dates into a format that pandas can understand.
        """

        # Rename column "#Launch_Tag" to "Launch_Tag"
        self.df.rename(columns={"#JCAT": "JCAT"}, inplace=True)
        
        # Strip Launch_Tags
        self.df["Launch_Tag"] = self.df["Launch_Tag"].astype(str).str.upper().str.strip()
        
        # Replace double space "  " with single space " " - Sputnik 1 edge case!
        self.df["LDate"] = self.df["LDate"].str.replace(r"\s{2,}", " ", regex=True).str.strip()
        self.df["SDate"] = self.df["SDate"].str.replace(r"\s{2,}", " ", regex=True).str.strip()
        self.df["DDate"] = self.df["DDate"].str.replace(r"\s{2,}", " ", regex=True).str.strip()
        self.df["ODate"] = self.df["ODate"].str.replace(r"\s{2,}", " ", regex=True).str.strip()
    
        # Remove problematic characters from date columns (?, -) and handle NaN
        self.df["LDate"] = self.df["LDate"].fillna("").str.replace(r"[?-]", "", regex=True).str.strip()
        self.df["SDate"] = self.df["SDate"].fillna("").str.replace(r"[?-]", "", regex=True).str.strip()
        self.df["DDate"] = self.df["DDate"].fillna("").str.replace(r"[?-]", "", regex=True).str.strip()
        self.df["ODate"] = self.df["ODate"].fillna("").str.replace(r"[?-]", "", regex=True).str.strip()
        
        # Only include characters before the third space in all date columns (Remove hour/min/sec as unneeded and messes with data frame time formatting)
        self.df["LDate"] = self.df["LDate"].str.split(" ", n=3).str[:3].str.join(" ").str.strip()
        self.df["SDate"] = self.df["SDate"].str.split(" ", n=3).str[:3].str.join(" ").str.strip()
        self.df["DDate"] = self.df["DDate"].str.split(" ", n=3).str[:3].str.join(" ").str.strip()
        self.df["ODate"] = self.df["ODate"].str.split(" ", n=3).str[:3].str.join(" ").str.strip()
        
        # Add " 1" to the end of all dates that only contain year and month (assuming this is all 8 character dates) eg. "2023 Feb" -> "2023 Feb 1"
        self.df["LDate"] = self.df["LDate"].where(self.df["LDate"].str.len() != 8, self.df["LDate"] + " 1")
        self.df["SDate"] = self.df["SDate"].where(self.df["SDate"].str.len() != 8, self.df["SDate"] + " 1")
        self.df["DDate"] = self.df["DDate"].where(self.df["DDate"].str.len() != 8, self.df["DDate"] + " 1")
        self.df["ODate"] = self.df["ODate"].where(self.df["ODate"].str.len() != 8, self.df["ODate"] + " 1")
        
        # Convert Mcdowell's Vague date format to pandas datetime format
        self.df["LDate"] = pd.to_datetime(self.df["LDate"], format="%Y %b %d", errors="coerce")
        self.df["SDate"] = pd.to_datetime(self.df["SDate"], format="%Y %b %d", errors="coerce")
        self.df["DDate"] = pd.to_datetime(self.df["DDate"], format="%Y %b %d", errors="coerce")
        self.df["ODate"] = pd.to_datetime(self.df["ODate"], format="%Y %b %d", errors="coerce") # This is the date on which the orbit data was taken

        # Rename date columns
        self.df.rename(columns={"LDate": "Launch_Date", "SDate": "Separation_Date", "DDate": "Decay_Date", "ODate": "Orbit_Canonical_Date"}, inplace=True)

        # Convert mass to float (in kg) and handle NaN
        self.df["Mass"] = pd.to_numeric(self.df["Mass"], errors="coerce").fillna(0)
        self.df["DryMass"] = pd.to_numeric(self.df["DryMass"], errors="coerce").fillna(0)
        self.df["TotMass"] = pd.to_numeric(self.df["TotMass"], errors="coerce").fillna(0)
        
        # Create Simplified Orbit Column
        # Orbits: https://planet4589.org/space/gcat/web/intro/orbits.html
        self.df["Simplified_Orbit"] = self.df["OpOrbit"].str.split(" ", n=1).str[0].str.strip()
        self.df["Simplified_Orbit"] = self.df["Simplified_Orbit"].replace(
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
    
    def process_launch_dependent_columns(self, launch_df):
        """
        Create columns in satcat_df derived from launch data:
        - LV_Type: The tag of the launch that the satellite was launched on
        - Agency: The launch provider
        - Launch Site
        - Launch Pad
        Args:
            launch_df: DataFrame containing the launch class. Note this isn't the mcdowell_launch class, but the dataframe itself.
        """
        
        # For every satellite, get the corresponding launch vehicle from the launch_df by using the Launch_Tag column to merge the two dataframes
        launch_df = launch_df.copy()
        
        # Merge satcat_df with launch_df to get LV_Type, using left join to keep all satellites
        self.df = self.df.merge(
            launch_df[["Launch_Tag", "LV_Type"]],
            on="Launch_Tag",
            how="left"
        )
        
        # Merge satcat_df with launch_df to get Agency, using left join to keep all satellites
        self.df = self.df.merge(
            launch_df[["Launch_Tag", "Agency"]],
            on="Launch_Tag",
            how="left"
        )
        
        # Merge satcat_df with launch_df to get Launch_Site, using left join to keep all satellites
        self.df = self.df.merge(
            launch_df[["Launch_Tag", "Launch_Site"]],
            on="Launch_Tag",
            how="left"
        )
        
        # Merge satcat_df with launch_df to get Launch_Pad, using left join to keep all satellites
        self.df = self.df.merge(
            launch_df[["Launch_Tag", "Launch_Pad"]],
            on="Launch_Tag",
            how="left"
        )
        
        # Fill NaN with empty string for unmatched launches
        self.df["LV_Type"] = self.df["LV_Type"].fillna("")
        self.df["Agency"] = self.df["Agency"].fillna("")
        self.df["Launch_Site"] = self.df["Launch_Site"].fillna("")
        self.df["Launch_Pad"] = self.df["Launch_Pad"].fillna("")
        
    
if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', 100)  
    
    launch = mcdowell_launch.McDowellLaunch()
    satcat = McDowellSatcat()
    #dataset.filter_by_launch_date(start_date="2000-01-01", end_date="2000-02-01")
    #dataset.filter_by_sat_type_coarse(["P"])

    print(satcat.df.head(20))  # Display the first few rows of the DataFrame for verification
    
    satcat.process_launch_dependent_columns(launch.df)
    
    print(satcat.df.head(20))  # Display the first few rows of the DataFrame for verification
