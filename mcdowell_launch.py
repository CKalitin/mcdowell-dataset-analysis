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
        
        # Only include characters before the third space in the launch_date column (Remove hour/min/sec as unneeded and messes with data frame time formatting)
        self.launch_df["Launch_Date"] = self.launch_df["Launch_Date"].str.split(" ", n=3).str[:3].str.join(" ")
        
        # Convert Mcdowell's Vague date format to pandas datetime format
        self.launch_df["Date_Pandas"] = pd.to_datetime(self.launch_df["Launch_Date"], errors="coerce")
        
        # Remove column "#Launch_Tag" to "Launch_Tag"
        self.launch_df.rename(columns={"#Launch_Tag": "Launch_Tag"}, inplace=True)

    def process_satcat_dependent_columns(self, satcat_df):
        """
        Create columns: Payload mass, satellite tags (pieces), canonical orbit
        Args:
            satcat_df: DataFrame containing the satcat class. Note this isn't the mcdowell_satcat class
        """
        
        satcat_df = satcat_df.copy()  # Avoid modifying the original DataFrame
        
        # Group satcat_df by Launch_Tag
        grouped = satcat_df.groupby("Launch_Tag")
        
        # Payload Mass: Sum Mass for Type="P"
        payload_mass = grouped.apply(
            lambda x: x[x["Type"].str.startswith("P")]["Mass"].sum(),
            include_groups=False
        ).reindex(self.launch_df["Launch_Tag"], fill_value=0).reset_index(name="Payload_Mass")
        
        # Satellite Tags: Collect Piece values
        satellite_tags = grouped["Piece"].agg(lambda x: ",".join(x)).reindex(
            self.launch_df["Launch_Tag"], fill_value=""
        ).reset_index(name="Satellite_Tags")
        
        # Canonical Orbit: First non-null OpOrbit
        canonical_orbit = grouped["OpOrbit"].agg(
            lambda x: next((o for o in x if pd.notnull(o) and o != "-"), "")
        ).reindex(self.launch_df["Launch_Tag"], fill_value="").reset_index(name="Canonical_Orbit")

        # Merge results into launch_df
        self.launch_df = self.launch_df.merge(
            payload_mass.rename(columns={"Launch_Tag": "Launch_Tag"}),
            on="Launch_Tag",
            how="left"
        ).merge(
            satellite_tags.rename(columns={"Launch_Tag": "Launch_Tag"}),
            on="Launch_Tag",
            how="left"
        ).merge(
            canonical_orbit.rename(columns={"Launch_Tag": "Launch_Tag"}),
            on="Launch_Tag",
            how="left"
        )
    
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
            self.launch_df = self.launch_df[self.launch_df["Date_Pandas"] >= start_date]
        
        if end_date is not None:
            self.launch_df = self.launch_df[self.launch_df["Date_Pandas"] <= end_date]


if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
        
    launch = McDowellLaunch()
    satcat = mcdowell_satcat.McDowellSatcat()
    launch.process_satcat_dependent_columns(satcat.satcat_df)
    launch.filter_by_date(start_date="2000-01-01", end_date="2000-02-01")

    print(launch.launch_df.head(20))  # Display the first few rows of the DataFrame for verification