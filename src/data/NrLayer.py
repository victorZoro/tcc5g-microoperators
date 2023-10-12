from E2EBytes import E2EBytes

class NrLayer(E2EBytes):
    def __init__(self, filePath, linkType):
        '''
        Constructor of NrLayer class. Receives the file path and sends it to the E2EBytes (super class) constructor.

        Args:
            filePath (str): Path of the file.
            linkType (str): Link type of the file.

        Also initializes the packetSize and delay attributes, which can be found in many simulation result files.

        Check the table under the README.md file for more information.
        '''
        super().__init__(filePath, linkType)
        self.packetSize = self.Dataset.dataset['packetSize']
        self.delay = self.Dataset.dataset['delay']
