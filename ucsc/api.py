import requests

BASE_URL = 'http://api.genome.ucsc.edu'


class Hub:  # yasmeen
    hubUrl = ''

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


class Genome:  # eyad
    def __init__(self, genomeName, genome=None, description=None, nibPath=None
                 , organism=None, defaultPos=None, active=None,
                 orderKey=None, scientificName=None,
                 htmlPath=None, hgNearOk=None, hgPbOk=None, sourceName=None, taxId=None):

        self.genomeName = genomeName
        self.genome = genome
        # call to find genome
        self.taxId = taxId
        self.sourceName = sourceName
        self.hgPbOk = hgPbOk
        self.hgNearOk = hgNearOk
        self.htmlPath = htmlPath
        self.scientificName = scientificName
        self.orderKey = orderKey
        self.active = active
        self.defaultPos = defaultPos
        self.nibPath = nibPath
        self.organism = organism
        self.description = description

        # fetch the genome based on name
        # return the genome as an object with all required attributes

    pass

    @staticmethod
    def get():

        response = requests.get(BASE_URL + '/list/ucscGenomes').json()
        myList = []
        for key in response['ucscGenomes']:
            myList.append(Genome(key, **response['ucscGenomes'][key]))
        return myList

    @staticmethod
    def exists(genomeName):
        for genome in Genome.get():
            if genome.genomeName == genomeName:
                return True

        return False

    @property
    def tracks(self):
        return Track.get(self.genomeName)

    def findTrack(self, trackName):
        return Track.find(self.genomeName, trackName)

    @staticmethod
    def find(genomeName):
        for genome in Genome.get():
            if genome.genomeName == genomeName:
                print('genome found')
                return genome
        raise Exception("can't find genome, Genome does not exist")

    @staticmethod
    def findBy(genomeAttribute, value):
        for genome in Genome.get():
            if getattr(genome, genomeAttribute) == value:
                print('genome found')
                return genome
        raise Exception("can't find genome, Genome does not exist")


class Track:  # mazen
    def __init__(self,trackName, **kwargs):
        # fetch the track based on name
        # return the track as an object with all required attributes
        self.trackName = trackName
        self.caddT = kwargs.get('caddT')
        self.superTrack = kwargs.get('superTrack')
        self.maxWindowToDraw = kwargs.get('maxWindowToDraw')
        self.bismapBigWig = kwargs.get('bismapBigWig')
        self.bismapBigBed = kwargs.get('bismapBigBed')
        self.noInherit = kwargs.get('noInherit')
        self.html = kwargs.get('html')
        self.parent = kwargs.get('parent')
        self.baseColorUseCds = kwargs.get('baseColorUseCds')
        self.baseColorDefault = kwargs.get('baseColorDefault')
        self.showCdsMaxZoom = kwargs.get('showCdsMaxZoom')
        self.showDiffBasesMaxZoom = kwargs.get('showDiffBasesMaxZoom')
        self.color = kwargs.get('color')
        self.showDiffBasesAllScales = kwargs.get('showDiffBasesAllScales')
        self.showCdsAllScales = kwargs.get('showCdsAllScales')
        self.baseColorUseSequence = kwargs.get('baseColorUseSequence')
        self.indelQueryInsert = kwargs.get('indelQueryInsert')
        self.pennantIcon = kwargs.get('pennantIcon')
        self.indelDoubleInsert = kwargs.get('indelDoubleInsert')
        self.dbSnp153ViewErrs = kwargs.get('dbSnp153ViewErrs')
        self.dbSnp153ViewVariants = kwargs.get('dbSnp153ViewVariants')
        self.url = kwargs.get('url')
        self.urlLabel = kwargs.get('urlLabel')
        self.priority = kwargs.get('priority')
        self.compositeTrack = kwargs.get('compositeTrack')
        self.subGroup1 = kwargs.get('subGroup1')
        self.compositeContainer = kwargs.get('compositeContainer')
        self.group = kwargs.get('group')
        self.visibility = kwargs.get('visibility')
        self.itemCount = kwargs.get('itemCount')
        self.longLabel = kwargs.get('longLabel')
        self.type = kwargs.get('type')
        self.shortLabel = kwargs.get('shortLabel')

    @staticmethod
    def exists(genomeName, trackName):
        for track in Track.get(genomeName):
            if track.trackName == trackName:
                return True

        return False

    @staticmethod
    def get(genomeName):

        response = requests.get(BASE_URL + '/list/tracks', {'genome': genomeName}).json()
        myList = []
        for key in response[genomeName]:
            myList.append(Track(key, **response[genomeName][key]))
        return myList

    @staticmethod
    def find(genomeName, trackName):
        for track in Track.get(genomeName):
            if track.trackName == trackName:
                return track
        raise Exception("can't find track, Track does not exist")

    @staticmethod
    def findBy(genomeName, trackAttribute, value):
        for track in Track.get(genomeName):
            if getattr(track, trackAttribute) == value:
                print('track found')
                return track
        raise Exception("can't find track, Genome does not exist")



    def schema(self, genomeName):
        return Schema.get(genomeName, self.trackName)


class Schema:
    def __init__(self, **kwargs):
        self.name = kwargs['name'],
        self.sqlType = kwargs['sqlType'],
        self.jsonType = kwargs['jsonType']
        self.description = kwargs['description']

    @staticmethod
    def get(genomeName, trackName):
        response = requests.get(BASE_URL + '/list/schema', {'genome': genomeName, 'track': trackName}).json()
        myList = []

        for key in response['columnTypes']:
            myList.append(Schema(**key))
        return myList


class Chromosome:  # salma
    def __init__(self, trackName=None, hub=None, track=None):
        # fetch the track based on name
        # return the track as an object with all required attributes
        self.trackName = trackName

    @staticmethod
    def getChromosomes(genome=None, hub=None, track=None):
        return []


class Sequence:  # sohaila
    def __init__(self, genome, chromosome, hub=None, track=None, chromStart=None, chromEnd=None):
        # must return the
        self.dna = None
        #
