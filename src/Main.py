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

        self.collected = {
            2: Dataset(attackers='2'),
            4: Dataset(attackers='4'),
            7: Dataset(attackers='7'),
            9: Dataset(attackers='9'),
        }

    def main(self):
        self.plot_throughputs()
        self.plot_delays()
        self.plot_jitters()

    def plot_throughputs(self):
        PlotProcessor.plot_throughput(
            [
                self.simulated_tcp[30].dataset['rxPacketTrace'],
                self.simulated_tcp[60].dataset['rxPacketTrace'],
                self.simulated_tcp[90].dataset['rxPacketTrace'],
                self.simulated_tcp[120].dataset['rxPacketTrace']
            ],
            ['30 UEs', '60 UEs', '90 UEs', '120 UEs'],
            'Medidas de Vazão',
            './plots/rx_throughput_tempo_tcp.png',
            [30, 60, 90, 120]
        )

        PlotProcessor.plot_throughput(
            [
                self.collected[2].dataset,
                self.collected[4].dataset,
                self.collected[7].dataset,
                self.collected[9].dataset
            ],
            ['2 attackers', '4 attackers', '7 attackers', '9 attackers'],
            'Medidas de Vazão (Dataset por SOUSA et al. (2023))',
            y_label='Vazão (Kbps)'
        )

    def plot_delays(self):
        PlotProcessor.plot_delay(
            [
                self.simulated_tcp[30].dataset['rx_pdcp'],
                self.simulated_tcp[60].dataset['rx_pdcp'],
                self.simulated_tcp[90].dataset['rx_pdcp'],
                self.simulated_tcp[120].dataset['rx_pdcp']
            ],
            ['30 UEs', '60 UEs', '90 UEs', '120 UEs'],
            'Medidas de Atraso',
            './plots/pdcp_delay_tempo_tcp.png'
        )

        PlotProcessor.plot_delay(
            [
                self.collected[2].dataset,
                self.collected[4].dataset,
                self.collected[7].dataset,
                self.collected[9].dataset
            ],
            ['2 attackers', '4 attackers', '7 attackers', '9 attackers'],
            'Medidas de Atraso com Ataques à Rede (Dataset por SOUSA et al. (2023))',
            './plots/delay_tempo_dataset_attacked.png'
        )

        PlotProcessor.plot_delay(
            [
                self.collected[2].dataset,
                self.collected[4].dataset,
                self.collected[7].dataset,
                self.collected[9].dataset
            ],
            ['2 attackers', '4 attackers', '7 attackers', '9 attackers'],
            'Medidas de Atraso sem Ataques à Rede (Dataset por SOUSA et al. (2023))',
            './plots/delay_tempo_dataset_not_attacked.png',
            is_attack=0
        )

    def plot_jitters(self):
        PlotProcessor.plot_jitter(
            [
                self.simulated_tcp[30].dataset['rx_pdcp'],
                self.simulated_tcp[60].dataset['rx_pdcp'],
                self.simulated_tcp[90].dataset['rx_pdcp'],
                self.simulated_tcp[120].dataset['rx_pdcp']
            ],
            ['30 UEs', '60 UEs', '90 UEs', '120 UEs'],
            'Medidas de $\it{Jitter}$',
            './plots/pdcp_jitter_tempo_tcp.png'
        )

        PlotProcessor.plot_jitter(
            [
                self.collected[2].dataset,
                self.collected[4].dataset,
                self.collected[7].dataset,
                self.collected[9].dataset
            ],
            ['2 attackers', '4 attackers', '7 attackers', '9 attackers'],
            'Medidas de $\it{Jitter}$ com Ataques à Rede (Dataset por SOUSA et al. (2023))',
            './plots/jitter_tempo_dataset_attacked.png'
        )

        PlotProcessor.plot_jitter(
            [
                self.collected[2].dataset,
                self.collected[4].dataset,
                self.collected[7].dataset,
                self.collected[9].dataset
            ],
            ['2 attackers', '4 attackers', '7 attackers', '9 attackers'],
            'Medidas de $\it{Jitter}$ sem Ataques à Rede (Dataset por SOUSA et al. (2023))',
            './plots/jitter_tempo_dataset_not_attacked.png',
            is_attack=0
        )


if __name__ == '__main__':
    main = Main()
    main.main()
