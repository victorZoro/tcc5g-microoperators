from SINR import SINR

class RxPacketTrace:
    def __init__(self, filePath):
        '''
        Constructor of the RxPacketTrace class. Receives the file path and sends it to the SINR (super class) constructor.

        Args:
            filePath (str): Path of the file.

        Also initializes the direction, CQI and corrupt attributes, which can be found in the simulation result file RxPacketTrace.
        '''
        super.__init__(filePath, None)
        self.direction = self.dataset['direction']
        self.CQI = self.dataset['CQI']
        self.corrupt = self.dataset['corrupt']