# Block Diagram

![Code Block Diagram](https://github.com/CKalitin/mcdowell-dataset-analysis/blob/main/docs/block-diagram.png)  
[Drawio Google Drive Link](https://drive.google.com/file/d/1IRLoI8Vcy9faPdhrrpZJAQ3iU27p1e-x/view?usp=sharing)

## Installation

### Install from PyPI
The easiest way to install the package is via PyPI:
```bash
pip install mcdowell-dataset-analysis
```

### Local Installation (Optional)
For developers who want to modify the source code:
1. Clone the repository:
   ```bash
   git clone https://github.com/CKalitin/mcdowell-dataset-analysis.git
   cd mcdowell-dataset-analysis
   ```
2. Install in editable mode:
   ```bash
   pip install -e .
   ```

### Dependencies
The package requires:
- `pandas>=2.0.0`
- `matplotlib>=3.5.0`
- `plotly>=5.0.0`

These are automatically installed when you use `pip`.

# Jonathan McDowell Dataset Analysis
Google sheets is terrible software once you reach 10000 lines, excel is ugly.

Going to manually write the csv analysis library and use plotly for display. Must be end-to-end, start with a natural language prompt, get a chart as a result in a couple of iterations. 

TODO:
1. Plotly
2. Use auxcat / parents of satellites to get their initial orbits
3. Documentation of everything and what to use for the AIs