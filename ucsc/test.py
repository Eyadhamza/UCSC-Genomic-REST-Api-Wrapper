from api import Genome
#
genome = Genome.constructGenome('nomLeu2')
print(genome.__dict__)
for genome in Genome.getUCSCGenomes():
    print(genome.__dict__)

#
# print(genome.name)
# print(Genome('11111111111111111').genomeName)
# genome = Genome('hg38')
#
# for i in genome.tracks:
#     print(i.__dict__)


