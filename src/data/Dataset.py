import pandas as pd


class Dataset:
    def __init__(self, file_path, link_type):
        """
        Constructor of Dataset class. Receives the file path and the link type (ul or dl).

        Args:
            file_path (str): Path of the file.
            link_type (str): Link type (ul or dl).
        """

        self.filePath = file_path
        self.dataset = pd.read_csv(file_path, sep='\\t', engine='python')
        self.link_type = link_type
