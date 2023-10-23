
from src.data.Dataset import Dataset


class SINR(Dataset):
    def __init__(self, file_path):

        """
        Constructor of SINR class. Receives the file path and sends it to the Dataset (super class) constructor.

        The link type is downlink for every file that has SINR.
        """

        super().__init__(file_path)
        self.SINR = self.dataset['SINR(dB)']
