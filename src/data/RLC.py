from NrLayer import NrLayer

class RLC(NrLayer):
    def __init__(self, filePath):
        '''
        Constructor of RLC class. Receives the file path and sends it to the NrLayer (super class) constructor.
        '''
        super().__init__(filePath, 'dl')
