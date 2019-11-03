import setuptools

import os

data_list = []
for folder in os.listdir("probabilistic_backpropagation_dataset/raw"):
    data_list.append('raw/' + folder + '/*')

setuptools.setup(
    name="probabilistic-backpropagation-dataset-yiyuezhuo", # Replace with your own username
    version="0.0.1",
    author="yiyuezhuo",
    author_email="yiyuezhuo@gmail.com",
    description="Datasets used in PB paper(see readme.md for detail)",
    url="https://github.com/yiyuezhuo/probabilistic-backpropagation-dataset",

    packages=['probabilistic_backpropagation_dataset'],
    package_dir={'probabilistic_backpropagation_dataset': 'probabilistic_backpropagation_dataset'},
    package_data={'probabilistic_backpropagation_dataset': data_list},
)
