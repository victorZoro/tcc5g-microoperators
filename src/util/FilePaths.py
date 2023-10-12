'''
Class that contains all the file paths for the project.

Follows the Singleton pattern.
'''

class FilePaths:
    _instance = None

    def __init__(self):
        '''
        Constructor of FilePaths class. Initializes the list of file paths and adds the files to the list.
        '''
        self._files = []

        # TODO: Add files to the list.

    @property
    def files(self):
        '''
        Getter for the list of file paths.
        '''
        return self._files

    @classmethod
    def instance(cls):
        ''''
        Singleton method that returns the instance of the class.
        '''
        if cls._instance is None:
            cls._instance = FilePaths()
        return cls._instance
