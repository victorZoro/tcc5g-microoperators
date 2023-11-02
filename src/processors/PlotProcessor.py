from src.exceptions.NotAListError import NotAListError
from src.processors.DataProcessor import DataProcessor
from src.util.PlotMaker import PlotMaker


class PlotProcessor:
    @staticmethod
    def seek_wrong_type(data):
        for previous_value, value in zip(data, data[:1]):
            if not isinstance(value, type(previous_value)):
                raise TypeError('The data is not of the same type.')

    @staticmethod
    def plot_throughput(data, legend, title='Medidas de Vazão', file_path=None, UEs=None, y_label='Vazão (Mbps)'):
        try:
            NotAListError.is_list(data)
        except NotAListError as e:
            print('NotAListError found:', e)

        plot_maker = PlotMaker.instance()
        plot_maker.create_plot('Tempo (s)', y_label, title)

        time = []
        throughput = []
        if UEs:
            for (value, UE) in zip(data, UEs):
                time.append(DataProcessor.convert_time_to_set(DataProcessor.get_time_stamps(value['time'])))
                throughput.append(DataProcessor.get_throughput(list(value['packetSize']), value['time']))
        else:
            for value in data:
                time.append(DataProcessor.convert_time_to_set(DataProcessor.get_time_stamps(value['time'])))
                throughput.append(DataProcessor.get_throughput(list(value['packetSize']), value['time']))

        plot_maker.plot(time, throughput, legend)
        if file_path:
            plot_maker.save(file_path)
        plot_maker.show()

    @staticmethod
    def plot_delay(data, legend, title='Medidas de Atraso', file_path=None, UEs=None, is_attack=None):
        try:
            NotAListError.is_list(data)
        except NotAListError as e:
            print('NotAListError found:', e)

        plot_maker = PlotMaker.instance()
        plot_maker.create_plot('Tempo (s)', 'Atraso (ms)', title)

        time = []
        delay = []

        if is_attack == 0:
            for value in data:
                time.append(DataProcessor.convert_time_to_set(
                    DataProcessor.get_time_stamps(DataProcessor.get_not_attacked_packets(value)[1])
                ))

                delay.append(
                    DataProcessor.get_avg_by_second(
                        DataProcessor.get_not_attacked_packets(value)[0],  # delay
                        DataProcessor.get_not_attacked_packets(value)[1]  # time
                    )
                )
        else:
            for value in data:
                time.append(DataProcessor.convert_time_to_set(DataProcessor.get_time_stamps(value['time'])))
                if UEs:
                    delay.append(DataProcessor.get_avg_by_second(value['delay'], value['time'], scale=1e3))
                else:
                    delay.append(DataProcessor.get_avg_by_second(value['delay'], value['time']))

        plot_maker.plot(time, delay, legend)
        if file_path:
            plot_maker.save(file_path)
        plot_maker.show()

    @staticmethod
    def plot_jitter(data, legend, title='Medidas de $\it{Jitter}$', file_path=None, UEs=None, is_attack=None):
        try:
            NotAListError.is_list(data)
        except NotAListError as e:
            print('NotAListError found:', e)

        plot_maker = PlotMaker.instance()
        plot_maker.create_plot('Tempo (s)', '$\it{Jitter}$ (ms)', title)

        time = []
        jitter = []

        if is_attack == 0:
            for value in data:
                time.append(DataProcessor.convert_time_to_set(
                    DataProcessor.get_time_stamps(DataProcessor.get_not_attacked_packets(value)[1])
                ))

                jitter.append(
                    DataProcessor.get_jitter(
                        DataProcessor.get_not_attacked_packets(value)[0],  # delay
                        DataProcessor.get_not_attacked_packets(value)[1]  # time
                    )
                )
        else:
            for value in data:
                time.append(DataProcessor.convert_time_to_set(DataProcessor.get_time_stamps(value['time'])))
                if UEs:
                    jitter.append(DataProcessor.get_jitter(value['delay'], value['time']))
                else:
                    jitter.append(DataProcessor.get_jitter(value['delay'], value['time']))

        plot_maker.plot(time, jitter, legend)
        if file_path:
            plot_maker.save(file_path)
        plot_maker.show()
