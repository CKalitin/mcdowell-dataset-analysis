## TODO

 - It lists CAPSTONE as a commercial payload (Great example of high leverage, write this down somewhere, who else would notice this instantly?)

1. Line charts with several different filters for each line, idk how to do this. Binning? Probably yes. Certainly
2. Pie Charts
3. Add functions to get launch types (in chart utils, not everywhere? Eh do it everywhere)
4. Add all legacy charts
5. Documentation of how everything works and how to use for the AIs

## Block Diagram

![Code Block Diagram](https://github.com/CKalitin/mcdowell-dataset-analysis/blob/main/docs/block-diagram.png)  
[Drawio Google Drive Link](https://drive.google.com/file/d/1IRLoI8Vcy9faPdhrrpZJAQ3iU27p1e-x/view?usp=sharing)

## Installation

### Install from PyPI
The easiest way to install the package is via PyPI:
```bash
pip install mcdowell-dataset-analysis
```

### Local Installation (Optional)
For modifying the code locally, without having to deal with PyPI every time you make a change:
1. Clone the repository:
   ```bash
   git clone https://github.com/CKalitin/mcdowell-dataset-analysis.git
   cd mcdowell-dataset-analysis
   ```
2. Install in editable mode (remember the dot at the end!!):
   ```bash
   pip install -e .
   ```
   If using Github desktop, run only this command in the base directory of this repo in the VS Code terminal.


### Dependencies
The package requires:
- `pandas>=2.0.0`
- `matplotlib>=3.5.0`
- `plotly>=5.0.0`

These are automatically installed when you use `pip`.

## Updating Datasets

The datasets currently have data up until June 3 2025.

To update the datasets, you can use the `update_datasets.py` script. This script fetches the latest data from Jonathan McDowell's website and updates the local TSV files.

If the script fails, manually download the datasets as instructed in How-To-Update-Datasets.md.

Use this sparingly, we don't want to DDOS Jonathan McDowell!
