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
    def plot_throughput(data, legend):
        try:
            NotAListError.isList(data)
        except NotAListError as e:
            print('NotAListError found:', e)

        plot_maker = PlotMaker.instance()
        plot_maker.create_plot('Tempo (s)', 'Throughput (Mbps)', 'Throughput x Tempo')

        time = []
        throughput = []

        for value in data:
            time.append(DataProcessor.get_time_stamps(value['time'])[:-1])
            throughput.append(DataProcessor.get_throughput(list(value['packetSize']), value['time']))

        plot_maker.plot(time, throughput, legend)
        plot_maker.show()
