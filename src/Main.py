import os

from src.util.DataAccess import DataAccess
from src.util.FilePaths import FilePaths
from src.util.Plotter import Plotter


class Main:
    def __init__(self):
        self.file_paths = FilePaths.instance()
        self.plotter = Plotter.instance()

        # 5G-LENA Results by students
        self.ln_results_ue30 = DataAccess(self.file_paths.load_files(self.file_paths.directory_ue30))
        # self.ln_results_ue60 = DataAccess(self.file_paths.load_files(self.file_paths.directory_ue60))
        # self.ln_results_ue90 = DataAccess(self.file_paths.load_files(self.file_paths.directory_ue90))
        # self.ln_results_ue120 = DataAccess(self.file_paths.load_files(self.file_paths.directory_ue120))

        # Dataset by SOUSA et. al. (2023)
        # self.ds_results_attacker2 = None
        # self.ds_results_attacker4 = None
        # self.ds_results_attacker7 = None
        # self.ds_results_attacker9 = None

    def main(self):
        pass

    @staticmethod
    def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    main = Main()
    main.main()
