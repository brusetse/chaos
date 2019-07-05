import math

# 函数定义
def max_num(a, b):
    if a > b:
        return a
    else:
        return b

# 空函数 返回None
def nop():
    pass

# 返回多个值
def returnMulti(x, y):
    num1 = x + y
    num2 = x - y
    num3 = x * y
    num4 = x / y
    return num1, num2, num3, num4

# 默认参数
def defaultParam(a, b = 5):
    return a + b

# 传指定参数
def assignParam(a, b = 5, c = 6):
    return a + b + c

# 可变参数 *
def changeable(*nums):
    sum = 0
    for n in nums:
        sum += n * n
    return sum

# 关键字参数 ** 自动组装为一个tuple
def keywordParam(name, age, **keyword):
    print('name: ', name, 'age: ', age, 'keyword: ', keyword)

# 递归
def recursion(n):
    if n == 1:
        return n
    else:
        return n * recursion(n - 1)

print(max(1, 2))
print(max(1, 2, 3))
num1, num2, num3, num4 = returnMulti(23, 67)
print(num1, num2, num3, num4)
print(math.pi)
print(nop())
print(defaultParam(1))
print(assignParam(1, c = 7))
print(changeable(1, 2, 3, 4, 5))
keywordParam('Michael', 30)
keywordParam('Michael', 30, city='Beijing', job='Engineer')
print(recursion(10))