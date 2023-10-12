from Dataset import Dataset


class SINR(Dataset):
    def __init__(self, filePath):

        '''
        Constructor of SINR class. Receives the file path and sends it to the Dataset (super class) constructor.

        The link type is downlink for every file that has SINR.
        '''

        self.filePath = filePath
        super().__init__(filePath, 'dl')
