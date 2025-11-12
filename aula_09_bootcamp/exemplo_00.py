from utils_log import log_decorator


@log_decorator
def soma(a, b):
    return a + b


soma(2, 3)
soma(2, 7)
