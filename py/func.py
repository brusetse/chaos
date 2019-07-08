import math

# 函数定义
def max_num(a, b):
    if a > b:
        return a
    else:
        return b
print(max(1, 2))
print(max(1, 2, 3))
print(math.pi)

# 空函数 返回None
def nop():
    pass
print(nop())

# 返回多个值
def returnMulti(x, y):
    num1 = x + y
    num2 = x - y
    num3 = x * y
    num4 = x / y
    return num1, num2, num3, num4
num1, num2, num3, num4 = returnMulti(23, 67)
print(num1, num2, num3, num4)

# 默认参数
def defaultParam(a, b = 5):
    return a + b
print(defaultParam(1))

# 传指定参数
def assignParam(a, b = 5, c = 6):
    return a + b + c
print(assignParam(1, c = 7))

# 可变参数 *
def changeable(*nums):
    sum = 0
    for n in nums:
        sum += n * n
    return sum
print(changeable(1, 2, 3, 4, 5))

# 关键字参数 ** 自动组装为一个tuple
def keywordParam(name, age, **keyword):
    print('name: ', name, 'age: ', age, 'keyword: ', keyword)
keywordParam('Michael', 30)
keywordParam('Michael', 30, city='Beijing', job='Engineer')

# 递归
def recursion(n):
    if n == 1:
        return n
    else:
        return n * recursion(n - 1)
print(recursion(10))

# 变量指向函数
f = abs
print(f(-10))

# 传入函数
x = -5
y = -6
def add(x, y, f):
    return f(x) + f(y)
print(add(x, y, abs))

# map 
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def fm(x):
    return x * x
r = map(fm, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

# reduce
# reduce把结果继续和序列的下一个元素做累积计算
# 其效果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def addr(x, y):
    return x + y
r = reduce(addr, [1, 3, 5, 7, 9])
print(r)

# filter 过滤序列
def is_odd(n):
    return n % 2 == 0
r = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(r)

# sorted 排序
print(sorted([36, 5, -12, 9, -21]))
# 忽略大小写
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# 反向排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

# 函数作为返回值 即闭包
def lazy_sum(*args):
    def sum():
        ax = 0
        for arg in args:
            ax += arg
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())
# 每次调用产生新函数
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)

# 闭包 返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i * i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print(f1(), f2(), f3())

# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count2():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs
f1, f2, f3 = count2()
print(f1(), f2(), f3())

# 匿名函数 lambda
print(list(map(lambda x: x * x, [1, 3, 5, 7, 8])))
f = lambda x: x * x
print(f(5))
def build(x, y):
    return lambda: x * x + y * y
print(build(1, 2)())

# 装饰器
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print("2000-01-01")
now()
# 传入参数
def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log2('execute')
def now2():
    print("2001-02-02")
now2()

# 偏函数 Partial function 
# 用于固定参数 多个参数时会自动加在左边
import functools
int2 = functools.partial(int, base=2)
print(int2('1000000'))
max2 = functools.partial(max, 10)
print(max2(5, 6, 7))