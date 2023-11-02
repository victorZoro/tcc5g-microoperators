import pandas as pd
import xml.etree.ElementTree as et

from src.exceptions.EmptyValueError import EmptyValueError
from src.processors.DataProcessor import DataProcessor
from src.util.FilePaths import FilePaths


class Dataset:
    def __init__(self, UEs=None, attackers=None, protocol=None):
        self.file_paths = FilePaths.instance()

        self.UEs = UEs
        self.attackers = attackers
        self.protocol = protocol

        if self.UEs and not self.protocol:
            raise ValueError('Protocol must be specified.')

        if self.attackers and self.UEs:
            raise ValueError('Only one value can be specified.')

        self.dataset = None

        self.find_files()

        self.rename_time()
        self.rename_delay()
        self.rename_packet_size()

    def find_files(self):
        if self.attackers:
            self.find_attacker_files()
            return
        else:
            protocol_directory = self.file_paths.results_tcp if self.protocol == 'TCP' \
                else self.file_paths.results_udp

            ue_directories = {
                30: protocol_directory / self.file_paths.directory_ue30,
                60: protocol_directory / self.file_paths.directory_ue60,
                90: protocol_directory / self.file_paths.directory_ue90,
                120: protocol_directory / self.file_paths.directory_ue120
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

            'rx_pdcp': pd.read_csv(files['NrDlPdcpRxStats'],
                                   sep='\\t', decimal='.', engine='python'),

            'tx_pdcp': pd.read_csv(files['NrDlPdcpTxStats'],
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
            print('XML file not found. Please check simulation results')
            return

        root = etree.getroot()

        self.dataset.update({'flowMonitor': pd.DataFrame(DataProcessor.get_transformed_xml(root))})

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

    def rename_delay(self):
        if isinstance(self.dataset, dict):
            for key in self.dataset:
                if 'delay(s)' in self.dataset[key].columns:
                    self.dataset[key].rename(columns={'delay(s)': 'delay'}, inplace=True)
            return
