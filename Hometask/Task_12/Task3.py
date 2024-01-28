def check_types(func):
    def wrapper(a, b):
        if type(a) != int:
            type_of_arg = str(type(a)).split("'")[1]
            raise TypeError(f'Argument a must be int, not {type_of_arg}')
        elif type(b) != int:
            type_of_arg = str(type(b)).split("'")[1]
            raise TypeError(f'Argument b must be int, not {type_of_arg}')
    return wrapper



@check_types
def add(a: int, b: int) -> int:
    return a + b

# add(1, 2)
# > 3
#
add(1, 2.0)
# > TypeError: Argument a must be int, not str