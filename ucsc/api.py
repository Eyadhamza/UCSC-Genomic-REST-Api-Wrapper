class Hub:
    def __init__(self, hubName):
        self.hubUrl = None
        self.hubName = hubName

    @staticmethod
    def getAllHubs():
        # call to api.genome.ucsc.edu/list/publicHubs
        return []

    def getHubGenomes(self):
        hubUrl = self.hubUrl
        # call to api.genome.ucsc.edu/list/hubGenomes?hubUrl=http://hgdownload.soe.ucsc.edu/hubs/mouseStrains/hub.txt
        pass





class Genome:
    def __init__(self, genomeName):
        # fetch the genome based on name
        # return the genome as an object with all required attributes
        self.genomeName = genomeName

    pass

    @staticmethod
    def getUCSCGenomes():
        #  api.genome.ucsc.edu/list/ucscGenomes
        return []


    def trackList(self):
        return []


class Track:
    def __init__(self, trackName):
        # fetch the track based on name
        # return the track as an object with all required attributes
        self.trackName = trackName



    def createShema(self, genome):
        # api.genome.ucsc.edu/list/schema?genome=hg38;track=knownGene
        return ''


class Chromosome:
    def __init__(self, genome =None, hub =None, track =None):
        # fetch the track based on name
        # return the track as an object with all required attributes
        self.trackName = trackName

    @staticmethod
    def getChromosomes(genome =None, hub =None, track =None):
        return []


# returns list of available hubs names and url (can be overriding by parameter)
hubList = Hub.getAllHubs()

hubName = 'ALFA Hub'  # researcher will choose his desired hub based on short label

hub = Hub(hubName)  # an object has every attribute of hub

# get all genomes from specified hub object
hub.getHubGenomes()

# get all genomes from all UCSC Database
genomesList = Genome.getUCSCGenomes()

genomeName = 'CAST_EiJ'  # researcher will choose his desired genome based on name

genome = Genome(genomeName)  # an object has every attribute of genome


tracks = genome.trackList()

trackName = 'affyGnf1h'

track = Track(trackName)  # an object has every attribute of track

# list chromosomes from specified track in UCSC database genome

# list schema from specified track in UCSC database genome
trackSchema = track.createShema(genome)

# duplication needs to be removed of course ! WARNING
# list chromosomes from assembly hub genome -

# list chromosomes from specified track in assembly hub genome -

# only one function to get the list of chromosomes

# list chromosomes from UCSC database genome then hub and track = None
chromosomes1 = Chromosome.getChromosomes(genome)

# list chromosomes from specified track in UCSC database genome
chromosomes2 = Chromosome.getChromosomes(genome, track=track)

# list chromosomes from assembly hub genome
chromosomes3 = Chromosome.getChromosomes(genome, hub)

# list chromosomes from specified track in assembly hub genome

chromosomes4 = Chromosome.getChromosomes(genome, hub, track)
