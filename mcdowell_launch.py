import pandas as pd
import mcdowell_satcat # TEMPORARY FOR TESTING DELETE ME

class McDowellLaunch:
    """
    This contains all functions required for using McDowell's launch dataset. This includes filtering the dataset by year, etc.
    """

    def __init__(self, file_path="datasets/launch.tsv"):
        """
        Initialize launch tsv file path and load the dataset into a pandas DataFrame.
        
        Launch.tsv column descriptions: https://planet4589.org/space/gcat/web/launch/lcols.html
        """
        
        self.file_path = file_path
        self.launch_df = pd.read_csv(self.file_path, sep="\t", encoding="utf-8")
        
        self.preprocess_launch_df()
    
    def preprocess_launch_df(self):
        """
        Create new columns from existing columns in satcat dataframe to make it more pandas friendly.
        Lots of string manipulation to get the dates into a format that pandas can understand.
        """
        
        # Remove column "#Launch_Tag" to "Launch_Tag"
        self.launch_df.rename(columns={"#Launch_Tag": "Launch_Tag"}, inplace=True)
        
        # Strip Launch_Tags
        self.launch_df["Launch_Tag"] = self.launch_df["Launch_Tag"].astype(str).str.upper().str.strip()
        
        # Remove problematic characters from date columns (?, -) and handle NaN
        self.launch_df["Launch_Date"] = self.launch_df["Launch_Date"].str.strip().fillna("").str.replace(r"[?-]", "", regex=True).str.strip()
    
        # Replace double space "  " with single space " " - Sputnik 1 edge case!
        self.launch_df["Launch_Date"] = self.launch_df["Launch_Date"].str.replace(r"\s{2,}", " ", regex=True).str.strip()
    
        # Only include characters before the third space in all date columns (Remove hour/min/sec as unneeded and messes with data frame time formatting)
        self.launch_df["Launch_Date"] = self.launch_df["Launch_Date"].str.split(" ", n=3).str[:3].str.join(" ").str.strip()
    
        # Add " 1" to the end of all dates that only contain year and month (assuming this is all 8 character dates) eg. "2023 Feb" -> "2023 Feb 1"
        self.launch_df["Launch_Date"] = self.launch_df["Launch_Date"].where(self.launch_df["Launch_Date"].str.len() != 8, self.launch_df["Launch_Date"] + " 1")

        # Convert Mcdowell's Vague date format to pandas datetime format
        self.launch_df["Launch_Date"] = pd.to_datetime(self.launch_df["Launch_Date"], format="%Y %b %d", errors="coerce")

    def process_satcat_dependent_columns(self, satcat_df):
        """
        Create columns in launch_df derived from satcat data:
        - Satellite_IDs: List of satellite IDs for a given launch
        - Payload_Mass: Sum of masses for all payloads in a launch
        - Canonical_Orbit_Parameters: Dictionary of canonical orbit data from satcat
        Args:
            satcat_df: DataFrame containing the satcat class. Note this isn't the mcdowell_satcat class
        """
        
        satcat_df = satcat_df.copy()
        
        payload_masses = (
            satcat_df
            .loc[satcat_df['Type'].str.startswith('P', na=False)] # Keep only payloads from satcat
            .groupby('Launch_Tag')['Mass'] # Group by launch tag and sum the masses of the payloads
            .sum()
        )
        
        # Create new column in launch_df for payload mass
        self.launch_df['Payload_Mass'] = self.launch_df['Launch_Tag'].map(payload_masses)
        
        #pick the first payload row for every Launch_Tag
        first_payload = (
            satcat_df
              .loc[satcat_df['Type'].str.startswith('P', na=False)]
              .drop_duplicates('Launch_Tag', keep='first')
              .set_index('Launch_Tag')
        )
        
        print(first_payload["Apogee"].head(20))  # Display the first few rows of the DataFrame for verification
        
        # Create new columns in launch_df for canonical orbit data
        for col in ['ODate', 'Perigee', 'Apogee', 'Inc', 'OpOrbit']:
            self.launch_df[col] = self.launch_df['Launch_Tag'].map(first_payload[col])
        self.launch_df.rename(columns={"OpOrbit": "Orbit"}, inplace=True)
        
        print(" - - - -")
        print(self.launch_df["Apogee"].head(20))  # Display the first few rows of the DataFrame for verification
        
        
    def filter_by_launch_category(self, launch_categories):
        """
        Remove all launches that are not in the given launch categories.
        Args:
            launch_categories: List of launch categories to filter by. eg. ["O", "R", "M"]
        """
        
        # vectorized operation to filter the DataFrame
        # Faster than a for loop for some reason, kind vibe coding here tbh
        self.launch_df = self.launch_df[
            self.launch_df["Launch_Code"].str[0].isin(launch_categories)
        ]
        
    def filter_by_launch_success_fraction(self, launch_success_fractions):
        """
        Remove all launches that are not in the given launch success fractions.
        Args:
            launch_success_fractions: List of launch success fractions to filter by. eg. ["S", "f"]
        """
        
        self.launch_df = self.launch_df[
            self.launch_df["Launch_Code"].str[1].isin(launch_success_fractions)
        ]

    def filter_by_date(self, start_date=None, end_date=None):
        """
        Remove all launches that are not in the given date range (inclusive range).
        Args:
            start_date: Start date to filter by. eg. "2000-01-01"
            end_date: End date to filter by. eg. "2020-01-01"
        """
        
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
        
        if start_date is not None:
            self.launch_df = self.launch_df[self.launch_df["Launch_Date"] >= start_date]
        
        if end_date is not None:
            self.launch_df = self.launch_df[self.launch_df["Launch_Date"] <= end_date]


if __name__ == "__main__":
    pd.set_option('display.max_columns', 200)
        
    launch = McDowellLaunch()
    satcat = mcdowell_satcat.McDowellSatcat()
    
    launch.filter_by_date(start_date="1957-10-01", end_date="1958-10-25")
    launch.filter_by_launch_category(["O"])
    launch.filter_by_launch_success_fraction(["S"])
    
    #print(launch.launch_df.head(50))  # Display the first few rows of the DataFrame for verification
    
    launch.process_satcat_dependent_columns(satcat.satcat_df)

    print(launch.launch_df.head(20))  # Display the first few rows of the DataFrame for verification