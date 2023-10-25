from matplotlib import pyplot as plt
from matplotlib import lines

from util.DataAccess import DataAccess


class Plotter:
    _instance = None

    def __init__(self):
        self.markers = list(lines.lineMarkers.keys())
        self.line_styles = list(lines.lineStyles.keys())

    def create_graph(self, x_label, y_label, title):
        """
        Creates a graph.

        Args:
            x_label (str): label for x axis.
            y_label (str): label for y axis.
            title (str): title for graph.
        """
        plt.figure(figsize=(3, 4))
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)

    def plot(self, x, y, legend=None, marker_style=None):
        """
        Plots a graph.

        Args:
            x (list): list of x values.
            y (list): list of y values.
            legend (list): list of legends.
            marker_style (str): marker style.
        """
        if isinstance(x[0], list) or isinstance(y[0], list):
            index = 0
            for i, j in zip(x, y):
                plt.plot(i, j, linestyle=self.line_styles[index], marker=marker_style)
                index += 1
        else:
            plt.plot(x, y, marker=marker_style)

        if legend:
            plt.legend(legend)

    def scatter(self, x, y, legend=None):
        """
        Creates a scatter plot.

        Args:
            x (list): list of x values.
            y (list): list of y values.
            legend (list / str, optional): legend for the plot. Defaults to None.
        """
        index = 0
        for i, j in zip(x, y):
            plt.scatter(i, j, marker=self.markers[index])
            index += 1

        if legend:
            plt.legend(legend)

    def show(self):
        """
        Shows the graph.
        """
        plt.show()

    def save(self, save_path):
        """
        Saves the graph.

        Args:
            save_path (str): path to save the graph.
        """
        plt.savefig(save_path)
        
    
    def seek_for_wrong_type(self, data):
        """
        Checks if the data is of the same type. If not, raises a TypeError.

        Args:
            data (list): list of data.
        """

        for prev_value, value in zip(data, data[1:]):
            if not isinstance(value, type(prev_value)):
                raise TypeError('Data must be of the same type.')

    def plot_throughput(self, data, legend):
        """
        Plots throughput on the screen.
        
        No need for x_label and y_label, since they are always Throughput (MBps) and Tempo (s).

        Args:
            data (list / pandas.Series): data plotted into screen.
            legend (list / str): legend for data.
        """
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

        self.create_graph('Tempo (s)', 'Throughput (MBps)', 'Throughput vs Tempo')
        self.plot(time, throughput, legend)
        self.show()

    def plot_average(self, data, legend, title, y_label):
        """
        Plots data on the screen by average.

        Args:
            data (list / pandas.Series): data plotted into screen
            legend (list / str): legend for data
            title (str): title for plot
            y_label (str): label for data. x_label will always be Tempo (s).
        """
        time = []
        average = []
        
        if isinstance(data, list):
            self.seek_for_wrong_type(data)
            for value in data:
                time.append(DataAccess.get_time_stamps(value.time)[:-1])
                average.append(DataAccess.get_avg_by_second(value.average, value.time))
        else:
            time.append(DataAccess.get_time_stamps(value.time)[:-1])
            average.append(DataAccess.get_avg_by_second(value.average, value.time))
            
        self.create_graph('Tempo (s)', y_label, title)
        self.plot(time, average, legend)
        self.show()

    def plot_vs_ue(self, data, y_label, title):
        """
        Plots data on the screen based off of quantity of UE.

        Args:
            data (list): data to be compared to UE.
            y_label (str): label for data. x_label will always be UE.
            title (str): title for plot.

        Raises:
            TypeError: In order to plot, data must be a list.
        """
        ue = [30, 60, 90, 120]

        if not isinstance(data, list):
            raise TypeError('Data must be a list.')

        self.seek_for_wrong_type(data)

        self.create_graph('UE', y_label, title)
        self.plot(ue, data, marker_style='s')
        self.show()

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = Plotter()
        return cls._instance
