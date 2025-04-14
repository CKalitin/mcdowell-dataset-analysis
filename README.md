# Jonathan McDowell Dataset Analysis
Google sheets is terrible software once you reach 10000 lines, excel too

Going to manually write the csv analysis library and use plotly for display. Must be end-to-end, start with a natural language prompt, get a chart as a result in a couple of iterations. 

TODO:
1. Create separate filter class so it's synced between satcat and launch
    a. Create a function for each filter and a case for being given either launch or satcat, throw an error if you are trying to a filter on the wrong dataset
2. Add psatcat dataset in for satellite program
3. Add sites dataset and simplify site names
4. Add orgs dataset and simplify country names