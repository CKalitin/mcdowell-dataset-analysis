See the website for this project here:
https://ckalitin.github.io/space/2025/06/08/space-industry-charts.html

## TODO

- It lists CAPSTONE as a commercial payload (Great example of high leverage, write this down somewhere, who else would notice this instantly?)

2. Line charts (eg. launches per country or pad)
3. Pie charts
4. Launch Types
   - Small sat payload type
   - Small sat operator type
   - General operator type?
   - F9 payload type
5. F9 Booster Launches Line Chart

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

The datasets currently have data up until June 8 2025.

To update the datasets, you can use the `update_datasets.py` script. This script fetches the latest data from Jonathan McDowell's website and updates the local TSV files.

If the script fails, manually download the datasets as instructed in How-To-Update-Datasets.md.

Use this sparingly, we don't want to DDOS Jonathan McDowell!
