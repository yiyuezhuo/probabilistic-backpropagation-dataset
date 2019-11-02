import pandas as pd

df = pd.read_excel("raw/Combined Cycle Power Plant/CCPP/Folds5x2_pp.xlsx")
exog_columns = list(df.columns[:-1])
endog_columns = list(df.columns[-1:])