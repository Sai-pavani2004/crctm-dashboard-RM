# CRCTM Dashboard

The Cybersecurity Risk Communication Threshold Model dashboard is a Streamlit
research interface for comparing the Equifax, Target, and Capital One case
studies.

## Run locally

```bash
python -m pip install -r requirements.txt
streamlit run crctm_dashboard.py
```

## Deploy with Streamlit Community Cloud

Create a new app from this GitHub repository and select:

- **Main file path:** `crctm_dashboard.py`
- **Branch:** `main`

Community Cloud installs the dependencies from `requirements.txt`. The
dashboard's research data is defined in the Python file; no separate data files,
environment variables, or credentials are required.

The displayed scores are researcher-entered example values, as described in the
dashboard methodology.
