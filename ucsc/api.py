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
        if genome is None:
            Genome.createGenome(genomeName)
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
    def getUCSCGenomes():

        response = requests.get(BASE_URL + '/list/ucscGenomes').json()
        myList = []
        for key in response['ucscGenomes']:
            myList.append(Genome(key, **response['ucscGenomes'][key]))
        return myList

    @staticmethod
    def genomeExists(genomeName):
        for genome in Genome.getUCSCGenomes():
            if genome.genomeName == genomeName:
                return True

        return False

    @property
    def tracks(self):

        response = requests.get(BASE_URL + '/list/tracks',{'genome' : self.genomeName}).json()
        myList = []
        for key in response[self.genomeName]:

            myList.append(Track(key, **response[self.genomeName][key]))
        return myList


    @staticmethod
    def createGenome(genomeName):
        for genome in Genome.getUCSCGenomes():
            if genome.genomeName == genomeName:
                print('genome found')
                return genome
        raise Exception("can't construct genome, Genome does not exist")


class Track:  # mazen
    def __init__(self, trackName, shortLabel=None, type=None, longLabel=None, itemCount=None,
                 visibility=None, group=None,compositeContainer=None, subGroup1=None,compositeTrack=None,
                 priority=None, urlLabel=None, url=None, dbSnp153ViewVariants=None,dbSnp153ViewErrs=None,
                 indelDoubleInsert=None,pennantIcon=None,indelQueryInsert=None,baseColorUseSequence=None,
                 showCdsAllScales=None,showDiffBasesAllScales=None,color = None,showDiffBasesMaxZoom =None,
                 showCdsMaxZoom=None,baseColorDefault= None,baseColorUseCds=None,parent=None,html=None,noInherit=None,
                 bismapBigBed=None,bismapBigWig=None,maxWindowToDraw=None,superTrack=None,caddT=None,**kwargs):
        # fetch the track based on name
        # return the track as an object with all required attributes
        self.trackName = trackName
        self.caddT = caddT
        self.superTrack = superTrack
        self.maxWindowToDraw = maxWindowToDraw
        self.bismapBigWig = bismapBigWig
        self.bismapBigBed = bismapBigBed
        self.noInherit = noInherit
        self.html = html
        self.parent = parent
        self.baseColorUseCds = baseColorUseCds
        self.baseColorDefault = baseColorDefault
        self.showCdsMaxZoom = showCdsMaxZoom
        self.showDiffBasesMaxZoom = showDiffBasesMaxZoom
        self.color = color
        self.showDiffBasesAllScales = showDiffBasesAllScales
        self.showCdsAllScales = showCdsAllScales
        self.baseColorUseSequence = baseColorUseSequence
        self.indelQueryInsert = indelQueryInsert
        self.pennantIcon = pennantIcon
        self.indelDoubleInsert = indelDoubleInsert
        self.dbSnp153ViewErrs = dbSnp153ViewErrs
        self.dbSnp153ViewVariants = dbSnp153ViewVariants
        self.url = url
        self.urlLabel = urlLabel
        self.priority = priority
        self.compositeTrack = compositeTrack
        self.subGroup1 = subGroup1
        self.compositeContainer = compositeContainer
        self.group = group
        self.visibility = visibility
        self.itemCount = itemCount
        self.longLabel = longLabel
        self.type = type
        self.shortLabel = shortLabel

    def createShema(self, genome):
        # api.genome.ucsc.edu/list/schema?genome=hg38;track=knownGene
        return ''

    @staticmethod
    def constructTrack(trackName):
        for track in Genome.getUCSCGenomes():
            if track.trackName == trackName:
                print('track found')
                return track
        raise Exception("can't construct track, Genome does not exist")


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

# # returns list of available hubs names and url (can be overriding by parameter)
# hubList = Hub.getAllHubs()
#
# hubName = 'ALFA Hub'  # researcher will choose his desired hub based on short label
#
# hub = Hub(hubName)  # an object has every attribute of hub
#
# # get all genomes from specified hub object
# hub.getHubGenomes()
#
# # get all genomes from all UCSC Database
# genomesList = Genome.getUCSCGenomes()
#
# genomeName = 'CAST_EiJ'  # researcher will choose his desired genome based on name
#
# genome = Genome(genomeName)  # an object has every attribute of genome
#
# tracks = genome.trackList()
#
# trackName = 'affyGnf1h'
#
# track = Track(trackName)  # an object has every attribute of track
#
# # list chromosomes from specified track in UCSC database genome
#
# # list schema from specified track in UCSC database genome
# trackSchema = track.createShema(genome)
#
# # only one function to get the list of chromosomes
#
# # list chromosomes from UCSC database genome then hub and track = None
# chromosomes1 = Chromosome.getChromosomes(genome)
#
# # list chromosomes from specified track in UCSC database genome
# chromosomes2 = Chromosome.getChromosomes(genome, track=track)
#
# # list chromosomes from assembly hub genome
# chromosomes3 = Chromosome.getChromosomes(genome, hub)
#
# # list chromosomes from specified track in assembly hub genome
# chromosomes4 = Chromosome.getChromosomes(genome, hub, track)
#
# chromosome = Chromosome(genome)
#
# chromStart = 123
# chromEnd = 543
#
# sequence = Sequence(hub, genome, track, chromosome, chromStart, chromEnd)
#
# # sequence.dna
