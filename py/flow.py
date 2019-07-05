# 条件
age = 20
if age >= 18:
    print('age: ', age)
    print('adult')
elif age <= 6:
    print('kid')
else:
    print('teenager')

# 循环
names = ['Kevin', 'Alex', 'Eva']
for name in names:
    print(name)

# 整数序列
listR = list(range(5))
print(listR)
for i in range(5):
    print(i)
for i in listR:
    print(i)

# while
start = 0
sum = 0
while start <= 50:
    start += 1
    sum += start
print(sum)

# break
listR = list(range(5))
sum = 0
for i in listR:
    if i > 2:
        break
    sum += i
print(sum)

# continue
listR = list(range(5))
sum = 0
for i in listR:
    if i % 2 == 0:
        continue
    sum += i
print(sum)