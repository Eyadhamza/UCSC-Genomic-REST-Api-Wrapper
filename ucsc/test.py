from api import Genome, Track

#
myGenome = Genome.findBy('genomeName','hg38')

# myTrack = Track.findBy('hg38','longLabel','ClinGen curation activities (Dosage Sensitivity and Gene-Disease Validity)')
# for genome in Genome.getUCSCGenomes():
print(myGenome.findTrack('clinGenComp').__dict__)
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
