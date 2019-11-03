import pandas as pd
from .utils import loc_data

df = pd.read_csv(loc_data("Naval Propulsion/UCI CBM Dataset/data.txt"),
    delim_whitespace=True, header=None)

exog_columns = ["lp", "v", "GTT", "GTn", "GGn", "Ts", "Tp", "T48",
    "T1", "T2", "P48", "P1", "P2", "Pexh", "TIC", "mf"]
endog_columns = ["GTCD", "GTTD"]

df.columns = exog_columns + endog_columns