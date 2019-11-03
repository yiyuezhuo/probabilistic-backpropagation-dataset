import os

def get_root():
    return os.path.dirname(os.path.abspath(__file__)) + '/'

def loc_data(path):
    return get_root() + "raw/" + path