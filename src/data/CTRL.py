from SINR import SINR

class CTRL(SINR):
    def __init__(self, filePath):
        '''
        Constructor of CTRL class. Receives the file path and sends it to the SINR (super class) constructor.

        Args:
            filePath (str): Path of the file.
        '''
        super().__init__(filePath)
