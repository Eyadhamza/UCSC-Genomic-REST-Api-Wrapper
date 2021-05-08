from ucsc.api import Genome, Track, Hub, Chromosome, Sequence

track = Track('gold')
# Track.get('asdasdasd')
track.downloadData(genome='hg3adas8',maxItemsOutput=10)

#
# myGenome = Genome.find('hg38')


# myTrack = Track.findBy('hg38','longLabel','ClinGen curation activities (Dosage Sensitivity and Gene-Disease Validity)')
# # for genome in Genome.getUCSCGenomes():
# for i in Hub.get():
#     print(i.__dict__)


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
