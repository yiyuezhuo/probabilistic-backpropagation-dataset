import pandas as pd
from .utils import loc_data


df = pd.read_excel(loc_data("Concrete Compression Strength/Concrete_Data.xls"))

exog_columns = ["Cement", "Blast Furnace Slag", "Fly Ash", "Water",
    "Superplasticizer", "Coarse Aggregate", "Fine Aggregate", "Age -- quantitative -- Day"]
endog_columns = ["Concrete compressive strength"]

df.columns = exog_columns + endog_columns