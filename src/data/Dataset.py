import pandas as pd

class Dataset:
    def __init__(self, filePath, linkType):

        '''
        Constructor of Dataset class. Receives the file path and the link type (ul or dl).

        Args:
            filePath (str): Path of the file.
            linkType (str): Link type (ul or dl).
        '''

        self.filePath = filePath
        self.dataset = pd.read_csv(filePath)
        self.linkType = linkType
