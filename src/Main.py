from src.data.Dataset import Dataset
from src.processors.PlotProcessor import PlotProcessor


class Main:
    def __init__(self):
        self.simulated_tcp = {
            30: Dataset(UEs=30, protocol='TCP'),
            60: Dataset(UEs=60, protocol='TCP'),
            90: Dataset(UEs=90, protocol='TCP'),
            120: Dataset(UEs=120, protocol='TCP'),
        }

        self.simulated_udp = {
            30: Dataset(UEs=30, protocol='UDP'),
            60: Dataset(UEs=60, protocol='UDP'),
            90: Dataset(UEs=90, protocol='UDP'),
            120: Dataset(UEs=120, protocol='UDP'),
        }

        self.collected = {
            2: Dataset(attackers='2'),
            4: Dataset(attackers='4'),
            7: Dataset(attackers='7'),
            9: Dataset(attackers='9'),
        }

    def main(self):
        # self.plot_throughputs()
        self.plot_delays()

    def plot_throughputs(self):
        PlotProcessor.plot_throughput(
            [
                self.simulated_tcp[30].dataset['rxPacketTrace'],
                self.simulated_tcp[60].dataset['rxPacketTrace'],
                self.simulated_tcp[90].dataset['rxPacketTrace'],
                self.simulated_tcp[120].dataset['rxPacketTrace']
            ],
            ['30 UEs', '60 UEs', '90 UEs', '120 UEs'],
            'Throughput x Tempo (TCP - RxPacketTrace)',
            './plots/rx_throughput_tempo_tcp.png'
        )

        PlotProcessor.plot_throughput(
            [
                self.simulated_udp[30].dataset['rxPacketTrace'],
                self.simulated_udp[60].dataset['rxPacketTrace'],
                self.simulated_udp[90].dataset['rxPacketTrace'],
                self.simulated_udp[120].dataset['rxPacketTrace']
            ],
            ['30 UEs', '60 UEs', '90 UEs', '120 UEs'],
            'Throughput x Tempo (UDP - RxPacketTrace)',
            './plots/rx_throughput_tempo_tcp.png'

        )

        PlotProcessor.plot_throughput(
            [
                self.simulated_tcp[30].dataset['pdcp'],
                self.simulated_tcp[60].dataset['pdcp'],
                self.simulated_tcp[90].dataset['pdcp'],
                self.simulated_tcp[120].dataset['pdcp']
            ],
            ['30 UEs', '60 UEs', '90 UEs', '120 UEs'],
            'Throughput x Tempo (TCP - Camada PDCP)',
            './plots/pdcp_throughput_tempo_tcp.png'
        )

        PlotProcessor.plot_throughput(
            [
                self.simulated_udp[30].dataset['pdcp'],
                self.simulated_udp[60].dataset['pdcp'],
                self.simulated_udp[90].dataset['pdcp'],
                self.simulated_udp[120].dataset['pdcp']
            ],
            ['30 UEs', '60 UEs', '90 UEs', '120 UEs'],
            'Throughput x Tempo (UDP - Camada PDCP)',
            './plots/pdcp_throughput_tempo_tcp.png'

        )

        PlotProcessor.plot_throughput(
            [
                self.simulated_tcp[30].dataset['rlc'],
                self.simulated_tcp[60].dataset['rlc'],
                self.simulated_tcp[90].dataset['rlc'],
                self.simulated_tcp[120].dataset['rlc']
            ],
            ['30 UEs', '60 UEs', '90 UEs', '120 UEs'],
            'Throughput x Tempo (TCP - Camada RLC)',
            './plots/rlc_throughput_tempo_tcp.png'
        )

        PlotProcessor.plot_throughput(
            [
                self.simulated_udp[30].dataset['rlc'],
                self.simulated_udp[60].dataset['rlc'],
                self.simulated_udp[90].dataset['rlc'],
                self.simulated_udp[120].dataset['rlc']
            ],
            ['30 UEs', '60 UEs', '90 UEs', '120 UEs'],
            'Throughput x Tempo (UDP - Camada RLC)',
            './plots/rlc_throughput_tempo_tcp.png'

        )

        PlotProcessor.plot_throughput(
            [
                self.collected[2].dataset,
                self.collected[4].dataset,
                self.collected[7].dataset,
                self.collected[9].dataset
            ],
            ['2 attackers', '4 attackers', '7 attackers', '9 attackers'],
            'Throughput x Tempo (Dataset por SOUSA et al. (2023))'
        )

    def plot_delays(self):
        PlotProcessor.plot_delay(
            [
                self.simulated_udp[30].dataset['pdcp'],
                self.simulated_udp[60].dataset['pdcp'],
                self.simulated_udp[90].dataset['pdcp'],
                self.simulated_udp[120].dataset['pdcp']
            ],
            ['30 UEs', '60 UEs', '90 UEs', '120 UEs'],
            'Delay x Tempo (UDP - Camada PDCP)',
            './plots/pdcp_delay_tempo_udp.png'
        )

        PlotProcessor.plot_delay(
            [
                self.simulated_udp[30].dataset['rlc'],
                self.simulated_udp[60].dataset['rlc'],
                self.simulated_udp[90].dataset['rlc'],
                self.simulated_udp[120].dataset['rlc']
            ],
            ['30 UEs', '60 UEs', '90 UEs', '120 UEs'],
            'Delay x Tempo (UDP - Camada PDCP)',
            './plots/rlc_delay_tempo_udp.png'
        )

        PlotProcessor.plot_delay(
            [
                self.collected[2].dataset,
                self.collected[4].dataset,
                self.collected[7].dataset,
                self.collected[9].dataset
            ],
            ['2 attackers', '4 attackers', '7 attackers', '9 attackers'],
            'Throughput x Tempo (Dataset por SOUSA et al. (2023))'
        )

if __name__ == '__main__':
    main = Main()
    main.main()
