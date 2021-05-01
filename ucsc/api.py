import requests

BASE_URL = 'http://api.genome.ucsc.edu'


class Hub:  # yasmeen

    def __init__(self,**kwargs):

        self.shortLabel = kwargs.get('shortLabel')
        self.hubUrl = kwargs.get('hubUrl')
        self.longLabel = kwargs.get('longLabel')
        self.registrationTime = kwargs.get('registrationTime')
        self.dbCount = kwargs.get('dbCount')
        self.dbList = kwargs.get('dbList')
        self.descriptionUrl = kwargs.get('descriptionUrl')


    @staticmethod
    def get():
        response = requests.get(BASE_URL + '/list/publicHubs').json()
        myList = []
        for key in response['publicHubs']:
            myList.append(Hub(**key))
        return myList


    def getGenomes(self):
        return Genome.get(self.hubUrl)
        # call to api.genome.ucsc.edu/list/hubGenomes?hubUrl=http://hgdownload.soe.ucsc.edu/hubs/mouseStrains/hub.txt



class Genome:  # eyad
    def __init__(self, genomeName, **kwargs):

        self.genomeName = genomeName
        self.genome = kwargs.get('genome')
        # call to find genome
        self.taxId = kwargs.get('taxId')
        self.sourceName = kwargs.get('sourceName')
        self.hgPbOk = kwargs.get('hgPbOk')
        self.hgNearOk = kwargs.get('hgNearOk')
        self.htmlPath = kwargs.get('htmlPath')
        self.scientificName = kwargs.get('scientificName')
        self.orderKey = kwargs.get('orderKey')
        self.active = kwargs.get('active')
        self.defaultPos = kwargs.get('defaultPos')
        self.nibPath = kwargs.get('nibPath')
        self.organism = kwargs.get('organism')
        self.description = kwargs.get('description')

        # fetch the genome based on name
        # return the genome as an object with all required attributes

    pass

    @staticmethod
    def get(hubUrl=None):
        genomesRequest = 'ucscGenomes' if hubUrl is None else 'hubGenomes'

        response = requests.get(BASE_URL + f'/list/{genomesRequest}', {'hubUrl':hubUrl}).json()
        myList = []
        genomesResponse = 'ucscGenomes' if hubUrl is None else 'genomes'

        for key in response[genomesResponse]:
            myList.append(Genome(key, **response[genomesResponse][key]))
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
