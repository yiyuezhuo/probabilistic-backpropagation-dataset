import pandas as pd
from .utils import loc_data

df = pd.read_excel(loc_data("Combined Cycle Power Plant/CCPP/Folds5x2_pp.xlsx"))
exog_columns = list(df.columns[:-1])
endog_columns = list(df.columns[-1:])