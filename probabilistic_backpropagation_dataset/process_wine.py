import pandas as pd
from .utils import loc_data

df = pd.read_csv(loc_data("Wine Quality Red/winequality-red.csv"), sep=';')

exog_columns = list(df.columns[:-1])
endog_columns = list(df.columns[-1:])