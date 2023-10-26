from src.data.Dataset import Dataset
from src.processors.DataProcessor import DataProcessor
from src.processors.PlotProcessor import PlotProcessor
from src.util.PlotMaker import PlotMaker


class Main:
    def __init__(self):
        # self.simulated = {
        #     '30': Dataset(UEs=30),
        #     '60': Dataset(UEs=60),
        #     '90': Dataset(UEs=90),
        #     '120': Dataset(UEs=120),
        # }

        self.tested = {
            'tcp-tdd': Dataset(UEs=10),
            'udp-tdd': Dataset(UEs=9),
        }

        # self.collected = {
        #     '2': Dataset(attackers='2'),
        #     '4': Dataset(attackers='4'),
        #     '7': Dataset(attackers='7'),
        #     '9': Dataset(attackers='9'),
        # }

    def main(self):
        # PlotProcessor.plot_throughput(
        #     [self.simulated['30'].dataset['rxPacketTrace'],
        #      self.simulated['60'].dataset['rxPacketTrace'],
        #      self.simulated['90'].dataset['rxPacketTrace'],
        #      self.simulated['120'].dataset['rxPacketTrace']],
        #     ['30 UEs', '60 UEs', '90 UEs', '120 UEs']
        # )
        # PlotProcessor.plot_throughput(
        #     [
        #         self.collected['2'].dataset,
        #         self.collected['4'].dataset,
        #         self.collected['7'].dataset,
        #         self.collected['9'].dataset,
        #     ],
        #     ['2 attackers', '4 attackers', '7 attackers', '9 attackers']
        # )
        PlotProcessor.plot_throughput(
            [
                self.tested['tcp-tdd'].dataset['rxPacketTrace'],
                self.tested['udp-tdd'].dataset['rxPacketTrace'],
            ],
            ['TCP-TDD', 'UDP-TDD']
        )

        PlotProcessor.plot_throughput(
            [
                self.tested['tcp-tdd'].dataset['pdcp'],
                self.tested['udp-tdd'].dataset['pdcp'],
            ],
            ['TCP-TDD', 'UDP-TDD']
        )

        PlotProcessor.plot_throughput(
            [
                self.tested['tcp-tdd'].dataset['rlc'],
                self.tested['udp-tdd'].dataset['rlc'],
            ],
            ['TCP-TDD', 'UDP-TDD']
        )
        pass


if __name__ == '__main__':
    main = Main()
    main.main()
