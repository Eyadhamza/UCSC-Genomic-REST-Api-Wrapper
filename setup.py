from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='ucsc-genomic-api',
    packages=['ucsc'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='1.0.0',
    license='MIT',
    description='access and query the UCSC database with an elegant and human readable Api',
    author='Eyad Hamza',
    author_email='eyadhamza0@outlook.com',
    url='https://github.com/Eyadhamza/UCSC-Genomic-REST-Api-Wrapper',
    download_url='https://github.com/Eyadhamza/UCSC-Genomic-REST-Api-Wrapper/releases/tag/1.0.0',
    keywords=['python', 'genomic', 'bioinformatics', 'bio', 'genomes', 'ucsc'],
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.6',
    ],
)