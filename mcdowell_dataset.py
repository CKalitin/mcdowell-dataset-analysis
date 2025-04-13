import pandas as pd
import mcdowell_launch
import mcdowell_satcat

class McDowellDataset:
    """
    This contains all functions required for using McDowell's dataset. This includes aggregates all datasets.
    """

    def __init__(self):
        self.launch = mcdowell_launch.McDowellLaunch()
        self.satcat = mcdowell_satcat.McDowellSatcat()
        
        index = ["Launch_Tag", "Launch_Date", "Launch_Code", "Launch_Success_Fraction", "LV_Type"] # fill later
        
        
    def preprocess_sat_df(self):
        """
        Load the raw satcat dataset into a pandas DataFrame and preprocess some of the columns to be more pandas friendly.
        """
        
        self.sat_df = pd.read_csv("datasets/satellites.csv", encoding="utf-8")
        
        # Convert Mcdowell's Vague date format to pandas datetime format
        self.sat_df["pandas_date"] = pd.to_datetime(self.sat_df["Launch_Date"], errors="coerce")

