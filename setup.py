from setuptools import setup, find_packages
import codecs
import os


VERSION = '1.0.0'
DESCRIPTION = 'UCSC-Genomic-REST-Api-Wrapper'
LONG_DESCRIPTION = 'An open-source python package licensed under the MIT license, the package represents a python Api wrapper on the UCSC genomic database, which makes it much easier for researchers to access and query the database with an elegant and human readable Api.'

# Setting up
setup(
    name="ucsc",
    version=VERSION,
    author="Eyadhamza",
    author_email="eyadhamza0@outlook.com",
    description='access and query the ucsc database with an elegant and human readable Api',
    long_description_content_type="text/markdown",
    long_description='An open-source python package licensed under the MIT license, the package represents a python Api wrapper on the UCSC genomic database, which makes it much easier for researchers to access and query the database with an elegant and human readable Api',

    packages=find_packages(),
    install_requires=['requests', 'urllib'],
    keywords=['python', 'genomic', 'bioinformatics', 'bio', 'genomes', 'ucsc'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)