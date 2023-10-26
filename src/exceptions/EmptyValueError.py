class EmptyValueError(Exception):
    @staticmethod
    def check_empty(variables):
        for variable in variables:
            if not variable:
                raise EmptyValueError('Value cannot be empty.')
