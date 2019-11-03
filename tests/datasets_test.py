from probabilistic_backpropagation_dataset.datasets import load, listed

for key in listed:
    dat = load(key)
    print('{}: N={} d={}'.format(key, dat['df'].shape[0], len(dat['exog_columns'])))