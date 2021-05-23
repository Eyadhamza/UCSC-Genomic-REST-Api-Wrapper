from distutils.core import setup

setup(
    name='ucsc-genomic',
    packages=['ucsc'],
    version='1.0.0',
    license='MIT',
    description='An open-source python package licensed under the MIT license, the package represents a python Api wrapper on the UCSC genomic database, which makes it much easier for researchers to access and query the database with an elegant and human readable Api',
    author='Eyad Hamza',
    author_email='eyadhamza0@outlook.com',
    url='https://github.com/Eyadhamza/UCSC-Genomic-REST-Api-Wrapper',
    download_url='https://github.com/Eyadhamza/UCSC-Genomic-REST-Api-Wrapper/releases/tag/1.0.0',
    keywords=['python', 'genomic', 'bioinformatics', 'bio', 'genomes', 'ucsc'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.6',
    ],
)