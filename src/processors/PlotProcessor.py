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
    def plot_throughput(data, legend, title='Throughput x Tempo', file_path=None):
        try:
            NotAListError.is_list(data)
        except NotAListError as e:
            print('NotAListError found:', e)

        plot_maker = PlotMaker.instance()
        plot_maker.create_plot('Tempo (s)', 'Throughput (Mbps)', title)

        time = []
        throughput = []

        for value in data:
            time.append(PlotProcessor.convert_time_to_set(DataProcessor.get_time_stamps(value['time'])))
            throughput.append(DataProcessor.get_throughput(list(value['packetSize']), value['time']))

        plot_maker.plot(time, throughput, legend)
        if file_path:
            plot_maker.save(file_path)
        plot_maker.show()

    @staticmethod
    def plot_delay(data, legend, title='Delay x Tempo', file_path=None):
        try:
            NotAListError.is_list(data)
        except NotAListError as e:
            print('NotAListError found:', e)

        plot_maker = PlotMaker.instance()
        plot_maker.create_plot('Tempo (s)', 'Delay (s)', title)

        time = []
        delay = []

        for value in data:
            time.append(PlotProcessor.convert_time_to_set(DataProcessor.get_time_stamps(value['time'])))
            delay.append(DataProcessor.get_avg_by_second(list(value['delay']), value['time']))

        plot_maker.plot(time, delay, legend)
        if file_path:
            plot_maker.save(file_path)
        plot_maker.show()



    @staticmethod
    def convert_time_to_set(time):
        return list(set(time))[:-1]
