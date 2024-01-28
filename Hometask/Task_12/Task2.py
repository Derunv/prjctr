def catch_errors(func):
    def wrapper(data):
        try:
            data = func(data)
        except KeyError:
            value = list(data.keys())[0]
            print(f'Found 1 error during execution of your function: KeyError no such key as {value}')
    return wrapper



@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])


some_function_with_risky_operation({'foo': 'bar'})
# > Found 1 error during execution of your function: KeyError no such key as foo

# some_function_with_risky_operation({'key': 'bar'})
# > bar