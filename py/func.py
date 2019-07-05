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