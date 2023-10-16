from src.data.Dataset import Dataset


class NrLayer(Dataset):
    def __init__(self, file_path, delay=None):
        """
        Constructor of NrLayer class. Receives the file path and sends it to the E2EBytes (super class) constructor.

        Args:
            file_path (str): Path of the file.

        Also initializes the packetSize and delay attributes, which can be found in many simulation result files.

        Check the table under the README.md file for more information.
        """
        super().__init__(file_path)
        self.packetSize = self.dataset['packetSize']
        self.time = self.dataset['time(s)']
        if delay:
            self.delay = self.dataset[delay]
