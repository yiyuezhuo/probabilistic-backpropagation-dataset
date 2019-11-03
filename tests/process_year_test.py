'''
Mock requests to test if process_year downloading and unzip data file properly.

Download YearPredictionMSD.txt.zip to folder in which the script live to run this test.
'''

import os

assert os.path.exists("YearPredictionMSD.txt.zip")

class ResponseMocked:
    def __init__(self, content):
        self.content = content

class requests_mocked:
    @staticmethod
    def get(url):
        with open("YearPredictionMSD.txt.zip", "rb") as f:
            dat = f.read()
        return ResponseMocked(dat)

import sys
sys.modules['requests'] = requests_mocked
# Therefore, other import called after this statement will set `requests_mocked` as value of `requests` instead of true `requests` module.

import probabilistic_backpropagation_dataset.process_year

print(probabilistic_backpropagation_dataset.process_year.df)