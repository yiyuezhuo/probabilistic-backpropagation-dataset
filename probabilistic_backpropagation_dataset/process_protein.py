import pandas as pd
from .utils import loc_data

df = pd.read_csv(loc_data("Protein Structure/CASP.csv"))

endog_columns = list(df.columns[:1])
exog_columns = list(df.columns[1:])