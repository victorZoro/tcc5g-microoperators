import pandas as pd
from src.exceptions.EmptyValueError import EmptyValueError
from src.util.FilePaths import FilePaths


class Dataset:
    def __init__(self, UEs=None, attackers=None):
        self.file_paths = FilePaths.instance()

        self.UEs = UEs
        self.attackers = attackers

        self.dataset = None

        self.find_files()

        self.rename_time()
        self.rename_packet_size()

    def find_files(self):
        if not (self.attackers, self.UEs):
            raise EmptyValueError('At least one value needs to be specified.')
        if self.attackers and self.UEs:
            raise ValueError('Only one value can be specified.')

        if self.attackers:
            attackers = str(self.attackers) + '.csv'
            self.dataset = pd.read_csv(
                self.file_paths.directory_dataset / attackers,
                sep=',',
                decimal='.',
                engine='python'
            )
            return

        if self.UEs == 9:
            files = self.file_paths.load_files(self.file_paths.directory_udp_tdd)
        elif self.UEs == 10:
            files = self.file_paths.load_files(self.file_paths.directory_tcp_tdd)
        elif self.UEs == 30:
            files = self.file_paths.load_files(self.file_paths.directory_ue30)
        elif self.UEs == 60:
            files = self.file_paths.load_files(self.file_paths.directory_ue60)
        elif self.UEs == 90:
            files = self.file_paths.load_files(self.file_paths.directory_ue90)
        elif self.UEs == 120:
            files = self.file_paths.load_files(self.file_paths.directory_ue120)
        else:
            raise ValueError('Invalid number of UEs.')

        self.dataset = {
            'rxPacketTrace': pd.read_csv(files['RxPacketTrace'],
                                         sep='\\t', decimal='.', engine='python'),

            'pdcp': pd.read_csv(files['NrDlPdcpRxStats'],
                                sep='\\t', decimal='.', engine='python'),

            'rlc': pd.read_csv(files['NrDlRxRlcStats'],
                               sep='\\t', decimal='.', engine='python'),
        }

    def rename_time(self):
        if self.UEs:
            for key in self.dataset:
                if 'time(s)' in self.dataset[key].columns:
                    self.dataset[key].rename(columns={'time(s)': 'time'}, inplace=True)
                if 'Time' in self.dataset[key].columns:
                    self.dataset[key].rename(columns={'Time': 'time'}, inplace=True)
            return

        if 'timeSec' in self.dataset.columns:
            self.dataset.rename(columns={'timeSec': 'time'}, inplace=True)

    def rename_packet_size(self):
        if self.UEs:
            for key in self.dataset:
                if 'tbSize' in self.dataset[key].columns:
                    self.dataset[key].rename(columns={'tbSize': 'packetSize'}, inplace=True)
                    return

        if 'pktSizeBytes' in self.dataset.columns:
            self.dataset.rename(columns={'pktSizeBytes': 'packetSize'}, inplace=True)
