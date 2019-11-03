import pandas as pd
import os

dst_path = "raw/Year Prediction MSD/YearPredictionMSD.txt"

if not os.path.exists(dst_path):
    print("Year Prediction MSD can not be found, downloading...")
    
    import requests
    res = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/00203/YearPredictionMSD.txt.zip")
    zip_path = dst_path + '.zip'
    with open(zip_path, 'wb') as f:
        f.write(res.content)
    
    print("Download complete, start extracting")
    import zipfile
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall("raw/Year Prediction MSD")
    print("Extracting completed")
    

df = pd.read_csv(dst_path, header=None)

endog_columns = ["year"]
exog_columns = ["X{}".format(i) for i in range(1,91)]
df.columns = endog_columns + exog_columns