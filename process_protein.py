import pandas as pd

df = pd.read_csv("raw/Protein Structure/CASP.csv")

endog_columns = list(df.columns[:1])
exog_columns = list(df.columns[1:])