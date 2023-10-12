from Dataset import Dataset

class E2EBytes:
    def __init__(self, filePath, linkType):
        '''
        Constructor of the E2EBytes class. Receives the file path and the link type (ul or dl).

        Args:
            filePath (str): Path of the file.
            linkType (str): Link type (ul or dl).

        Also initializes the txBytes and rxBytes attributes, which are both None by default for simplification purposes.
        '''
        super.__init__(self, filePath, linkType)
        self.txBytes = None
        self.rxBytes = None

    @txBytes.setter
    def txBytes(self, txBytes):
        '''
        Setter of the txBytes attribute.

        Args:
            txBytes (int): Number of bytes transmitted.
        '''
        self.txBytes = txBytes

    @rxBytes.setter
    def rxBytes(self, rxBytes):
        '''
        Setter of the rxBytes attribute.

        Args:
            rxBytes (int): Number of bytes received.
        '''
        self.rxBytes = rxBytes
