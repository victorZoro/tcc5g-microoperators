import pandas as pd


class Dataset:
    def __init__(self, file_path):
        """
        Constructor of Dataset class. Receives the file path and the link type (ul or dl).

        Args:
            file_path (str): Path of the file.
        """

        self.file_path = file_path
        self.dataset = pd.read_csv(file_path, sep='\\t', engine='python')
        self.time = None
