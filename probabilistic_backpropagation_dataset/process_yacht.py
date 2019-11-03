import pandas as pd

df = pd.read_csv("raw/Yacht Hydrodynamics/yacht_hydrodynamics.data", delim_whitespace=True, header=None)

exog_columns = ['Longitudinal', "Prismatic", "Length-displacement",
    "Beam-draught", "Length-beam", "Froude"]
endog_columns = ["Residuary resistance"]

df.columns = exog_columns + endog_columns