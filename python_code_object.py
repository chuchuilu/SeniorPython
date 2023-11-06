def f(a, b, *, c, d, **kwargs):
    a = 5
    print(1)


code = f.__code__
print(f.__code__)  # 函数code_object
print(code.co_code)  # 也就是汇编

# meta data
print(code.co_name)
print(code.co_filename)
print(code.co_lnotab)  # mapping 源码行数保存

print(code.co_flags)  # bit map
print(code.co_stacksize)  # size
print("argument", code.co_argcount)
print("pos_argument", code.co_posonlyargcount)
print("keywords_argument", code.co_kwonlyargcount)

print(f"nlocals:{code.co_nlocals}")  # local variable length
print(f"varnames:{code.co_varnames}")  # local variable
print(f"co_names:{code.co_names}")  # used f(x)
print(f"cellvars:{code.co_cellvars}")  # 成对出现，实现闭包
print(f"freevars:{code.co_freevars}")
print(f"consts:{code.co_consts}")  # all const
