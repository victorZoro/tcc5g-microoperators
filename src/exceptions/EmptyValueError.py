from src.exceptions.NotAListError import NotAListError


class EmptyValueError(Exception):
    @staticmethod
    def check_for_empty_value(values_list):
        try:
            NotAListError.is_list(values_list)
        except NotAListError as e:
            print("'values_list' is not a list:", e)
            return

        for element in values_list:
            if not element:
                raise EmptyValueError('Value cannot be empty.')
