from src.data.Ctrl import Ctrl
from src.data.Data import Data
from src.data.RxPacketTrace import RxPacketTrace
from src.data.Pathloss import Pathloss
from src.data.PDCP import PDCP
from src.data.RLC import RLC


class DataAccess:
    def __init__(self, files):
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

        self.dataset = None

        print('[Dataset] [All files were loaded successfully]')

    def get_overall_avg(self, data):
        sum = 0
        for value in data:
            sum += value

        return sum / len(data)

    def get_avg_by_second(self, data, time):
        time_stamps = self.get_time_stamps(time)
        average = []
        sum = 0

        for index, (previous_time, current_time, value) in enumerate(zip(time_stamps, time_stamps[1:], data)):
            sum += value
            if previous_time != current_time:
                average.append(sum / (index + 1))
                sum = 0

        return average

    def get_time_stamps(self, time):
        return list(set(time.astype(int)))

    def get_throughput(self, data):
        pass
