import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="probabilistic-backpropagation-dataset-yiyuezhuo", # Replace with your own username
    version="0.0.1",
    author="yiyuezhuo",
    author_email="yiyuezhuo@gmail.com",
    description="Datasets used in PB paper(see readme.md for detail)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yiyuezhuo/probabilistic-backpropagation-dataset",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
