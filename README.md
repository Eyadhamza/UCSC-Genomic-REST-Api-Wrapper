# UCSC-Genomic-REST-Api-Wrapper
An open-source python package licensed under the MIT license, the package represents a python Api wrapper on the UCSC genomic database, which makes it much easier for researchers to access and query the database with an elegant and human readable Api

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

## About The Package

[Project Proposal](https://github.com/Eyadhamza/UCSC-Genomic-REST-Api-Wrapper/blob/main/UCSC%20Genomic%20REST%20Api%20Wrapper.pdf)


## Features

-  Expressive Api

-  Easy to use

-  Can be extended
  
-  Can be reused.

-  No boilerplate  

## Installation 

Install ucsc with pip

```bash 
  pip install ucsc-genomic-api
```

## Documentation

### Quick Introduction for busy developers

There are 6 primary classes in the package:

``` python
from ucsc.api import Hub, Genome, Track, TrackSchema, Chromosome, Sequence  
```



Each class has the following primary method:

``` python
# check documentation for required and optional parameters

className.get()  # Returns list of objects of the class

className.find()  # Find object by name

className.findBy()  # Find object by a specified attribute

className.exists()  # Check to see if an object exists
```


Then you can access the attributes of the object using . notation
``` python
className.attributeName # Returns attribute name
```



    

## Usage guide

List of available hubs as python objects 


```python
from ucsc.api import Hub  

hubList = Hub.get()
```


Find hub by name, the function will return the result as an object or throws a not found exception


```python 
from ucsc.api import Hub  

hub = Hub.find('ALFA Hub') 
```

Find hub by given attribute, the function will return the result as an object or throws a not found exception


```python
from ucsc.api import Hub  

hub = Hub.findBy('hubName','ALFA Hub') 
```


Get all genomes from specified hub object
  

```python
from ucsc.api import Hub  

hub = Hub.find('ALFA Hub')

print(hub.genomes) # prints the list of all genomes in the given hub

``` 


Get all genomes from all UCSC Database


```python
from ucsc.api import Genome 

genomesList = Genome.get() 
```



Find genome by name, the function will return the result as an object or throws a not found exception

```python
from ucsc.api import Genome 

genome = Genome.find('ALFA Genome') 
```  

Find genome by given attribute, the function will return the result as an object or throws a not found exception



```python
from ucsc.api import Genome  

genome = Genome.findBy('genomeName','ALFA Genome') 
```

Check if genome exists in a UCSC database

```python
from ucsc.api import Genome

Genome.exists('hg38') 
```

List the available tracks of the genome object


```python
from ucsc.api import Genome 

genome = Genome.find('ALFA Genome') 
tracks = genome.tracks 
```

 
Find a specific track in a genome by name, the return type is an object of track

```python
from ucsc.api import Track 

track = Track.find('hg38','knownGene') 

```
Or using a Genome object



```python 
from ucsc.api import Genome 

genome.findTrack('knownGene')
```

Find a specific track using a specific attribute, the return type is an object of track


```python
from ucsc.api import Track

track = Track.findBy('hg38','longLabel','ClinGen curation ') 
```

Or using a Genome object


```python 
from ucsc.api import Genome 

genome.findTrackBy('longLabel','knownGene')
```

Check if track exists in a genome


```python
from ucsc.api import Track 

Track.exists('hg38','knownGene') 
```

Or using a Genome object

```python 
from ucsc.api import Genome 

genome.isTrackExists('longLabel')
```

List the schema of specified track from given genome 



```python
from ucsc.api import Track 

track = Track.find('hg38','knownGene') 

trackSchema = track.schema('hg38')
```

Get track data depends on the parameter you will pass to the trackData function, listed below the possible parameter for each use case
```python
from ucsc.api import Track 

track = Track.find('hg38','knownGene') # or you can get the track using the findBy method

# Get track data for specified track in UCSC database genome 

track.trackData(genome='hg38',track='gold',maxItemsOutput=100)

# Get track data for specified track and chromosome in UCSC database genome 

track.trackData(genome='hg38',track='gold',chrom='chrM')

# Get track data for specified track, chromosome and start,end coordinates in UCSC database genome 

track.trackData(genome='hg38',track='gold',chrom='chr1',start=47000,end=48000)

# Get track data for specified track in an assembly hub genome -
hubUrl='http://hgdownload.soe.ucsc.edu/hubs/mouseStrains/hub.txt'

track.trackData(genome='CAST_EiJ',track='assembly',hubUrl=hubUrl)


# Get track data for specified track and chromosome in an assembly hub genome 
hubUrl='http://hgdownload.soe.ucsc.edu/hubs/mouseStrains/hub.txt'

track.trackData(genome='CAST_EiJ',track='assembly',chrom='chr1',hubUrl=hubUrl)

# Get track data for specified track in a track hub -

hubUrl='http://hgdownload.soe.ucsc.edu/hubs/mouseStrains/hub.txt'

track.trackData(genome='CAST_EiJ',track='ensGene',hubUrl=hubUrl)


# Get track data for specified track and chromosome in a track hub 

hubUrl='http://hgdownload.soe.ucsc.edu/hubs/mouseStrains/hub.txt'

track.trackData(genome='CAST_EiJ',track='ensGene',chrom='chr1',hubUrl=hubUrl)


# Download track data for specified track, chromosome with start and end limits in an assembly hub genome -
hubUrl='http://hgdownload.soe.ucsc.edu/hubs/mouseStrains/hub.txt'

track.downloadData(genome='CAST_EiJ',track='ensGene',chrom='chr1',hubUrl=hubUrl,start=4321,end=5678)

# Download track data for specified track in a UCSC database genome 
track.downloadData(genome='galGal6',track='gc5BaseBw',maxItemsOutput=100)

```





List chromosomes from UCSC database genome 

```python
from ucsc.api import Chromosome 

chromosomes = Chromosome.get(genome='hg38')
```

List chromosomes from specified track in UCSC database genome



```python
from ucsc.api import Chromosome

chromosomes = Chromosome.get(genome='hg38', track='knownGene')

# or 

from ucsc.api import Track,Genome

track = Track.find('hg38','knownGene') 

genome = Genome.find('ALFA Genome')

chromosomes = Chromosome.get(genome, track)
```


List chromosomes from assembly hub genome


```python
from ucsc.api import Chromosome 

chromosomes = Chromosome.get(hub='ALFA Hub')
```

List chromosomes from specified track in assembly hub genome # Deprected!


``` python
from ucsc.api import Chromosome 

chromosomes = Chromosome.get('hg38', 'ALFA Hub','knownGene')
```

Find Specific chromosome
``` python
from ucsc.api import Chromosome 
```

``` python
chromosome = Chromosome.find(genome)
```


Find DNA sequence

The get method in Sequence class accepts multiple parameter, which depends on how do you want to retrieve the sequence object




```python
from ucsc.api import Sequence 


# Get DNA sequence from specified chromosome in UCSC database genome -

sequence = Sequence.get(genome = 'hg38',chrom= 'chrM')

print(sequence.dna)

# Get DNA sequence from specified chromosome and start,end coordinates in UCSC database genome -

sequence = Sequence.get(genome= 'hg38',chrom= 'chrM',start=4321,end=5678)

print(sequence.dna)

# Get DNA sequence from a track hub where 'genome' is a UCSC database -

hubUrl = 'http://hgdownload.soe.ucsc.edu/hubs/mouseStrains/hub.txt';

sequence = Sequence.get(genome= 'mm10',chrom= 'chrM',hubUrl=hubUrl,start=4321,end=5678)

print(sequence.dna)

```
