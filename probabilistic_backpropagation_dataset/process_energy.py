import pandas as pd
from .utils import loc_data

df = pd.read_excel(loc_data("Energy efficiency/ENB2012_data.xlsx"))

exog_columns = list(df.columns[:-2])
endog_columns = list(df.columns[-2:])