# pySLIME: Ionospheric Background Modeling Toolkit

MISA-pySLIME (Millstone Hill Incoherent Scatter Radar Spatial-Linear Ionospheric Modeling Engine) is a Python package for building and querying binned‑regression ionospheric ion & electron temperature and density (Te, Ti, Ne) from Millstone Hill Incoherent Scatter Radar (MISA) data.

---

## 🔧 Installation

### Prerequisites

* Python 3.8+

`
pip install MISA-pySLIME
`

## 🚀 Quickstart

### Running A Single Prediction

```python
from pySLIME import predict_ne, predict_ti, predict_te

# Example: predict electron density (Ne) at azimuth=-80°, altitude=350 km,
# DOY=99, UT=12.5 in 2024:
ne = predict_ne(
    doy=99,
    time=12.5,
    year=2024,
    coords=(-80, 350),
    input_coords='az_alt',  # or 'lat_lon'
    time_ref='ut'           # 'slt' or 'ut'
)
print(f"Predicted Ne: {ne:.3e} m⁻³")
```

---

## 📦 Functions Overview

> All functions are defined in `pySLIME.py`.
* **`predict_ne(...)`, `predict_ti(...)`, `predict_te(...)`**
  Primary wrappers loading pre‑trained models for electron density, ion temperature, and electron temperature.
* **`query_model(az, alt, doy, slt, indices, bin_models, feature_order)`**
  Low‑level engine that selects the correct bin, scales & transforms features, and runs the Ridge regression.
* **`get_lat_lon(az, alt)`**
  Convert radar beam geometry (azimuth, altitude) to geographic (latitude, longitude).
* **`get_az_alt(lat, lon)`**
  Inverse mapping: geographic coords → beam (azimuth, altitude).


---

## 📁 Project Structure

```text
pySLIME/
├── ancillary/             # Geophysical & grid datasets (netCDF, CSV)
├── model/                 # Pre‑trained model artifacts (.npy)
├── notebooks/             # Example & tutorial Jupyter notebooks
├── pySLIME.py             # Core library functions
├── requirements.txt       # Python dependencies (pip)
├── environment.yml        # Optional: conda environment spec
├── README.md              # This file
├── LICENSE                # Open‑source license
└── .gitignore             # Ignore patterns for git
```

---