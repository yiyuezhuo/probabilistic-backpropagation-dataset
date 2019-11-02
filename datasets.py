
listed = {
    'Boston Housing': 'boston',
    'Combined Cycle Power Plant': 'combined',
    'Concrete Compression Strength': 'concrete', 
    'Energy Efficiency': 'energy', 
    'Kin8nm': 'kin8nm', 
    'Naval Propulsion': 'naval', 
    'Protein Structure': 'protein', 
    'Wine Quality Red': 'wine', 
    'Yacht Hydrodynamics': 'yacht', 
    'Year Prediction MSD': 'year'
}

module_cache = {}

def extract_from_module(mod):
    return dict(df = mod.df, exog_columns = mod.exog_columns, endog_columns=mod.endog_columns)

def load(key):
    if key not in listed:
        raise ValueError("Unknown dataset {}".format(key))
    if key not in module_cache:
        mod_name = 'process_' + listed[key]
        module_cache[key] = __import__(mod_name)

    return extract_from_module(module_cache[key])