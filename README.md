# UCSC-Genomic-REST-Api-Wrapper
An open-source python package licensed under the MIT license, the package represents a python Api wrapper on the UCSC genomic database, which makes it much easier for researchers to access and query the database with an elegant and human readable Api

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

## Documentation 

Below you will find the api wrapper details:

### Quick Introduction for busy developers
There are 6 primary classes in the package:

Hub, Genome, Track, TrackSchema, Chromosome, Sequence

Each class has the following primary method:

get : returns list of objects of the class

find : Find object by name

findBy : Find object by a specified attribute

exists : Check to see if an object exists

Then you can access the attributes of the object using . notation


List of available hubs as python objects 

``` 
from ucsc.api import Hub  
```

``` 
hubList = Hub.get() 
```


Find hub by name, the function will return the result as an object or throws a not found exception

``` 
from ucsc.api import Hub  
```

``` 
hub = Hub.find('ALFA Hub') 
```  

Find hub by given attribute, the function will return the result as an object or throws a not found exception

``` 
from ucsc.api import Hub  
```

``` 
hub = Hub.find('hubName','ALFA Hub') 
```


Get all genomes from specified hub object
  
``` 
from ucsc.api import Hub  
```

``` 
hub = Hub.getGenomes('ALFA Hub') 
``` 


Get all genomes from all UCSC Database

``` 
from ucsc.api import Genome 
```

```  
genomesList = Genome.get() 
```



Find genome by name, the function will return the result as an object or throws a not found exception

``` 
from ucsc.api import Genome 
```

``` 
genome = Genome.find('ALFA Genome') 
```  

Find genome by given attribute, the function will return the result as an object or throws a not found exception

``` 
from ucsc.api import Genome  
```

``` 
genome = Genome.findBy('genomeName','ALFA Genome') 
```

Check if genome exists in a UCSC database

``` 
from ucsc.api import Genome
 ```

```
 Genome.exists('hg38') 
```

List the available tracks of the genome object

``` 
from ucsc.api import Genome 
```

``` 
genome = Genome.find('ALFA Genome') 
tracks = genome.tracks 
```

 
Find a specific track in a genome by name, the return type is an object of track

``` 
from ucsc.api import Track 
```

``` 
track = Track.find('hg38','knownGene') 
```

Find a specific track using a specific attribute, the return type is an object of track

``` 
from ucsc.api import Track
 ```

``` 
track = Track.findBy('hg38','longLabel','ClinGen curation ') 
```

Check if track exists in a genome

``` 
from ucsc.api import Track 
```

``` 
Track.exists('hg38','knownGene') 
```
List the schema of specified track from given genome 

``` 
from ucsc.api import Track 
```

``` 
track = Track.find('hg38','knownGene') 

trackSchema = track.schema('hg38')
```

List chromosomes from UCSC database genome 

``` 
from ucsc.api import Chromosome 
```

``` 
chromosomes = Chromosome.get('hg38')
```

List chromosomes from specified track in UCSC database genome

``` 
from ucsc.api import Chromosome 
```

```
chromosomes = Chromosome.get('hg38', 'knownGene')

# or
track = Track.find('hg38','knownGene') 
genome = Genome.find('ALFA Genome')
chromosomes = Chromosome.get(genome, track)
```


List chromosomes from assembly hub genome

``` 
from ucsc.api import Chromosome 
```

```
chromosomes = Chromosome.get('hg38', 'ALFA Hub')
```

List chromosomes from specified track in assembly hub genome

``` 
from ucsc.api import Chromosome 
```

```
chromosomes = Chromosome.get('hg38', 'ALFA Hub','knownGene')
```

Find Specific chromosome
``` 
from ucsc.api import Chromosome 
```

```
chromosome = Chromosome.find(genome)
```


Find DNA sequence
``` 
from ucsc.api import Sequence 
```

```
chromStart = 123
chromEnd = 543

sequence = Sequence.find('hg38', 'ALFA Hub','knownGene', 'Chrm', chromStart, chromEnd)
# this will return a sequence object, you can then access the sequence data using :
print(sequence.dna)
```

