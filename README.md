# Block Diagram

![Code Block Diagram](https://github.com/CKalitin/mcdowell-dataset-analysis/blob/main/docs/block-diagram.png)

![Link](https://app.diagrams.net/#G1IRLoI8Vcy9faPdhrrpZJAQ3iU27p1e-x#%7B%22pageId%22%3A%22hL2WBVDFGfZaWTC3ArIe%22%7D)

# Jonathan McDowell Dataset Analysis
Google sheets is terrible software once you reach 10000 lines, excel too

Going to manually write the csv analysis library and use plotly for display. Must be end-to-end, start with a natural language prompt, get a chart as a result in a couple of iterations. 

TODO:
1. Add psatcat and sites and orgs datasets in separate files
2. Add remaining filters since these new datasets
3. Write documentation for everything (for the AIs)
4. Add simplified site names and beautified country names
5. For launch orbits use category column, as satcat has edge cases (roadster)
    a. See: https://planet4589.org/space/gcat/web/intro/profile.html
6. Put all column translations in their own config file (ie. OpOrbit raw to Simplified Orbit, or category to orbit)
8. Dictionary to translate LV_Type into easier names (eg. "Starship" instead of "Starship V1.0")

# Dictionary to translate raw orbit categories to simplified ones
orbit_translation = {
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

Note: There'll be some edge cases with SSO where in satcat a simplified orbit is given as SSO but the raw orbit is LEO/S or something. In the launch dataset this might be recorded as LEO instead of SSO. Or polar.