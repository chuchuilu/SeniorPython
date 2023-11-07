"""
生成器最外层函数立即求值，而内层函数，在迭代时才开始生成
"""
lst = [1, 2, 3, 4, 5]
g = (n for n in lst if n in lst)  # 迭代用前一个list，判断用后一个list，
lst = [0, 1, 2]
print(list(g))  # ----> [1, 2]
