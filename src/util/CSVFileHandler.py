import pandas as pandas


class CSVFileHandler:
    _instance = None

    def __init__(self):
        self.file_path = None

    def create_csv(self, info):
        if not isinstance(info, list):
            raise TypeError("The parameter for createCSV(list) must be a list.")

        # aux = []

        for i in info:
            if not isinstance(i, pandas.core.series.Series):
                raise TypeError("The elements of the list must be pandas.Series objects.")

            if i.empty:
                raise ValueError("The elements of the list must not be empty.")

            # if i.name == 'time':
            #     aux.append(i)
            #     info.pop(i)
            #     aux = aux + info
            #     break

        # df = pandas.DataFrame(aux)

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = CSVFileHandler()
        return cls._instance

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, path):
        self._file_path = path
