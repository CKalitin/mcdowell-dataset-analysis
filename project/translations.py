import csv

class Translation:
    """
    This class contains all functions required for translating columns into more pandas or user friendly formats.
    
    This is a class because some translation dictionaries like lv_translation require a file to be read in.
    """
    
    def __init__(self):
        self.generate_OpOrbit_to_simplified_orbit()
        self.generate_launch_category_to_simplified_orbit()
        self.generate_lv_translation()

    def generate_OpOrbit_to_simplified_orbit(self):
        self.opOrbit_to_simplified_orbit = {
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


    def generate_launch_category_to_simplified_orbit(self):
        # Note:
        # There might be some edge cases where a satcat simplified orbit is SSO
        # while launch simplified orbit is LEO.
        # Eg. satcat raw orbit "LEO/P" while launch raw orbit "LEO"
        self.launch_category_to_simplified_orbit = {
            "DSO": "BEO",    # Deep space orbit
            "EEO": "BEO",    # Earth escape orbit
            "GEO": "GEO",    # Direct geosync insertion
            "GTO": "GTO",    # Geosync transfer orbit
            "HEO": "HEO",    # Highly elliptical orbit
            "ISS": "LEO",    # International Space Station
            "LEO": "LEO",    # Low Earth Orbit
            "LSS": "LEO",    # LEO space station other than ISS
            "MEO": "MEO",    # Medium Earth Orbit
            "MOL": "HEO",    # Molniya orbit
            "MTO": "MEO",    # MEO transfer orbit
            "SSO": "SSO",    # Sun-sync orbit
            "STO": "GTO",    # Supersync transfer orbit
            "XO": "BEO"      # Extraterrestrial launch
        }

    def generate_lv_translation(self, filePath = "./datasets/lv.tsv"):
        """
        Generate a dictionary that translate LV_Type to LV_Family.
        This requires lv.tsv file
        Launch Vehicle Families Text File: https://planet4589.org/space/gcat/web/lvs/family/index.html
        """
        with open(filePath, 'r') as file:
            reader = csv.reader(file, delimiter='\t')
            reader.__next__() # Skip the index row
            reader.__next__() # Skip the header row
            self.lv_type_to_lv_family = {row[0].strip(): row[1].strip() for row in reader}