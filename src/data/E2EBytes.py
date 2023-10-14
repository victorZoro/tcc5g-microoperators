from src.data.Dataset import Dataset


class E2EBytes(Dataset):
    def __init__(self, file_path):
        """
        Constructor of the E2EBytes class. Receives the file path and the link type (ul or dl).

        Args:
            file_path (str): Path of the file.

        Also initializes the txBytes and rxBytes attributes, which are both None by default for simplification purposes.
        """
        super().__init__(file_path)
        self.tx_bytes = None
        self.rx_bytes = None

    @property
    def tx_bytes(self):
        """
        Getter of the tx_bytes attribute.
        """
        return self._tx_bytes

    @tx_bytes.setter
    def tx_bytes(self, tx_bytes):
        """
        Setter of the tx_bytes attribute.

        Args:
            tx_bytes (int): Number of bytes transmitted.
        """
        self._tx_bytes = tx_bytes

    @property
    def rx_bytes(self):
        """
        Getter of the rx_bytes attribute.
        """
        return self._rx_bytes

    @rx_bytes.setter
    def rx_bytes(self, rx_bytes):
        """
        Setter of the rx_bytes attribute.

        Args:
            rx_bytes (int): Number of bytes received.
        """
        self._rx_bytes = rx_bytes
