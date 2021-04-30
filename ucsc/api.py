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

    def getChromosomes(self, genome):
        # api.genome.ucsc.edu/list/chromosomes?hubUrl=http://hgdownload.soe.ucsc.edu/hubs/mouseStrains/hub.txt;genome=CAST_EiJ

        return []

    def getTrackChromosomes(self, genome, track):
        # api.genome.ucsc.edu/list/chromosomes?hubUrl=hubUrl=http://hgdownload.soe.ucsc.edu/hubs/mouseStrains/hub.txt;genome=CAST_EiJ;track=assembly

        return []


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

    def getChromosomes(self):
        # call to list chromosomes from UCSC database genome -
        # api.genome.ucsc.edu/list/chromosomes?genome=hg38

        return []

    def trackList(self):
        return []


class Track:
    def __init__(self, trackName):
        # fetch the track based on name
        # return the track as an object with all required attributes
        self.trackName = trackName

    def getTrackChromosomes(self, genome):
        # list chromosomes from specified track in UCSC database genome
        # api.genome.ucsc.edu/list/chromosomes?genome=hg38;track=gold
        return []

    def createShema(self, genome):
        # api.genome.ucsc.edu/list/schema?genome=hg38;track=knownGene
        return ''


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

chromosomes = genome.getChromosomes()

tracks = genome.trackList()

trackName = 'affyGnf1h'

track = Track(trackName)  # an object has every attribute of track


# list chromosomes from specified track in UCSC database genome
trackChromosomes = track.getTrackChromosomes(genome)

# list schema from specified track in UCSC database genome
trackSchema = track.createShema(genome)

# duplication needs to be removed of course ! WARNING
# list chromosomes from assembly hub genome -
chromosomes2 = hub.getChromosomes(genome)


# list chromosomes from specified track in assembly hub genome -
trackChromosomes2 = hub.getTrackChromosomes(genome, track)



