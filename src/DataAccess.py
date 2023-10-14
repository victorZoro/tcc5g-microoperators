from src.data import Ctrl
from src.data import Data
from src.data import RxPacketTrace
from src.data import Pathloss


# from util import FilePaths as fp

class DataAccess:
    def __init__(self, files):
        self.ctrl = Ctrl.Ctrl(files['DlCtrlSinr'])

        # self.data = Data.Data(files['DlDataSinr'])
        # self.rxPacketTrace = RxPacketTrace.RxPacketTrace(files['RxPacketTrace'])
        #
        # # Reminder: These are dicts.
        # self.pdcp = {}
        # self.rlc = {}
        # self.pathLoss = {
        #     'ul': Pathloss.Pathloss(files['DlPathlossTrace'], 'ul'),
        #     'dl': Pathloss.Pathloss(files['UlPathlossTrace'], 'dl')
        # }
        #
        # self._import_all_pdcp()
        # self._import_all_rlc()

    def _import_all_pdcp(self):
        # TODO: Implement
        pass

    def _import_all_rlc(self):
        # TODO: Implement
        pass
