from src.data.Dataset import Dataset
from src.processors.PlotProcessor import PlotProcessor
from src.processors.DataProcessor import DataProcessor


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
        self.plot_by_ue()

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

    def plot_delays(self):
        # Simulation Scenarios
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

        # Dataset por SOUSA et al. (2023)
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
        # Simulation Scenarios
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

        # Dataset por SOUSA et al. (2023)
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

    def plot_by_ue(self):
        # Simulation Scenarios
        PlotProcessor.plot_by_ue(
            [
                DataProcessor.get_throughput(self.simulated_tcp[30].dataset['rxPacketTrace']['packetSize'],
                                             self.simulated_tcp[30].dataset['rxPacketTrace']['time']),

                DataProcessor.get_throughput(self.simulated_tcp[60].dataset['rxPacketTrace']['packetSize'],
                                             self.simulated_tcp[60].dataset['rxPacketTrace']['time']),

                DataProcessor.get_throughput(self.simulated_tcp[90].dataset['rxPacketTrace']['packetSize'],
                                             self.simulated_tcp[90].dataset['rxPacketTrace']['time']),

                DataProcessor.get_throughput(self.simulated_tcp[120].dataset['rxPacketTrace']['packetSize'],
                                             self.simulated_tcp[120].dataset['rxPacketTrace']['time']),
            ],
            [30, 60, 90, 120],
            'Usuários ativos',
            'Vazão (MBPS)',
            'Média de Vazão por Cenário',
            './plots/throughput_usuarios_tcp.png'
        )

        PlotProcessor.plot_by_ue(
            [
                DataProcessor.get_avg_by_second(self.simulated_tcp[30].dataset['rx_pdcp']['delay'],
                                                self.simulated_tcp[30].dataset['rx_pdcp']['time']),

                DataProcessor.get_avg_by_second(self.simulated_tcp[60].dataset['rx_pdcp']['delay'],
                                                self.simulated_tcp[60].dataset['rx_pdcp']['time']),

                DataProcessor.get_avg_by_second(self.simulated_tcp[90].dataset['rx_pdcp']['delay'],
                                                self.simulated_tcp[90].dataset['rx_pdcp']['time']),

                DataProcessor.get_avg_by_second(self.simulated_tcp[120].dataset['rx_pdcp']['delay'],
                                                self.simulated_tcp[120].dataset['rx_pdcp']['time']),
            ],
            [30, 60, 90, 120],
            'Usuários ativos',
            'Atraso (ms)',
            'Média de Atraso por Cenário',
            './plots/delay_usuarios_tcp.png'
        )

        PlotProcessor.plot_by_ue(
            [
                DataProcessor.get_jitter(self.simulated_tcp[30].dataset['rx_pdcp']['delay'],
                                         self.simulated_tcp[30].dataset['rx_pdcp']['time']),

                DataProcessor.get_jitter(self.simulated_tcp[60].dataset['rx_pdcp']['delay'],
                                         self.simulated_tcp[60].dataset['rx_pdcp']['time']),

                DataProcessor.get_jitter(self.simulated_tcp[90].dataset['rx_pdcp']['delay'],
                                         self.simulated_tcp[90].dataset['rx_pdcp']['time']),

                DataProcessor.get_jitter(self.simulated_tcp[120].dataset['rx_pdcp']['delay'],
                                         self.simulated_tcp[120].dataset['rx_pdcp']['time']),
            ],
            [30, 60, 90, 120],
            'Usuários ativos',
            'Jitter (ms)',
            'Média de $\it{Jitter}$ por Cenário',
            './plots/jitter_usuarios_tcp.png'
        )

        PlotProcessor.plot_by_ue(
            [
                DataProcessor.get_packet_loss_ratio(self.simulated_tcp[30].dataset['rx_pdcp']['time'],
                                                    self.simulated_tcp[30].dataset['tx_pdcp']['time']),

                DataProcessor.get_packet_loss_ratio(self.simulated_tcp[60].dataset['rx_pdcp']['time'],
                                                    self.simulated_tcp[60].dataset['tx_pdcp']['time']),

                DataProcessor.get_packet_loss_ratio(self.simulated_tcp[90].dataset['rx_pdcp']['time'],
                                                    self.simulated_tcp[90].dataset['tx_pdcp']['time']),

                DataProcessor.get_packet_loss_ratio(self.simulated_tcp[120].dataset['rx_pdcp']['time'],
                                                    self.simulated_tcp[120].dataset['tx_pdcp']['time'])
            ],
            [30, 60, 90, 120],
            'Usuários ativos',
            '$\it{PLR}$ (%)',
            'Média de $\it{PLR}$ por Cenário',
            './plots/plr_usuarios_tcp.png',
            True
        )


if __name__ == '__main__':
    main = Main()
    main.main()
