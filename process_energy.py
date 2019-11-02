import pandas as pd

df = pd.read_excel("raw/Energy efficiency/ENB2012_data.xlsx")

exog_columns = list(df.columns[:-2])
endog_columns = list(df.columns[-2:])