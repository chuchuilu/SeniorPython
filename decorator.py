import time
"""
decorator是一个输入和输出都是函数的func
"""
def time_cal(func):
    def wrapper(*args, **kwargs):
        print(time.time())
        res = func(*args, **kwargs)
        time.sleep(2)
        print(time.time())
        return res
    return wrapper

@time_cal
def f(a: int, b: int) -> int:
    return a + b


result = f(2, 3)
print(result)
# rest = f(3, b=4)
# print(rest)
