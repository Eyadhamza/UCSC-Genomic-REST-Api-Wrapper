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


class Hub:
    request = BASE_URL + '/list/publicHubs'
    key = 'publicHubs'

    def __init__(self, **kwargs):
        self.name = kwargs.get('shortLabel')
        self.hubUrl = kwargs.get('hubUrl')
        self.longLabel = kwargs.get('longLabel')
        self.registrationTime = kwargs.get('registrationTime')
        self.dbCount = kwargs.get('dbCount')
        self.dbList = kwargs.get('dbList')
        self.descriptionUrl = kwargs.get('descriptionUrl')

    @staticmethod
    def get():
        response = requests.get(Hub.request).json()
        raiseExceptionOfRequest(response)
        myList = []
        for key in response[Hub.key]:
            myList.append(Hub(**key))
        return myList

    @staticmethod
    def find(hubName):
        for hub in Hub.get():
            if hub.name == hubName:
                print('hub found')
                return hub
        raise Exception("can't find hub, Hub does not exist")

    @staticmethod
    def findBy(hubAttribute, value):
        for hub in Hub.get():
            if getattr(hub, hubAttribute) == value:
                print('hub found')
                return hub
        raise Exception("can't find hub, Hub does not exist")

    @property
    def genomes(self):
        return Genome.get(self.hubUrl)


class Genome:
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
        URL = 'ucscGenomes' if hubUrl is None else 'hubGenomes'

        response = requests.get(BASE_URL + f'/list/{URL}', {'hubUrl': hubUrl}).json()
        raiseExceptionOfRequest(response)

        genomesList = []
        genomesResponse = 'ucscGenomes' if hubUrl is None else 'genomes'

        for key in response[genomesResponse]:
            genomesList.append(Genome(key, **response[genomesResponse][key]))
        return genomesList

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

    def findTrackBy(self, attributeName, trackName):
        return Track.findBy(self.genomeName, attributeName, trackName)

    def isTrackExists(self, trackName):
        return Track.exists(self.genomeName, trackName)

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


# Genome.findBy('genomeName','PWK_PhJ')

class Track:
    def __init__(self, trackName, **kwargs):
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

        raiseExceptionOfRequest(response)
        trackList = []
        for key in response[genomeName]:
            trackList.append(Track(key, **response[genomeName][key]))
        return trackList

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
        raise Exception("can't find track, Track does not exist")

    def schema(self, genomeName):
        return TrackSchema.get(genomeName, self.trackName)

    def trackData(self, genome, chrom=None, chromStart=None, chromEnd=None, hubUrl=None, maxItemsOutput=None,
                  download=False):
        URL = BASE_URL + '/getData/track'

        params = {'genome': genome, 'track': self.trackName,
                  'maxItemsOutput': maxItemsOutput,
                  'chrom': chrom, 'chromStart': chromStart,
                  'chromEnd': chromEnd, 'hubUrl': hubUrl}

        response = requests.get(URL, params).json()

        raiseExceptionOfRequest(response)

        chromList = []
        fragmentList = []

        if download:
            return response.get('dataDownloadUrl')

        if chrom is not None or hubUrl is not None:
            for key in response[self.trackName]:
                fragmentList.append(Fragment(**key))
            return fragmentList

        for key in response[self.trackName]:
            chromList.append(Chromosome(key))
            for chromosome in chromList:
                print(chromosome.chromosomeName)
                for fragment in response[self.trackName][chromosome.chromosomeName]:
                    fragmentList.append(Fragment(**fragment))
        return fragmentList

    def downloadData(self, genome, chrom=None, chromStart=None, chromEnd=None, hubUrl=None, maxItemsOutput=None,
                     filename=None):

        url = self.trackData(genome, chrom, chromStart, chromEnd, hubUrl, maxItemsOutput, download=True)

        filename = genome + '_' + self.trackName + '.zip' if filename is None else filename

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


class Chromosome:
    def __init__(self, chromosomeName):
        self.chromosomeName = chromosomeName

    @staticmethod
    def get(hub=None, genome=None, track=None):
        URL = BASE_URL + '/list/chromosomes'
        response = requests.get(URL, {'genome': genome, 'track': track, 'hub': hub}).json()
        
        raiseExceptionOfRequest(response)
        chromosomesList = []
        
        for key in response['chromosomes']:
            chromosomesList.append(Chromosome(key))
        return chromosomesList

    @staticmethod
    def exists(chromosomeName, hub=None, genome=None, track=None):
        for chromosome in Chromosome.get(hub, genome, track):
            if chromosome.chromosomeName == chromosomeName:
                return True

        return False

    @staticmethod
    def find(chromosomeName, hub=None, genome=None, track=None):
        for chromosome in Chromosome.get(hub, genome, track):
            if chromosome.chromosomeName == chromosomeName:
                return chromosome

        raise Exception("can't find chromosome, Chromosome does not exist")


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
    def __init__(self, genome, chrom, dna=None, hub=None, track=None, start=None, end=None,**kwargs):
        self.end = end
        self.start = start
        self.track = track
        self.hub = hub
        self.chrom = chrom
        self.dna = dna
        self.genome = genome

    @staticmethod
    def get(genome, chrom, hubUrl=None, start=None, end=None):
        URL = BASE_URL + '/getData/sequence'
        params = {'hubUrl': hubUrl, 'genome': genome, 'chrom': chrom, 'start': start, 'end': end}
        response = requests.get(URL, params).json()
        raiseExceptionOfRequest(response)
        return Sequence(**response)
