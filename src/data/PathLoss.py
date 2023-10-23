from src.data.Dataset import Dataset


class Pathloss(Dataset):
    def __init__(self, file_path):
        """
        Constructor of the Pathloss class. Receives the file path and the link type (ul or dl).

        Args:
            file_path (str): Path of the file.

        Also initializes the pathLoss attribute, which can be found in the simulation result files UlPathlossTrace
        and DlPathlossTrace.
        """
        super().__init__(file_path)
        self.pathLoss = self.dataset['pathLoss(dB)']
