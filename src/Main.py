from util import FilePaths
from data import Dataset
import DataAccess
import pandas as pd

test = FilePaths.FilePaths.instance()

try:
    print(test.search_file('DlCtrlSinr', 'txt'))
except ValueError as e:
    print(e)
except TypeError as e:
    print(e)

# da = DataAccess.DataAccess(test.files)

# print(da.ctrl.dataset['Time'].head())
