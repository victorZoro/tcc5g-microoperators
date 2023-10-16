import os

from src.util.DataAccess import DataAccess
from src.util.FilePaths import FilePaths
from src.util.Plotter import Plotter


class Main:
    def __init__(self):
        self.file_paths = FilePaths.instance()
        self.da = DataAccess(self.file_paths.files)

    def main(self):
        self.clear_console()
        # y = [
        #     self.da.pdcp.get('NrDlPdcpRxStats').delay,
        #     self.da.rlc.get('NrDlRxRlcStats').delay
        # ]
        #
        # x = [
        #     self.da.pdcp.get('NrDlPdcpRxStats').time,
        #     self.da.rlc.get('NrDlRxRlcStats').time
        # ]
        #
        #
        # Plotter.plot(x, y, 'x', 'y', 'title', ['legend1', 'legend2'])

        avg = self.da.get_avg_by_second(self.da.rxPacketTrace.SINR, self.da.rxPacketTrace.time)
        time = self.da.get_time_stamps(self.da.rxPacketTrace.time)[:-1] # Ignores last value.

        print(avg, time)
        Plotter.plot(time, avg, 'Time(s)', 'SINR(dB)', 'SINR vs Time')

    @staticmethod
    def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    main = Main()
    main.main()
