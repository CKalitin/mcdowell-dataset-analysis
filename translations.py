# Note:
# There might be some edge cases where a satcat simplified orbit is SSO
# while launch simplified orbit is LEO.
# Eg. satcat raw orbit "LEO/P" while launch raw orbit "LEO"
launch_category_to_simplified_orbit = {
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

opOrbit_to_simplified_orbit = {
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