from src.exceptions.NotAListError import NotAListError


class EmptyValueError(Exception):
    @staticmethod
    def check_for_empty_value(values_list):
        for element in values_list:
            if not element:
                raise EmptyValueError('Value cannot be empty.')
