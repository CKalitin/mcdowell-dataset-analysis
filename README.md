## TODO

First, remember the previous commit:
"
Attempt at general launch type

todo is to look for edge cases and fix them
"

1. Fix text overflow on Electron general launch payload type mass distribution chart
   - Also, it lists CAPSTONE as a commercial payload (Great example of high leverage, write this down somewhere, who else would notice this instantly?)
   - Also Soyuz title overflow
1. Automatically detect first and last launches in timeframe for no require manual parameter
   - Also fix Titan start year on charts
1. Net payload mass launches vs time
2. Add functions to get launch types (in chart utils, not everywhere? Eh do it everywhere)
2. Better military general launch payload type detection (eg. NROL, etc.) will need to get a full list of military payload designations
   - Really, a better category (eg. military observation is both, which one do you put? Make a separate category! User (comm, gov, mil) and rename current military to weapon or something)
3. Pie charts
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
