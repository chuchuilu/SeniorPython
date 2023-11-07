import time
"""
等价于 add = Timer(add)
等价于实例化一个函数
"""

class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        ret = self.func(*args, **kwargs)
        print(f"Time: {time.time() - start}")
        return ret


class TTimer:
    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            start = time.time()
            ret = func(*args, **kwargs)
            print(f"{self.prefix}{time.time() - start}")
            return ret
        return wrapper

@TTimer(prefix="current time")
def add(a, b):
    return a + b


print(add(5, 6))