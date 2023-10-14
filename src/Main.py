from util import FilePaths
from src.util import DataAccess

file_paths = FilePaths.FilePaths.instance()


def load_files():
    file_names = file_paths.get_file_names()

    for file in file_names:
        file_paths.add_file({file: file_paths.search_file(file, 'txt')})
        print('Successful loading for file:', file)


load_files()

da = DataAccess.DataAccess(file_paths.files)

print(da.pdcp.get('NrDlPdcpRxStats').dataset.head())

