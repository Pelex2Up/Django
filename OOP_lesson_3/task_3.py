def validate_sum(*types):
    def check_types(f):
        def wrapper(*args):
            for (i, v) in zip(args, types):
                assert isinstance(i, v), f'Аргумент {i}, не соответствует типу {v}.'
            return f(*args)
        return wrapper
    return check_types


@validate_sum(int, int)
def summa(a, b): return a + b


print(summa(42, 56))
