# Pythonized SPEAR model diagnostic tool for Ferret-based scripts

## Overview
This repository contains Python-based diagnostic tools for SPEAR variables. 
The original code is in Ferret, written by Andrew Wittenberg. This is an example of pythonization of an example suite of analysis,
applying best practices from a user, high-resolution data and institutional workflow perspective.

---

## Structure

- `diagnostics` - Diagnostics source code and related materials
- `README.md` — documentation for diagnostics
- `requirements.txt` — environment dependencies for running diagnostics

---

## Diagnostics

Pythonized diagnostic suites for SPEAR data analysis and evaluation.


## atw_atmos_ts_monthly_sfc_ocean

Sea Surface Temperature ( `t_surf`) bias diagnostic tool comparing SPEAR-Hi outputs against observational OISST datasets.

These Python scripts are adapted from original Ferret-based diagnostics developed by Andrew Wittenberg, with enhancements for reproducibility and integration into modern workflows.

The name of the analysis script is self-descriptive: 

atw - lead_author initials
atmos - post-processing component for data
ts - time-series
monthly - frequency of data 
sfc_ocean = surface ocean field

Key Features

* **Bilinear/Conservative Regridding:** Uses `xESMF` bilinear/conservative interpolation to map the SPEAR ocean pixels onto the 1°x1° OISST grid.
* **Diagnostic Stats:** Generates basic statistics for model comparison with observation.
* 
---

## Notes

See development timeline.

## Dependencies
This script requires specific Python modules. You can install the requirements via `conda` or `pip`.

```bash
# Recommended Conda environment setup
conda env create -n spear-analysis -f environment.yaml
conda activate spear-analysis
```

## How to run interactively
Run the ferret_test_final.ipynb notebook after starting JupyterLab. If you want to apply the "conservative" regridding, change the argument inside the xe.Regridder function from "bilinear" to "conservative".

```bash
# Start JupyterLab
conda activate spear-analysis
jupyter lab
```

Running with snakemake
``
conda activate /nbhome/Aparna.Radhakrishnan/conda/envs/snakemake-env/
python -m snakemake -j 1 -p --forceall
``
One can also run with papermill 

conda run papermill -k spear-analysis diagnostics/atw_atmos_ts_monthly_sfc_ocean_updated.ipynb diagnostics/atw_atmos_ts_monthly_sfc_ocean_executed.ipynb

## Development Timeline

**Phases**

1. Foundation  
2. Efficiency *(parallel)*  
3. Reproducible & Flexible Workflows *(parallel)*  
4. Validation *(continuous)*  
5. Portability
   
Efficiency and workflow development proceed in parallel; validation spans all phases.
User engagement throughout.

## How to install and use through pip
```bash
# 1. Install the tricky dependencies using conda
conda env create -f environment.yml
conda activate your_env_name

# 2. Install the atw_diags package into that environment
pip install .

# 3. Install the kernel (Is there a better way?)
python -m ipykernel install --user --name spear-analysis --display-name "spear-analysis"

# 4. Run command-line tool
run-atw-diags output.ipynb
```
