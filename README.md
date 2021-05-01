# UCSC-Genomic-REST-Api-Wrapper
An open-source python package licensed under the MIT license, the package represents a python Api wrapper on the UCSC genomic database, which makes it much easier for researchers to access and query the database with an elegant and human readable Api

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

## Documentation 

 list of available hubs as python objects 

``` from ucsc.api import Hub  ```

``` hubList = Hub.get() ```


Find hub by name, the function will return the result as an object or throws a not found exception

``` from ucsc.api import Hub  ```

``` hub = Hub.find('ALFA Hub') ```  

Find hub by given attribute, the function will return the result as an object or throws a not found exception

``` from ucsc.api import Hub  ```

``` hub = Hub.find('hubName','ALFA Hub') ```


Get all genomes from specified hub object
  
``` from ucsc.api import Hub  ```

``` hub = Hub.getGenomes('ALFA Hub') ``` 


Get all genomes from all UCSC Database

``` from ucsc.api import Genome ```

```  genomesList = Genome.get() ```



Find genome by name, the function will return the result as an object or throws a not found exception

``` from ucsc.api import Genome ```

``` genome = Genome.find('ALFA Genome') ```  

Find genome by given attribute, the function will return the result as an object or throws a not found exception

``` from ucsc.api import Genome  ```

``` genome = Genome.findBy('genomeName','ALFA Genome') ```

Check if genome exists in a UCSC database

``` from ucsc.api import Genome ```

```
 Genome.exists('hg38') 
```

List the available tracks of the genome object

``` from ucsc.api import Genome ```

``` 
genome = Genome.find('ALFA Genome') 
tracks = genome.tracks 
```

 
Find a specific track in a genome by name, the return type is an object of track

``` from ucsc.api import Track ```

``` track = Track.find('hg38','knownGene') ```

Find a specific track using a specific attribute, the return type is an object of track

``` from ucsc.api import Track ```

``` track = Track.findBy('hg38','longLabel','ClinGen curation ') ```

Check if track exists in a genome

``` from ucsc.api import Track ```

``` Track.exists('hg38','knownGene') ```

  list chromosomes from specified track in UCSC database genome

  list schema from specified track in UCSC database genome
 trackSchema = track.createShema(genome)

  only one function to get the list of chromosomes

  list chromosomes from UCSC database genome then hub and track = None
 chromosomes1 = Chromosome.getChromosomes(genome)

  list chromosomes from specified track in UCSC database genome
 chromosomes2 = Chromosome.getChromosomes(genome, track=track)

  list chromosomes from assembly hub genome
 chromosomes3 = Chromosome.getChromosomes(genome, hub)

  list chromosomes from specified track in assembly hub genome
 chromosomes4 = Chromosome.getChromosomes(genome, hub, track)

 chromosome = Chromosome(genome)

 chromStart = 123
 chromEnd = 543

 sequence = Sequence(hub, genome, track, chromosome, chromStart, chromEnd)

  sequence.dna
