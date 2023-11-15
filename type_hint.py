from typing import List,  Sequence, Union
def add(a: int, b: int) -> int:
    return a + b


# print(add("3", 4)) --> error runtime error


def list_sum(lst: Sequence[int]) -> int:
    total: int = 0
    for i in lst:
        total += i
    return total


print(add(3, 4))
res = list_sum([1, 4.0, 7.2])
print(res)
