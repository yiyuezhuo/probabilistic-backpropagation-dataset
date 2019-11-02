import pandas as pd

df = pd.read_csv("raw/Wine Quality Red/winequality-red.csv", sep=';')

exog_columns = list(df.columns[:-1])
endog_columns = list(df.columns[-1:])