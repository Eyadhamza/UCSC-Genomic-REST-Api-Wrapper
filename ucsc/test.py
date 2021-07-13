import requests

from ucsc.api import Genome, Track, Hub, Chromosome, Sequence


# genome = Genome.findBy('name', 'hg38asdasd')
# tracks = genome.tracks
#
# for track in tracks:
#     print(track.__dict__)


# get the wuhCor1 from the UCSC database and return a python object
genome = Genome.find('wuhCor1')

# wanna access the attributes?
print(genome.name)
print(genome.organism)
print(genome.__dict__) # to return all attributes in the object


# want to get the tracks?
tracks = genome.tracks

# wanna see details of tracks object
for track in tracks:
    print(track.__dict__)

# you can also loop over the tracks, which is basically a list of objects
# you can also find specific track using the given methods!
# you noticed a track named microdel, you wanna know more about it
track = genome.findTrack('microdel')


# don't know the name?
# don't be nervous, you can access it using any attribute

track = genome.findTrackBy('shortLabel','Microdeletions')

# you now have a track object, you want to get all it's related data?
# i mean you wanna get all its fragments

trackFragments = track.getTrackData(genome='wuhCor1')

print(trackFragments[0].__dict__) # you get the details of fragment object

# Get track data for specified track and chromosome in wuhCor1
# You can also specify other flags, check usage for more details.

chromosomeFragment = track.getTrackData(genome='wuhCor1', chrom='NC_045512v2')


# Wanna download them for offline processing?
hubUrl = 'http://hgdownload.soe.ucsc.edu/hubs/mouseStrains/hub.txt'

track.downloadData(genome='wuhCor1', chrom='NC_045512v2', hubUrl=hubUrl, start=4321, end=5678)

# You studied the track data, you analyzed chromosomes, you want to get a
# Sequence data from a given chromosome..

sequence = Sequence.get(genome = 'wuhCor1',chrom= 'chrM')

print(sequence.dna)

# Get DNA sequence from specified chromosome and start,end coordinates in UCSC database genome -

sequence = Sequence.get(genome= 'wuhCor1',chrom= 'chrM',start=4321,end=5678)

print(sequence.dna)

# process any of the data you just retrieved and saved to variables
# code!


# response = requests.get('http://api.genome.ucsc.edu/list/ucscGenomes').json()
# genome = ''
# for key in response:
#     if key == 'wuhCor1':
#         genome = key
#     else:
#         genome = ''
# # well, you found it, you made sure it exists



# hub = Hub.findBy('name','ALFA Hub')
#
# print(hub.__dict__)
#
# hubs = Hub.get()
# for i in hubs:
#     print(i.__dict__)
# hub = Hub.find('ALFA Hub')
#
# print(hub.genomes.__dict__)
# print(hub.__dict__)

# track = Track('gold')
#
#
# sequence = Sequence.get(genome = 'mm10',chrom= 'chrM')
# print(sequence.__dict__)

#Sequence.getByGenomeChrom('hg38','chrM')

#Hub.get()

# track.downloadData(genome='hg3adas8',maxItemsOutput=10)

#
# myGenome = Genome.find('hg38')


# myTrack = Track.findBy('hg38','longLabel','ClinGen curation activities (Dosage Sensitivity and Gene-Disease Validity)')
# # for genome in Genome.getUCSCGenomes():


#for i in Hub.get():
 #   print(i.__dict__)

# print(myGenome.tracks)

#
# print(genome.name)
# print(Genome('11111111111111111').genomeName)
# genome = Genome('hg38')
#
# for i in genome.tracks:
#     print(i.__dict__)


# @staticmethod
#     def findBy(genomeAttribute,value):
#         myList = []
#         for genome in Genome.UCSCGenomes():
#
#             if getattr(genome, genomeAttribute) == value:
#                 print('genome found')
#                 myList.append(genome)
#         return myList
