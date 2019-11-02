import pandas as pd

df = pd.read_csv("raw/Boston Housing/housing.data",
    delim_whitespace=True, header=None)
    
endog_columns = ["MEDV"]
exog_columns = ['CRIM', "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE",
    "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT"]

df.columns = exog_columns + endog_columns
