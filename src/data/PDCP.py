from src.data.NrLayer import NrLayer


class PDCP(NrLayer):
    def __init__(self, file_path, delay=None):
        """
        Constructor of PDCP class. Receives the file path and sends it to the NrLayer (super class) constructor.
        """
        super().__init__(file_path, delay)
