from SINR import SINR

'''
Disclaimer: The Data class represents the DlDataSinr file from the simulation results.
'''

class Data(SINR):
    def __init__(self, filePath):
        '''
        Constructor of Data class. Receives the file path and sends it to the SINR (super class) constructor.

        Args:
            filePath (str): Path of the file.
        '''
        super().__init__(filePath)
