import pandas as pd

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


pd.set_option('display.max_columns', None)
        
dataset = McDowellLaunch()
dataset.filter_by_date(start_date="2000-01-01", end_date="2000-02-01")

print(dataset.launch_df.head(20))  # Display the first few rows of the DataFrame for verification
