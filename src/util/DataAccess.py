from src.data import Ctrl
from src.data import Data
from src.data import RxPacketTrace
from src.data import Pathloss
from src.data import PDCP
from src.data import RLC


# from util import FilePaths as fp

class DataAccess:
    def __init__(self, files):
        self.ctrl = Ctrl.Ctrl(files['DlCtrlSinr'])

        self.data = Data.Data(files['DlDataSinr'])
        self.rxPacketTrace = RxPacketTrace.RxPacketTrace(files['RxPacketTrace'])

        # Reminder: These are dicts.
        self.pdcp = {
            'NrDlPdcpRxStats': PDCP.PDCP(files['NrDlPdcpRxStats'], 'delay(s)'),
            'NrDlPdcpTxStats': PDCP.PDCP(files['NrDlPdcpTxStats']),
            'NrUlPdcpTxStats': PDCP.PDCP(files['NrUlPdcpTxStats']),
        }
        self.rlc = {
            'NrDlRxRlcStats': RLC.RLC(files['NrDlRxRlcStats'], 'delay(s)'),
            'NrDlTxRlcStats': RLC.RLC(files['NrDlTxRlcStats']),
        }
        self.pathLoss = {
            'DlPathlossTrace': Pathloss.Pathloss(files['DlPathlossTrace']),
        }
