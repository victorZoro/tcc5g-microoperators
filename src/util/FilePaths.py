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

        self.load_files()

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

    def get_file_names(self):
        return [
            'DlCtrlSinr',
            'DlDataSinr',
            'RxPacketTrace',
            'DlPathlossTrace',
            'UlPathlossTrace'
            'RxPacketTrace',
            'NrDlPdcpRxStats',
            'NrDlPdcpTxStats',
            'NrUlPdcpTxStats',
            'NrDlRxRlcStats',
            'NrDlTxRlcStats',
        ]

    def load_files(self):
        file_names = self.get_file_names()

        for file in file_names:
            self.add_file({file: self.search_file(file, 'txt')})
            print('Successful loading for file:', file)

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
