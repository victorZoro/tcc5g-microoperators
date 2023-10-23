from matplotlib import pyplot as plt
from matplotlib import lines


class Plotter:
    _instance = None

    def __init__(self):
        self.markers = list(lines.lineMarkers.keys())
        self.line_styles = list(lines.lineStyles.keys())

    def create_graph(self, x_label, y_label, title):
        plt.figure(figsize=(12, 6))
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)

    def plot(self, x, y, legend=None):
        """
        Plots a graph.

        Args:
            x (list): List of x values.
            y (list): List of y values.
            legend (list): List of legends.
        """

        index = 0
        for i, j in zip(x, y):
            plt.plot(i, j, linestyle=self.line_styles[index], marker=self.markers[index])
            index += 1

        if legend:
            plt.legend(legend)

    def scatter(self, x, y, legend=None):

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
            save_path (str): Path to save the graph.
        """
        plt.savefig(save_path)

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = Plotter()
        return cls._instance
