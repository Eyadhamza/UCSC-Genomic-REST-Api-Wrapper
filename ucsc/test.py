from api import Genome
#
# genome = Genome('hg38')
#
# print(genome.name)
# print(Genome('11111111111111111').genomeName)
genome = Genome('hg38')

for i in genome.tracks:
    print(i.__dict__)


