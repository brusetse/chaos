# 多行字符串''''''
print('''111
222
333''')

# 布尔值
booleanT = True
booleanF = False
print(booleanT & booleanF)
print(booleanT | booleanF)

# 空值
varN = None
print(varN)

# 动态语言  
varDynamic = 10
print(varDynamic)
varDynamic = "String"
print(varDynamic)

# 常量 动态语言没有常量保留字 必须通过常量类才能实现
PI = 3.14159265359

# 格式化
print('Hi %s, your score is %d.' % ('Bart', 59))

# format()
print('Hi {0}, your score is {1}.'.format('Kevin', 58))

# 列表
classmates = ['Albert', 'Bob', 'Evens']
print(classmates)
print(classmates[2])
classmates.append('Floda')
print(len(classmates))

# 有序列表
classmatesTuple = ('Albert', 'Bob', 'Evens')
print(classmatesTuple)

# dict 相当于 map
dictS = {
    'Michael': 95,
    'Kevin': 80,
    'Leon': 65
}
print(dictS)
print(dictS['Leon'])

# set
setS = set([1, 2, 3])
print(setS)
setS.remove(3)
setS.add(4)
for s in setS:
    print(s)