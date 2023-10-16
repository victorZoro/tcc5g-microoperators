from src.data.SINR import SINR


class RxPacketTrace(SINR):
    def __init__(self, file_path):
        """
        Constructor of the RxPacketTrace class. Receives the file path and sends it to the SINR (super class) constructor.

        Args:
            file_path (str): Path of the file.

        Also initializes the direction, CQI and corrupt attributes, which can be found in the simulation result file RxPacketTrace.
        """
        super().__init__(file_path)
        self.direction = self.dataset['direction']
        self.CQI = self.dataset['CQI']
        self.corrupt = self.dataset['corrupt']
        self.time = self.dataset['Time']
