import pandas as pd
import xml.etree.ElementTree as et

from src.exceptions.EmptyValueError import EmptyValueError
from src.processors.DataProcessor import DataProcessor
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
        if self.attackers and self.UEs:
            raise ValueError('Only one value can be specified.')

        if self.attackers:
            self.find_attacker_files()
            return
        else:
            ue_directories = {
                9: self.file_paths.directory_udp_tdd,
                10: self.file_paths.directory_tcp_tdd,
                30: self.file_paths.directory_ue30,
                60: self.file_paths.directory_ue60,
                90: self.file_paths.directory_ue90,
                120: self.file_paths.directory_ue120
            }
            self.find_ue_files(ue_directories)
            self.find_xml_files(ue_directories)
            return

    def find_attacker_files(self):
        attackers = str(self.attackers) + '.csv'
        self.dataset = pd.read_csv(
            self.file_paths.directory_dataset / attackers,
            sep=',',
            decimal='.',
            engine='python'
        )

    def find_ue_files(self, ue_directories):
        try:
            EmptyValueError.check_for_empty_value(ue_directories)
        except EmptyValueError as e:
            print('ue_directories', e)
            return

        if self.UEs in ue_directories:
            files = self.file_paths.load_files(ue_directories[self.UEs])
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

    def find_xml_files(self, ue_directories):
        try:
            EmptyValueError.check_for_empty_value(ue_directories)
        except EmptyValueError as e:
            print('ue_directories', e)
            return

        if self.UEs in ue_directories:
            files = self.file_paths.load_files(ue_directories[self.UEs], 'xml')
        else:
            raise ValueError('Invalid number of UEs.')

        try:
            etree = et.parse(files['flowmonitor'])
        except TypeError:
            print('flowmonitor.xml is not available. Please review the simulation results.')
            return

        root = etree.getroot()

        self.dataset.update({'flowMonitor': pd.DataFrame(DataProcessor.get_transformed_xml(root))})

        pass

    def rename_time(self):

        if isinstance(self.dataset, dict):
            for key in self.dataset:
                if 'time(s)' in self.dataset[key].columns:
                    self.dataset[key].rename(columns={'time(s)': 'time'}, inplace=True)
                elif 'Time' in self.dataset[key].columns:
                    self.dataset[key].rename(columns={'Time': 'time'}, inplace=True)
            return

        if 'timeSec' in self.dataset.columns:
            self.dataset.rename(columns={'timeSec': 'time'}, inplace=True)

    def rename_packet_size(self):
        if isinstance(self.dataset, dict):
            for key in self.dataset:
                if 'tbSize' in self.dataset[key].columns:
                    self.dataset[key].rename(columns={'tbSize': 'packetSize'}, inplace=True)
                    return

        if 'pktSizeBytes' in self.dataset.columns:
            self.dataset.rename(columns={'pktSizeBytes': 'packetSize'}, inplace=True)
