from src.data.NrLayer import NrLayer


class RLC(NrLayer):
    def __init__(self, file_path):
        """
        Constructor of RLC class. Receives the file path and sends it to the NrLayer (super class) constructor.
        """
        super().__init__(file_path, 'dl')
