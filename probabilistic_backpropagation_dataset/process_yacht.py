import pandas as pd
from .utils import loc_data

df = pd.read_csv(loc_data("Yacht Hydrodynamics/yacht_hydrodynamics.data"), delim_whitespace=True, header=None)

exog_columns = ['Longitudinal', "Prismatic", "Length-displacement",
    "Beam-draught", "Length-beam", "Froude"]
endog_columns = ["Residuary resistance"]

df.columns = exog_columns + endog_columns