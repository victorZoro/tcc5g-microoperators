from Dataset import Dataset

class Pathloss:
    def __init__(self, filePath, linkType):
        '''
        Constructor of the Pathloss class. Receives the file path and the link type (ul or dl).

        Args:
            filePath (str): Path of the file.
            linkType (str): Link type (ul or dl).

        Also initializes the pathLoss attribute, which can be found in the simulation result files UlPathlossTrace and DlPathlossTrace.
        '''
        super.__init__(self, filePath, linkType)
        self.pathLoss = self.dataset['pathLoss']
