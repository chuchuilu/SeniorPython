"""
iterable:可迭代对象
iterator:迭代器

"""

def gen(num):
    while num > 0:
        yield num
        num -= 1
    return


g = gen(5)
first_g = next(g)
print(first_g)
sec_g = next(g)
print(sec_g)
for i in g:
    print(i)
