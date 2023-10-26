class NotAListError(Exception):
    @staticmethod
    def isList(variable):
        if not isinstance(variable, list):
            raise NotAListError('Value must be a list.')