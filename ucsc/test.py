from api import Genome
#
# genome = Genome('hg38')
#
# print(genome.name)
for i in Genome.getUCSCGenomes():
    print(i.genomeName)

