# 10 datasets for Probabilistic backpropagation for scalable learning of bayesian neural networks

The paper `Probabilistic backpropagation for scalable learning of bayesian neural networks` list 10 datasets to evaluate performance of their proposed algorithm. While they're old school "table"(instead of image or text) non-linear regression dataset, the format of them are a a little messy. This repo include 9 datasets directly and automatically download the rest one, a 200Mb+ dataset if required. A unified interface, `pandas.DataFrame` is given.

9 of 10 datasets are from `archive.ics.uci.edu`, and rest one, `Kin8nm` is from another GitHub repo since the original link is broken.

## Usage

See `datasets_test.py`:

```python
from datasets import load, listed

for key in listed:
    dat = load(key)
    print('{}: N={} d={}'.format(key, dat['df'].shape[0], len(dat['exog_columns'])))

'''output:
Boston Housing: N=506 d=13
Combined Cycle Power Plant: N=9568 d=4
Concrete Compression Strength: N=1030 d=8
Energy Efficiency: N=768 d=8
Kin8nm: N=8192 d=8
Naval Propulsion: N=11934 d=16
Protein Structure: N=45730 d=9
Wine Quality Red: N=1599 d=11
Yacht Hydrodynamics: N=308 d=6
Year Prediction MSD: N=515345 d=90
'''
```

## Lists and links

* [Boston Housing](https://archive.ics.uci.edu/ml/machine-learning-databases/housing/)
* [Concrete Compression Strength](https://archive.ics.uci.edu/ml/datasets/Concrete+Compressive+Strength)
* [Energy efficiency](https://archive.ics.uci.edu/ml/datasets/energy+efficiency)
* [Kin8nm](https://github.com/zygmuntz/nonlinear-vowpal-wabbit/tree/master/kin8nm/data)
* [Naval Propulsion](https://archive.ics.uci.edu/ml/datasets/Condition+Based+Maintenance+of+Naval+Propulsion+Plants)
* [Combined Cycle Power Plant](https://archive.ics.uci.edu/ml/datasets/combined+cycle+power+plant)
* [Protein Structure](https://archive.ics.uci.edu/ml/datasets/Physicochemical+Properties+of+Protein+Tertiary+Structure)
* [Wine Quality Red](https://archive.ics.uci.edu/ml/datasets/wine+quality)
* [Yacht Hydrodynamics](http://archive.ics.uci.edu/ml/datasets/yacht+hydrodynamics)
* [Year Prediction MSD](https://archive.ics.uci.edu/ml/datasets/yearpredictionmsd)