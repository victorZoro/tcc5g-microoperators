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
        self.ln_results_ue60 = DataAccess(self.file_paths.load_files(self.file_paths.directory_ue60))
        # self.ln_results_ue90 = DataAccess(self.file_paths.load_files(self.file_paths.directory_ue90))
        # self.ln_results_ue120 = DataAccess(self.file_paths.load_files(self.file_paths.directory_ue120))

        # Dataset by SOUSA et. al. (2023)
        # self.ds_results_attacker2 = None
        # self.ds_results_attacker4 = None
        # self.ds_results_attacker7 = None
        # self.ds_results_attacker9 = None

    def main(self):
        # self.plot_throughput(
        #     [self.ln_results_ue30.pdcp.get('NrDlPdcpRxStats'),
        #      self.ln_results_ue60.pdcp.get('NrDlPdcpRxStats')],
        #     ['UE 30', 'UE 60']
        # )

        self.plot_vs_ue([
            self.ln_results_ue30.rxPacketTrace.tb_size.mean(),
            self.ln_results_ue60.rxPacketTrace.tb_size.mean(),
            self.ln_results_ue30.rxPacketTrace.tb_size.mean(),
            self.ln_results_ue60.rxPacketTrace.tb_size.mean()
        ], 'Throughput (MBps)', 'Throughput vs UE')

        # print(self.ln_results_ue30.rxPacketTrace.tb_size.mean())

    def seek_for_wrong_type(self, data):
        """
        Checks if the data is of the same type. If not, raises a TypeError.

        Args:
            data (list): List of data.
        """

        for prev_value, value in zip(data, data[1:]):
            if not isinstance(value, type(prev_value)):
                raise TypeError('Data must be of the same type.')

    def plot_throughput(self, data, legend):
        time = []
        throughput = []

        if isinstance(data, list):
            self.seek_for_wrong_type(data)
            for value in data:
                time.append(DataAccess.get_time_stamps(value.time)[:-1])
                throughput.append(DataAccess.get_throughput(value.packet_size, value.time))
        else:
            time.append(DataAccess.get_time_stamps(data.time)[:-1])
            throughput.append(DataAccess.get_throughput(data.packet_size, data.time))

        self.plotter.create_graph('Tempo (s)', 'Throughput (MBps)', 'Throughput vs Tempo')
        self.plotter.plot(time, throughput, legend)
        self.plotter.show()

    def plot_delay(self, data, legend):
        pass

    def plot_vs_ue(self, data, y_label, title):
        ue = [30, 60, 90, 120]

        if not isinstance(data, list):
            raise TypeError('Data must be a list.')

        self.seek_for_wrong_type(data)

        self.plotter.create_graph('UE', y_label, title)
        self.plotter.plot(ue, data, marker_style='s')
        self.plotter.show()

    @staticmethod
    def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    main = Main()
    main.main()
