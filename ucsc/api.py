import requests
import urllib.request

BASE_URL = 'http://api.genome.ucsc.edu'


class NotFoundException(Exception):
    pass


class NotAllowedException(Exception):
    pass


def raiseExceptionOfRequest(response):
    if response.get('statusCode') == 400:
        raise NotFoundException('Something went wrong, ' + response.get('error'))

    if response.get('statusCode') == 403:
        raise NotAllowedException('The Requested Resource is not allowed to be accessed' + response.get('error'))

    if response.get('error') is not None:
        raise NotFoundException('An error happened, ' + response.get('error'))

    pass


class Model:
    requestUrl = ''
    requestParams = {}
    responseKey = ''

    @classmethod
    def makeGetRequest(cls):

        response = requests.get(cls.requestUrl, cls.requestParams).json()
        raiseExceptionOfRequest(response)
        return response

    @classmethod
    def get(cls, *param):
        response = cls.makeGetRequest()
        return cls.buildList(response)

    @classmethod
    def find(cls, name, *param):
        for item in cls.get(*param):
            if item.name == name:
                return item
        raise NotFoundException("can't find" + name + " in the list of " + item.__class__.__name__ + "s it does not exist")

    @classmethod
    def findBy(cls, itemAttribute, value, *param):
        for item in cls.get(*param):
            if getattr(item, itemAttribute) == value:
                return item
        raise NotFoundException("can't find" + value + " in the list of " + item.__class__.__name__ + "s it does not exist")

    @classmethod
    def exists(cls, name, *param):

        for item in cls.get(*param):
            if item.name == name:
                return True
        return False

    @classmethod
    def buildList(cls, response):
        pass


class Hub(Model):
    requestUrl = BASE_URL + '/list/publicHubs'
    responseKey = 'publicHubs'

    def __init__(self ,**kwargs):

        self.name = kwargs.get('shortLabel')
        self.hubUrl = kwargs.get('hubUrl')
        self.longLabel = kwargs.get('longLabel')
        self.registrationTime = kwargs.get('registrationTime')
        self.dbCount = kwargs.get('dbCount')
        self.dbList = kwargs.get('dbList')
        self.descriptionUrl = kwargs.get('descriptionUrl')

    @property
    def genomes(self):
        return Genome.get(self.hubUrl)

    @classmethod
    def buildList(cls,response):
        myList = []
        for key in response[cls.responseKey]:
            myList.append(cls(**key))
        return myList

class Genome(Model):
    requestUrl = ''
    requestParams = {}
    responseKey = ''

    def __init__(self, name, **kwargs):
        self.name = name
        self.genome = kwargs.get('genome')
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

    @classmethod
    def buildList(cls, response):
        myList = []
        for key in response[cls.responseKey]:
            myList.append(cls(key, **response[cls.responseKey][key]))
        return myList

    @classmethod
    def get(cls, hubUrl=None):
        Genome.requestUrl = BASE_URL + f'/list/{Genome.getUrl(hubUrl)}'
        Genome.requestParams = {'hubUrl': hubUrl}
        Genome.responseKey = Genome.getKeyOfResponse(hubUrl)
        return super().get()
    @classmethod
    def find(cls, name, *param):
        return super().find(name)

    @property
    def tracks(self):
        return Track.get(self.name)

    def findTrack(self, trackName):
        return Track.find(trackName, self.name)

    def findTrackBy(self, attributeName, trackName):
        return Track.findBy(attributeName, trackName, self.name)

    def isTrackExists(self, trackName):
        return Track.exists(trackName, self.name)

    @classmethod
    def getKeyOfResponse(cls, hubUrl):
        return 'ucscGenomes' if hubUrl is None else 'genomes'

    @classmethod
    def getUrl(cls, hubUrl):
        return 'ucscGenomes' if hubUrl is None else 'hubGenomes'


class Track(Model):
    requestUrl = ''
    requestParams = {}
    responseKey = ''
    genome = ''

    def __init__(self, name, **kwargs):
        self.name = name
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

    @classmethod
    def buildList(cls, response):
        myList = []
        for key in response[cls.responseKey]:
            myList.append(cls(key, **response[cls.responseKey][key]))
        return myList

    @classmethod
    def get(cls, genomeName):
        Track.requestUrl = BASE_URL + '/list/tracks'
        Track.requestParams = {'genome': genomeName}
        Track.responseKey = genomeName
        Track.genome = genomeName
        return super().get()

    @property
    def schema(self):
        return TrackSchema.get(self.genome, self.name)

    def getTrackData(self, genome, chrom=None, chromStart=None, chromEnd=None, hubUrl=None, maxItemsOutput=None,
                     download=False):

        self.requestUrl = BASE_URL + '/getData/track'

        params = {'genome': genome, 'track': self.name,
                  'maxItemsOutput': maxItemsOutput,
                  'chrom': chrom, 'chromStart': chromStart,
                  'chromEnd': chromEnd, 'hubUrl': hubUrl}

        response = requests.get(self.requestUrl, params).json()

        raiseExceptionOfRequest(response)

        chromList = []
        fragmentList = []

        if download:
            return response.get('dataDownloadUrl')

        if chrom is not None or hubUrl is not None:
            for key in response[self.name]:
                fragmentList.append(Fragment(**key))
            return fragmentList

        for key in response[self.name]:
            chromList.append(Chromosome(key))
            for chromosome in chromList:
                print(chromosome.name)
                for fragment in response[self.name][chromosome.name]:
                    fragmentList.append(Fragment(**fragment))
        return fragmentList

    def downloadData(self, genome, chrom=None, chromStart=None, chromEnd=None, hubUrl=None, maxItemsOutput=None,
                     filename=None):

        url = self.getTrackData(genome, chrom, chromStart, chromEnd, hubUrl, maxItemsOutput, download=True)

        filename = genome + '_' + self.name + '.zip' if filename is None else filename

        urllib.request.urlretrieve(url, filename)


class TrackSchema:
    def __init__(self, **kwargs):
        self.name = kwargs['name'],
        self.sqlType = kwargs['sqlType'],
        self.jsonType = kwargs['jsonType']
        self.description = kwargs['description']

    @staticmethod
    def get(genomeName, trackName):
        response = requests.get(BASE_URL + '/list/schema', {'genome': genomeName, 'track': trackName}).json()
        raiseExceptionOfRequest(response)
        schemaList = []

        for key in response['columnTypes']:
            schemaList.append(TrackSchema(**key))
        return schemaList


class Chromosome(Model):
    requestUrl = ''
    requestParams = {}
    responseKey = ''

    def __init__(self, name):
        self.name = name

    @classmethod
    def buildList(cls, response):
        myList = []
        for key in response[cls.responseKey]:
            myList.append(cls(key))
        return myList

    @classmethod
    def get(cls, hub=None, genome=None, track=None):
        cls.requestUrl = BASE_URL + '/list/chromosomes'
        cls.requestParams = {'genome': genome, 'track': track, 'hub': hub}
        cls.responseKey = 'chromosomes'
        response = requests.get(cls.requestUrl, cls.requestParams).json()
        raiseExceptionOfRequest(response)

        return super().get()

    @classmethod
    def exists(cls, name, hub=None, genome=None, track=None):
        return super().exists(name, hub, genome, track)

    @classmethod
    def find(cls, name, hub=None, genome=None, track=None):
        return super().find(name, hub, genome, track)


class Fragment:
    def __init__(self, **kwargs):
        self.chrom = kwargs.get('chrom')
        self.chromStart = kwargs.get('chromStart')
        self.chromEnd = kwargs.get('chromEnd')
        self.bin = kwargs.get('bin')
        self.ix = kwargs.get('ix')
        self.type = kwargs.get('type')
        self.frag = kwargs.get('frag')
        self.fragStart = kwargs.get('fragStart')
        self.fragEnd = kwargs.get('fragEnd')
        self.strand = kwargs.get('strand')


class Sequence:
    requestUrl = ''
    requestParams = {}
    responseKey = ''

    def __init__(self, genome, chrom, dna=None, hub=None, track=None, start=None, end=None,**kwargs):
        self.end = end
        self.start = start
        self.track = track
        self.hub = hub
        self.chrom = chrom
        self.dna = dna
        self.genome = genome

    @classmethod
    def get(cls, genome, chrom, hubUrl=None, start=None, end=None):
        cls.requestUrl = BASE_URL + '/getData/sequence'
        cls.requestParams = {'hubUrl': hubUrl, 'genome': genome, 'chrom': chrom, 'start': start, 'end': end}
        response = requests.get(cls.requestUrl, cls.requestParams).json()
        raiseExceptionOfRequest(response)
        return Sequence(**response)
