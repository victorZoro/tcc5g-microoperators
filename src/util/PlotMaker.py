import locale
from matplotlib import pyplot as plt
from matplotlib import lines


class PlotMaker:
    _instance = None

    def __init__(self):
        self.markers = list(lines.lineMarkers.keys())
        self.line_styles = list(lines.lineStyles.keys())

    def create_plot(self, x_label, y_label, title, ticklabel_format='plain'):
        plt.figure(figsize=(12, 6))
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.ticklabel_format(style=ticklabel_format)
        plt.grid()
        locale.setlocale(locale.LC_NUMERIC, "pt_BR")

    def plot(self, x, y, legend=None, ls='dashed', ms=None):
        if any(isinstance(item, list) for item in (x[0], y[0])):
            for index, (i, j) in enumerate(zip(x, y)):
                plt.plot(i, j, linestyle=self.line_styles[index], marker=ms, linewidth=2)
        else:
            plt.xticks(x)
            plt.plot(x, y, linestyle=ls, marker=ms, linewidth=2, markersize=15)

        if legend:
            plt.legend(legend)

    def scatter(self, x, y, legend=None):
        if any(isinstance(item, list) for item in (x[0], y[0])):
            for index, (i, j) in enumerate(zip(x, y)):
                plt.scatter(i, j, marker=self.markers[index])
        else:
            plt.scatter(x, y)

        if legend:
            plt.legend(legend)

    def show(self):
        plt.show()

    def save(self, file_path):
        plt.savefig(file_path, format='png', dpi='figure', bbox_inches='tight')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = PlotMaker()
        return cls._instance
