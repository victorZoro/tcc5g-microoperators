class NotAListError(Exception):
    @staticmethod
    def is_list(value):
        if not isinstance(value, list):
            raise NotAListError('Value must be a list.')
