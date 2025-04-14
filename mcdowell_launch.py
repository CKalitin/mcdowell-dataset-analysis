import pandas as pd
import mcdowell_satcat

class Launch:
    """
    This contains all functions required for using McDowell's launch dataset. This includes filtering the dataset by year, etc.
    """

    def __init__(self, file_path="datasets/launch.tsv"):
        """
        Initialize launch tsv file path and load the dataset into a pandas DataFrame.
        
        Launch.tsv column descriptions: https://planet4589.org/space/gcat/web/launch/lcols.html
        """
        
        self.file_path = file_path
        self.df = pd.read_csv(self.file_path, sep="\t", encoding="utf-8") # load csv into dataframe
        
        self.preprocess_launch_df()
    
    def preprocess_launch_df(self):
        """
        Create new columns from existing columns in satcat dataframe to make it more pandas friendly.
        Lots of string manipulation to get the dates into a format that pandas can understand.
        """
        
        # Rename column "#Launch_Tag" to "Launch_Tag"
        self.df.rename(columns={"#Launch_Tag": "Launch_Tag"}, inplace=True)
        
        # Strip Launch_Tags
        self.df["Launch_Tag"] = self.df["Launch_Tag"].astype(str).str.upper().str.strip()
        
        # Remove problematic characters from date columns (?, -) and handle NaN
        self.df["Launch_Date"] = self.df["Launch_Date"].str.strip().fillna("").str.replace(r"[?-]", "", regex=True).str.strip()
    
        # Replace double space "  " with single space " " - Sputnik 1 edge case!
        self.df["Launch_Date"] = self.df["Launch_Date"].str.replace(r"\s{2,}", " ", regex=True).str.strip()
    
        # Only include characters before the third space in all date columns (Remove hour/min/sec as unneeded and messes with data frame time formatting)
        self.df["Launch_Date"] = self.df["Launch_Date"].str.split(" ", n=3).str[:3].str.join(" ").str.strip()
    
        # Add " 1" to the end of all dates that only contain year and month (assuming this is all 8 character dates) eg. "2023 Feb" -> "2023 Feb 1"
        self.df["Launch_Date"] = self.df["Launch_Date"].where(self.df["Launch_Date"].str.len() != 8, self.df["Launch_Date"] + " 1")

        # Convert Mcdowell's Vague date format to pandas datetime format
        self.df["Launch_Date"] = pd.to_datetime(self.df["Launch_Date"], format="%Y %b %d", errors="coerce")

    def process_satcat_dependent_columns(self, satcat_df):
        """
        Create columns in launch_df derived from satcat data:
        - Payload_Mass: Sum of masses for all payloads in a launch
        - Canonical Orbit Parameters: [ODate, Ap, Pe, Inc, OpOrbit, Simplified Orbit]
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
        self.df['Payload_Mass'] = self.df['Launch_Tag'].map(payload_masses)
        
        #pick the first payload row for every Launch_Tag
        first_payload = (
            satcat_df
              .loc[satcat_df['Type'].str.startswith('P', na=False)]
              .drop_duplicates('Launch_Tag', keep='first')
              .set_index('Launch_Tag')
        )
        
        # Create new columns in launch_df for canonical orbit data
        for col in ['Orbit_Canonical_Date', 'Perigee', 'Apogee', 'Inc', 'OpOrbit', 'Simplified_Orbit']:
            self.df[col] = self.df['Launch_Tag'].map(first_payload[col])
        self.df.rename(columns={"OpOrbit": "Orbit"}, inplace=True)


if __name__ == "__main__":
    pd.set_option('display.max_columns', 200)
        
    launch = Launch()
    satcat = mcdowell_satcat.Satcat()
    
    launch.filter_by_launch_date(start_date="1957-10-01", end_date="1958-10-25")
    launch.filter_by_launch_category(["O"])
    launch.filter_by_launch_success_fraction(["S"])
    
    #print(launch.launch_df.head(50))  # Display the first few rows of the DataFrame for verification
    
    launch.process_satcat_dependent_columns(satcat.satcat_df)

    print(launch.launch_df.head(20))  # Display the first few rows of the DataFrame for verification