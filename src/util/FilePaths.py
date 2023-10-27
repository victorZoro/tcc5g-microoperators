import git
from pathlib import Path
import os

from src.exceptions.EmptyValueError import EmptyValueError


class FilePaths:
    _instance = None

    def __init__(self):
        self.root = self.get_project_root()

        self.directory_tests = self.root / 'sim_tests'
        self.directory_results = self.root / 'results'

        self.directory_ue30 = self.directory_results / 'UDP-30-UE'
        self.directory_ue60 = self.directory_results / 'UDP-60-UE'
        self.directory_ue90 = self.directory_results / 'UDP-90-UE'
        self.directory_ue120 = self.directory_results / 'UDP-120-UE'

        self.directory_tcp_tdd = self.root / 'sim_tests' / 'testes' / 'TCP-5S TDD'
        self.directory_udp_tdd = self.root / 'sim_tests' / 'testes' / 'UDP-5S TDD'

        self.directory_dataset = self.directory_results / 'DATASET-BY-SOUSA'

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = FilePaths()
        return cls._instance

    def get_project_root(self):
        return Path(git.Repo('.', search_parent_directories=True).working_tree_dir)

    def search_file(self, file_name, extension, search_path=None):
        """
        Searches for a file in the dict of file paths.

        Args:
            file_name (str): Name of the file.
            extension (str): Extension of the file.
            search_path (str): Path to search for the file.

        Returns:
            str: File path.
        """

        if search_path is None or not search_path:
            search_path = self.root

        for root, dir, files in os.walk(search_path):
            for file in files:
                if file == file_name + '.' + extension:
                    return os.path.join(root, file)

    def get_file_names(self):
        return [
            'RxPacketTrace',
            'NrDlPdcpRxStats',
            'NrDlRxRlcStats',
            'flowmonitor',
        ]

    def load_files(self, search_path, file_extension='txt'):
        try:
            EmptyValueError.check_for_empty_value([file_extension])
        except EmptyValueError as e:
            print(e)
            return

        file_names = self.get_file_names()
        files = {}

        for file in file_names:
            files.update({file: self.search_file(file, file_extension, search_path)})
            print('Successful loading for file:', search_path, file)

        return files
