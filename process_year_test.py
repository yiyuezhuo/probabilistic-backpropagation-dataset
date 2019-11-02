'''
Mock requests to test if process_year downloading and unzip data file properly.
'''
class ResponseMocked:
    def __init__(self, content):
        self.content = content

class requests_mocked:
    @staticmethod
    def get(url):
        with open("raw_test/YearPredictionMSD.txt.zip", "rb") as f:
            dat = f.read()
        return ResponseMocked(dat)

import sys
sys.modules['requests'] = requests_mocked
# Therefore, other import called after this statement will set `requests_mocked` as value of `requests` instead of true `requests` module.

import process_year