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


# returns list of available hubs names and url (can be overriding by parameter)
hubList = Hub.getAllHubs()

hubName = 'ALFA Hub'  # researcher will choose his desired hub based on short label

hub = Hub(hubName)  # an object has every attribute of hub

# get all genomes from specified hub object
hub.getHubGenomes()


# get all genomes from all UCSC Database
genomesList = Genome.getUCSCGenomes()

genomeName = 'CAST_EiJ'  # researcher will choose his desired genome based on name

genome = Genome(genomeName) # an object has every attribute of genome

