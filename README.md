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
7. Check Starship Flight 1 Date and realize that all dates are wrong