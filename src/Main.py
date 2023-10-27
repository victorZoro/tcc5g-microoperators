from src.data.Dataset import Dataset
from src.processors.DataProcessor import DataProcessor
from src.processors.PlotProcessor import PlotProcessor


class Main:
    def __init__(self):
        self.simulated = {
            30: Dataset(UEs=30),
            # 60: Dataset(UEs=60),
            # 90: Dataset(UEs=90),
            # 120: Dataset(UEs=120),
        }

        # self.tested = {
        #     'tcp-tdd': Dataset(UEs=10),
        #     'udp-tdd': Dataset(UEs=9),
        # }
        #
        # self.collected = {
        #     2: Dataset(attackers='2'),
        #     4: Dataset(attackers='4'),
        #     7: Dataset(attackers='7'),
        #     9: Dataset(attackers='9'),
        # }

    def main(self):
        print(self.simulated[30].dataset['flowMonitor'])
        pass


if __name__ == '__main__':
    main = Main()
    main.main()
