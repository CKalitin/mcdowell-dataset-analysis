"""
Types:
Orbit
General Launch Type (Starlink, Commercial, Chinese Commecerial, Military, Government, Eastern)
Western Launch Type (High-Energy, Capsule, Small Sat Rideshare, Small Sat, Commercial LEO / SSO / MEO, Commercial GEO / GTO, Constellation GEO/MEO, LEO Constellation, Starlink)
Small Sat Launch Type (Ridesharable, Kick Stagable, Unique Plane SLV, Government SLV, Gov. / Military Payload)
Small Sat Payload Type (Earth imaging, Earth Observation, Synthetic Aperture Radar, Tech Demo, Military, Other)
Payload Type (Other, Tech Demo, Military, Sicence, Communications, Observation)
"""

def add_general_launch_payload_type(launch_dataframe):
    """
    Launch group descriptions:
    https://planet4589.org/space/gcat/web/intro/service.html
    
    Note that this is launch payload type. So a government payload on a commercial rocket is government.
    
    Starlink: mission column contains 'Starlink'
    Commercial: group starts with 'C' and state is not 'CN' or 'RU'
    Chinese Commercial: group starts with 'C' and state is 'CN' or 'RU'
    Military: First_Simple_Payload_Category is 'Military'
    Eastern Military: Same as military but state is 'CN' or 'RU'
    Government: group starts with 'G' or contains 'CX' or 'OG'
    Eastern Government: group starts with 'G' or contains 'CX' or 'OG' and state is 'CN' or 'RU'
    """
    
    # Make 'Unknown' the default value for General_Launch_Payload_Type
    launch_dataframe['General_Launch_Payload_Type'] = 'Unknown'
    
    # Commercial
    commercial_mask = (launch_dataframe['Group'].str.startswith('C'))
    launch_dataframe.loc[commercial_mask, 'General_Launch_Payload_Type'] = 'Commercial'
    
    # Chinese Commercial
    chinese_commercial_mask = (launch_dataframe['Group'].str.startswith('C')) & (~launch_dataframe['Group'].str.contains('CX')) & (launch_dataframe['State'].isin(['CN']))
    launch_dataframe.loc[chinese_commercial_mask, 'General_Launch_Payload_Type'] = 'Chinese Commercial'
    
    # Government
    # If starts with 'G' or contains 'CX' or 'OG'
    government_mask = (
        launch_dataframe['Group'].str.startswith('G') |
        launch_dataframe['Group'].str.contains('CX', case=False, na=False) |
        launch_dataframe['Group'].str.contains('OG', case=False, na=False)
    )
    launch_dataframe.loc[government_mask, 'General_Launch_Payload_Type'] = 'Government'
    
    # Eastern Government
    # If is government type and state is China or Russia
    eastern_government_mask = (
        government_mask &
        launch_dataframe['State'].isin(['CN', 'RU', 'SU'])
    )
    launch_dataframe.loc[eastern_government_mask, 'General_Launch_Payload_Type'] = 'Eastern Government'
    
    # Military
    # See https://planet4589.org/space/gcat/web/cat/pcols.html
    military_mask = launch_dataframe['First_Payload_Class'] == 'D'
    launch_dataframe.loc[military_mask, 'General_Launch_Payload_Type'] = 'Military'
    
    # Eastern Military
    eastern_military_mask = military_mask & launch_dataframe['State'].isin(['CN', 'RU', 'SU'])
    launch_dataframe.loc[eastern_military_mask, 'General_Launch_Payload_Type'] = 'Eastern Military'
    
    # Starlink
    launch_dataframe.loc[launch_dataframe['Mission'].str.contains('Starlink', case=False, na=False), 'General_Launch_Payload_Type'] = 'Starlink'
    
    print(launch_dataframe.tail(100))
    
    return launch_dataframe