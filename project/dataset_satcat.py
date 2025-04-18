import pandas as pd
import translations

import dataframe_filters
import dataset_launch

class Satcat:
    """
    This contains all functions required for using McDowell's satellite catalog dataset.
    """

    def __init__(self, translation=None, file_path="./datasets/satcat.tsv", psatcat_path="./datasets/psatcat.tsv"):
        """
        Load the raw satcat dataset into a pandas DataFrame.
        
        satcat.tsv column descriptions: https://planet4589.org/space/gcat/web/cat/cols.html
        """
        
        self.file_path = file_path
        self.translation = translations.Translation()
        
        self.df = pd.read_csv(self.file_path, sep="\t", encoding="utf-8", low_memory=False) # load satcat tsv into dataframe
        self.psatcat_df = pd.read_csv(psatcat_path, sep="\t", encoding="utf-8", low_memory=False) # load psatcat tsv into dataframe
        
        self.preprocess_satcat_df()
        
        self.process_psatcat_dependent_columns(self.psatcat_df)

    def reload(self):
        self.__init__()

    def preprocess_satcat_df(self):
        """
        Create new columns from existing columns in satcat dataframe to make it more pandas friendly.
        Lots of string manipulation to get the dates into a format that pandas can understand.
        """

        # Rename column "#Launch_Tag" to "Launch_Tag"
        self.df.rename(columns={"#JCAT": "JCAT"}, inplace=True)
        
        # Strip Launch_Tags & Piece & JCAT
        self.df["Launch_Tag"] = self.df["Launch_Tag"].astype(str).str.upper().str.strip()
        self.df["Piece"] = self.df["Piece"].astype(str).str.upper().str.strip()
        self.df["JCAT"] = self.df["JCAT"].astype(str).str.upper().str.strip()
        
        date_cols = ["LDate", "SDate", "DDate", "ODate"]
        for col in date_cols:
            # Remove problematic characters from date columns (?, -) and handle NaN
            self.df[col] = self.df[col].str.strip().fillna("").str.replace(r"[?-]", "", regex=True).str.strip()
            # Replace double space "  " with single space " " - Sputnik 1 edge case!
            self.df[col] = self.df[col].str.replace(r"\s{2,}", " ", regex=True).str.strip()
            # Only include characters before the third space in all date columns (Remove hour/min/sec as unneeded and messes with data frame time formatting)
            self.df[col] = self.df[col].str.split(" ", n=3).str[:3].str.join(" ").str.strip()
            # Add " 1" to the end of all dates that only contain year and month (assuming this is all 8 character dates) eg. "2023 Feb" -> "2023 Feb 1"
            self.df[col] = self.df[col].where(self.df[col].str.len() != 8, self.df[col] + " 1")
            # Convert Mcdowell's Vague date format to pandas datetime format
            self.df[col] = pd.to_datetime(self.df[col], format="%Y %b %d", errors="coerce")
        
        # Rename date columns
        self.df.rename(columns={"LDate": "Launch_Date", "SDate": "Separation_Date", "DDate": "Decay_Date", "ODate": "Orbit_Canonical_Date"}, inplace=True)

        # Convert mass to float (in kg) and handle NaN
        self.df["Mass"] = pd.to_numeric(self.df["Mass"], errors="coerce").fillna(0)
        self.df["DryMass"] = pd.to_numeric(self.df["DryMass"], errors="coerce").fillna(0)
        self.df["TotMass"] = pd.to_numeric(self.df["TotMass"], errors="coerce").fillna(0)
        
        # Create Simple Orbit Column
        # Orbits: https://planet4589.org/space/gcat/web/intro/orbits.html
        self.df["Simple_Orbit"] = self.df["OpOrbit"].str.strip()
        self.df["Simple_Orbit"] = self.df["Simple_Orbit"].replace(self.translation.opOrbit_to_simple_orbit)
    
    def process_psatcat_dependent_columns(self, psatcat):
        """
        Create columns in satcat dataframe derived from psatcat data:
        - Payload_Name (Name)
        - Payload_Program (Program)
        - Payload_Class (Class)
        - Payload_Category (Category)
        - Payload_Discipline (Discipline)
        - Payload_Result (Result)
        - Payload_Comment (Comment)
        Args:
            psatcat: dataframe containing psatcat tsv
        Psatcat: https://planet4589.org/space/gcat/data/cat/psatcat.html  
        Psatcat column descriptions: https://planet4589.org/space/gcat/web/cat/pscols.html
        """
        
        psatcat_df = psatcat.copy()
        
        # Rename to avoid confusion with satcat columns
        psatcat_df.rename(columns={"#JCAT": "JCAT", "Name": "Payload_Name", "Program": "Payload_Program", "Class": "Payload_Class", "Category": "Payload_Category", "Discipline": "Payload_Discipline", "Result": "Payload_Result", "Comment": "Payload_Comment"}, inplace=True)
        
        # Strip JCAT
        psatcat_df["JCAT"] = psatcat_df["JCAT"].astype(str).str.upper().str.strip()
        
        # Merge satcat_df with psatcat_df to get Name, using left join to keep all satellites
        self.df = self.df.merge(
            psatcat_df[["JCAT", "Payload_Name"]],
            on="JCAT",
            how="left"
        )
        
        self.df = self.df.merge(
            psatcat_df[["JCAT", "Payload_Program"]],
            on="JCAT",
            how="left"
        )
        
        self.df = self.df.merge(
            psatcat_df[["JCAT", "Payload_Class"]],
            on="JCAT",
            how="left"
        )
        
        self.df = self.df.merge(
            psatcat_df[["JCAT", "Payload_Category"]],
            on="JCAT",
            how="left"
        )
        
        self.df = self.df.merge(
            psatcat_df[["JCAT", "Payload_Discipline"]],
            on="JCAT",
            how="left"
        )
        
        self.df = self.df.merge(
            psatcat_df[["JCAT", "Payload_Result"]],
            on="JCAT",
            how="left"
        )
        
        self.df = self.df.merge(
            psatcat_df[["JCAT", "Payload_Comment"]],
            on="JCAT",
            how="left"
        )
        
        self.df["Simple_Payload_Category"] = self.df["Payload_Category"].str.strip()
        self.df["Simple_Payload_Category"] = self.df["Simple_Payload_Category"].replace(self.translation.payload_category_to_simple_payload_category)
        
    
    def process_launch_dependent_columns(self, launch):
        """
        Create columns in satcat_df derived from launch data:
        - LV_Type: The tag of the launch that the satellite was launched on
        - Agency: The launch provider
        - Launch Site
        - Launch Pad
        Args:
            launch_df: DataFrame containing the launch class.
        """
        
        # For every satellite, get the corresponding launch vehicle from the launch_df by using the Launch_Tag column to merge the two dataframes
        launch_df = launch.df.copy()
        
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
        
        self.df = self.df.merge(
            launch_df[["Launch_Tag", "Launch_Vehicle_Family"]],
            on="Launch_Tag",
            how="left"
        )
        
        # Fill NaN with empty string for unmatched launches
        self.df["LV_Type"] = self.df["LV_Type"].fillna("")
        self.df["Agency"] = self.df["Agency"].fillna("")
        self.df["Launch_Site"] = self.df["Launch_Site"].fillna("")
        self.df["Launch_Pad"] = self.df["Launch_Pad"].fillna("")
        self.df["Launch_Vehicle_Family"] = self.df["Launch_Vehicle_Family"].fillna("")
        
    
# For testing
if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', 100)  
    
    launch = dataset_launch.Launch()
    satcat = Satcat()
    #dataset.filter_by_launch_date(start_date="2000-01-01", end_date="2000-02-01")
    #dataset.filter_by_sat_type_coarse(["P"])

    satcat.process_launch_dependent_columns(launch)

    dataframe_filters.Filters.filter_by_launch_vehicle(satcat, launch_vehicles=["Electron"])
    #dataframe_filters.Filters.filter_by_orbit(satcat, orbits=["SSO"])
    
    print(satcat.df.tail(25))  # Display the first few rows of the DataFrame for verification
    print(len(satcat.df))
