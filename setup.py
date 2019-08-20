import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-divinorum",
    version="0.0.1",
    author="Elliott Stam",
    author_email="elliott.stam@gmail.com",
    description="An example package for PyPI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/divinorum-webb/example_pkg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
