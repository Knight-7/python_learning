from functools import wraps
from time import time


def record_func_time(func):
    """
    自定义修饰函数的装饰器
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f'{func.__name__}:{time() - start}')
        return result

    return wrapper()


@record_func_time
def sum(*args):
    res = 0
    for i in args:
        res += i
    return res


if __name__ == '__main__':
    print(sum.__name__)