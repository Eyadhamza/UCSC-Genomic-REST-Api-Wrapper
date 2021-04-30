class Hub:
    def __init__(self,hubName):
        self.hubUrl = None
        self.hubName = hubName

    @staticmethod
    def getAllHubs():
        return []

    def getHubData(self):
        hubUrl = self.hubUrl
        # call to api.genome.ucsc.edu/list/hubGenomes?hubUrl=http://hgdownload.soe.ucsc.edu/hubs/mouseStrains/hub.txt
        pass


# returns list of available hubs names and url (can be overriding by parameter)
hubList = Hub.getAllHubs()

hubName = 'ALFA Hub' # programmer will choose his desired hub based on short label


hub = Hub(hubName) # an object has every attribute of hub


# get all genomes from specified hub object
hub.getHubData()
