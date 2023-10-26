from src.data.Ctrl import Ctrl
from src.data.Data import Data
from src.data.RxPacketTrace import RxPacketTrace
from src.data.Pathloss import Pathloss
from src.data.PDCP import PDCP
from src.data.RLC import RLC


class DataAccess:
    def __init__(self, files):
        """
        Constructor for DataAcess class.

        Args:
            files (list): directories for the files.
        """
        self.UEs = None

        self.ctrl = Ctrl(files['DlCtrlSinr'])

        self.data = Data(files['DlDataSinr'])
        self.rxPacketTrace = RxPacketTrace(files['RxPacketTrace'])

        # Reminder: These are dicts.
        self.pdcp = {
            'NrDlPdcpRxStats': PDCP(files['NrDlPdcpRxStats'], 'delay(s)'),
            'NrDlPdcpTxStats': PDCP(files['NrDlPdcpTxStats']),
            'NrUlPdcpTxStats': PDCP(files['NrUlPdcpTxStats']),
        }
        self.rlc = {
            'NrDlRxRlcStats': RLC(files['NrDlRxRlcStats'], 'delay(s)'),
            'NrDlTxRlcStats': RLC(files['NrDlTxRlcStats']),
        }
        self.pathLoss = {
            'DlPathlossTrace': Pathloss(files['DlPathlossTrace']),
        }

        # self.dataset = None

        print('[Dataset] [All files were loaded successfully]')

    @staticmethod
    def get_avg_by_second(data, time):
        """
        Gets the average of the data by second.

        Args:
            data (list / pandas.Series): list of data.
            time (list / pandas.Series): list of timestamps.

        Returns:
            list: list of averages per second.
        """
        time_stamps = DataAccess.get_time_stamps(time)
        average = []
        sum = 0

        for index, (previous_time, current_time, value) in enumerate(zip(time_stamps, time_stamps[1:], data)):
            sum += value
            if previous_time != current_time:
                average.append(sum / (index + 1))
                sum = 0

        return average

    @staticmethod
    def get_time_stamps(time):
        """
        Gets the timestamps in seconds only.

        Args:
            time (list): list of timestamps.

        Returns:
            list (int): list of timestamps in seconds.
        """
        return list(set(time.astype(int)))

    @staticmethod
    def get_throughput(data, time):
        """
        Gets the throughput in MBps.
        
        Necessary because the throughput has a formula to be calculated. 

        Args:
            data (list): list of data.
            time (list): list of timestamps.

        Returns:
            list: list of throughput per second.
        """
        time_stamps = DataAccess.get_time_stamps(time)
        throughput = []
        sum = 0

        for index, (previous_time, current_time, value) in enumerate(zip(time_stamps, time_stamps[1:], data)):
            sum += data[index]
            if previous_time != current_time:
                throughput.append(8 * (sum / current_time) * (1024 ** 2) / 1e6)
                sum = 0

        return throughput