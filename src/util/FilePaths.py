import git
from pathlib import Path
import os
import types

from argon2._utils import NoneType

"""
Class that contains all the file paths for the project.

Follows the Singleton pattern.
"""


class FilePaths:
    _instance = None

    def __init__(self):
        """
        Constructor of FilePaths class. Initializes the dict of file paths and adds the files to the dict.

        The keys are the filename while the values are the file paths.
        """

        self.root = self.get_project_root()

        self._files = {}
        # self.sim_tests = self.root / 'sim_tests'
        # self.teste_NGMN = self.sim_tests / 'teste_NGMN'
        # self.ctrl = self.teste_NGMN / 'CTRL'
        # self.data = self.teste_NGMN / 'DATA'
        # self.others = self.teste_NGMN / 'OTHERS'
        # self.pdcp = self.teste_NGMN / 'PDCP'
        # self.rlc = self.teste_NGMN / 'RLC'
        #
        # self._files = {
        #     'DlCtrlSinr': self.ctrl / 'DlCtrlSinr.txt',
        #     'DlDataSinr': self.data / 'DlDataSinr.txt',
        #     'RxPacketTrace': self.others / 'RxPacketTrace.txt',
        #     'DlPathlossTrace': self.others / 'DlPathlossTrace.txt',
        #     'UlPathlossTrace': self.others / 'UlPathlossTrace.txt',
        #     'NrDlPdcpRxStats': self.pdcp / 'NrDlPdcpRxStats.txt',
        #     'NrDlPdcpTxStats': self.pdcp / 'NrDlPdcpTxStats.txt',
        #     'NrUlPdcpTxStats': self.pdcp / 'NrUlPdcpTxStats.txt',
        #     'NrDlPdcpStatsE2E': self.pdcp / 'NrDlPdcpStatsE2E.txt',
        #     'NrUlPdcpStatsE2E': self.pdcp / 'NrUlPdcpStatsE2E.txt',
        #     'NrDlRxRlcStats': self.rlc / 'NrDlRxRlcStats.txt',
        #     'NrDlTxRlcStats': self.rlc / 'NrDlTxRlcStats.txt',
        #     'NrDlRlcStatsE2E': self.rlc / 'NrDlRlcStatsE2E.txt',
        #     'NrUlRlcStatsE2E': self.rlc / 'NrUlRlcStatsE2E.txt'
        # }

    def add_file(self, file):
        """
        Updates the dict of file paths.

        Args:
            files (dict): Dict of file paths.
        """
        if not isinstance(file, dict):
            raise TypeError('File must be a dict.')

        self._files.update(file)

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
        if not isinstance(file_name, str) or not isinstance(extension, str):
            bad_argument = file_name if not isinstance(file_name, str) else extension
            raise TypeError('Argument', bad_argument, 'cannot be a', type(bad_argument), '. Must be a str.')
        if not isinstance(search_path, (str, type(None))):
            raise TypeError('Argument search_path cannot be a', type(search_path), '. Must be a str or None.')
        if not file_name or not extension:
            raise ValueError('Arguments cannot be empty.')

        if search_path is None or not search_path:
            search_path = self.root

        for root, dir, files in os.walk(search_path):
            for file in files:
                if file == file_name + '.' + extension:
                    return os.path.join(root, file)

    def get_project_root(self):
        return Path(git.Repo('.', search_parent_directories=True).working_tree_dir)

    @property
    def files(self):
        """
        Getter for the dict of file paths.
        """
        return self._files

    @classmethod
    def instance(cls):
        """
        Singleton method that returns the instance of the class.
        """
        if cls._instance is None:
            cls._instance = FilePaths()
        return cls._instance
