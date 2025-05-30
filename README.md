## TODO

TODO:
1. Plotly
2. Use auxcat / parents of satellites to get their initial orbits
3. Documentation of everything and what to use for the AIs

Refactoring:
1. Split into categories easily (need a function as parameter, eg do you want to sort by orbit or mass or what?)
2. 

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

## Updating Datasets

The datasets currently have data up until May 16 2025.

To update the datasets, you can use the `update_datasets.py` script. This script fetches the latest data from Jonathan McDowell's website and updates the local TSV files.

If the script fails, manually download the datasets as instructed in How-To-Update-Datasets.md.

Use this sparingly, we don't want to DDOS Jonathan McDowell!
