from src.data.SINR import SINR

'''
Disclaimer: The Data class represents the DlDataSinr file from the simulation results.
'''


class Data(SINR):
    def __init__(self, file_path):
        """
        Constructor of Data class. Receives the file path and sends it to the SINR (super class) constructor.

        Args:
            file_path (str): Path of the file.
        """
        super().__init__(file_path)
