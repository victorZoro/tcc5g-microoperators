from data import *
# from util import FilePaths as fp

class DataAccess:
    def __init__(self, files):
        self.ctrl = Ctrl(files['ctrl'])
        self.data = Data(files['data'])
        self.rxPacketTrace = RxPacketTrace(files['rxPacketTrace'])

        # Reminder: These are dicts.
        self.pdcp = None
        self.rlc = None
        self.pathLoss = {
            'ul': PathLoss(files['ulPathLoss'], 'ul'),
            'dl': PathLoss(files['dlPathLoss'], 'dl')
        }
