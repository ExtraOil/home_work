
def validation(value_type):
    def inner(func):
        def wrapper(*args, **kwargs):
            modified_arg = [value_type(argument)  for argument in args]
            modified_kwargs = {}
            for key, value in kwargs.items():
                modified_kwargs[key] = value_type(value)
            result = func(*modified_arg, **modified_kwargs)
            return result
        return wrapper
    return inner
@validation(int)
def summ(arg1: int, *, arg2: int):
    return arg1, arg2 
print(summ('21', arg2 = '5'))