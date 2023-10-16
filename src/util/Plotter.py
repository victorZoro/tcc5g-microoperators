from matplotlib import pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.markers import MarkerStyle


class Plotter:
    def __init__(self):
        self.markers = MarkerStyle.markers.keys()
        self.line_styles = Line2D.lineStyles.keys()

    @staticmethod
    def plot(x, y, x_label, y_label, title, legend=None, save_path=None):
        """
        Plots a graph.

        Args:
            x (list): List of x values.
            y (list): List of y values.
            x_label (str): Label of x axis.
            y_label (str): Label of y axis.
            title (str): Title of the graph.
            legend (list): List of legends.
            save_path (str): Path to save the graph.
        """
        plt.figure(figsize=(12, 6))

        plt.plot(x,y)

        # for i, j in zip(x, y):
        #     plt.plot(i, j)

        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)

        if legend:
            plt.legend(legend)

        if save_path:
            plt.savefig(save_path)
        plt.show()
