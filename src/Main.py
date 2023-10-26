import os
from src.util.DataAccess import DataAccess
from src.util.FilePaths import FilePaths
from src.util.Plotter import Plotter


class Main:
    def __init__(self):
        self.file_paths = FilePaths.instance()
        self.plotter = Plotter.instance()

        # self.data_access = DataAccess(self.file_paths.load_files(self.file_paths.directory_tests))

        # 5G-LENA Results by students
        self.ln_results_ue30 = DataAccess(self.file_paths.load_files(self.file_paths.directory_ue30))
        self.ln_results_ue60 = DataAccess(self.file_paths.load_files(self.file_paths.directory_ue60))
        self.ln_results_ue90 = DataAccess(self.file_paths.load_files(self.file_paths.directory_ue90))
        self.ln_results_ue120 = DataAccess(self.file_paths.load_files(self.file_paths.directory_ue120))

        self.defineUEs()

        # Dataset by SOUSA et. al. (2023)
        # self.ds_results_attacker2 = None
        # self.ds_results_attacker4 = None
        # self.ds_results_attacker7 = None
        # self.ds_results_attacker9 = None

    def main(self):
        self.plotter.plot_throughput(
            [self.ln_results_ue30.pdcp.get('NrDlPdcpRxStats'),
             self.ln_results_ue60.pdcp.get('NrDlPdcpRxStats'),
             self.ln_results_ue90.pdcp.get('NrDlPdcpRxStats'),
             self.ln_results_ue120.pdcp.get('NrDlPdcpRxStats')],
            ['UE 30', 'UE 60', 'UE 90', 'UE 120']
        )

        self.plotter.plot_throughput(
            [self.ln_results_ue30.rlc.get('NrDlRxRlcStats'),
             self.ln_results_ue60.rlc.get('NrDlRxRlcStats'),
             self.ln_results_ue90.rlc.get('NrDlRxRlcStats'),
             self.ln_results_ue120.rlc.get('NrDlRxRlcStats')],
            ['UE 30', 'UE 60', 'UE 90', 'UE 120']
        )

        self.plotter.plot_throughput(
            [self.ln_results_ue30.rxPacketTrace,
             self.ln_results_ue60.rxPacketTrace,
             self.ln_results_ue90.rxPacketTrace,
             self.ln_results_ue120.rxPacketTrace],
            ['UE 30', 'UE 60', 'UE 90', 'UE 120']
        )

        # self.plotter.plot_vs_ue([
        #     self.ln_results_ue30.rxPacketTrace.tb_size.mean() / 120,
        #     self.ln_results_ue60.rxPacketTrace.tb_size.mean() / 120,
        #     self.ln_results_ue30.rxPacketTrace.tb_size.mean() / 120,
        #     self.ln_results_ue60.rxPacketTrace.tb_size.mean() / 120
        # ], 'Throughput (MBps)', 'Throughput vs UE')

        # self.plotter.plot_throughput(
        #         [self.data_access.rxPacketTrace],
        #         ['UE 30']
        # )

    def defineUEs(self):
        """
        Defines the amount of UEs per scenario.
        """
        self.ln_results_ue30.UEs = 30
        self.ln_results_ue60.UEs = 60
        self.ln_results_ue90.UEs = 90
        self.ln_results_ue120.UEs = 120

    @staticmethod
    def clear_console():
        """
        Clears the console.
        
        Command differs depending on OS.
        
        - For Windows, command is "cls".
        
        - For Linux, command is "clear".
        """
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    main = Main()
    main.main()
