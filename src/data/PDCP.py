from NrLayer import NrLayer

class PDCP(NrLayer):
    def __init__(self, filePath, linkType):
        '''
        Constructor of PDCP class. Receives the file path and sends it to the NrLayer (super class) constructor.
        '''
        super().__init__(filePath, linkType)