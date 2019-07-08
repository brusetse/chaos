# 类和实例
class Student(object):
    pass

bart = Student()
print(bart)
bart.name = 'Bart Simpson'
print(bart.name)

# 实例化方法
class StudentInit(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

bartInit = StudentInit('Bart Simpson', 19)
print(bartInit.name, bartInit.age)

# 封装
class StudentMethod(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_age(self):
        print('%s: %s' % (self.name, self.age))

bartMethod = StudentMethod('Bart Simpson', 19)
bartMethod.print_age()

# 内部属性
class StudentPrivate(object):
    # 以两个下划线前缀
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    # get
    def get_name(self):
        return self.__name
    # set
    def set_name(self, name):
        self.__name = name

bartPrivate = StudentPrivate('Bart Simpson', 19)
bartPrivate.set_name('Kim Kardashian')
print(bartPrivate.get_name())

# 继承
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running')

class Cat(Animal):
    def run(self):
        print('Cat is running')

dog = Dog()
dog.run()
cat = Cat()
cat.run()

# 多态
def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Dog())
run_twice(Cat())

# 静态语言 vs 动态语言
# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了
# 动态语言继承不是必须的
class Timer(object):
    def run(self):
        print('Start...')
run_twice(Timer())

# 获取对象信息
import types
print(type(123))
print(type(abs))
print(type(123) == int)
print(type(abs) == types.BuiltinFunctionType)
print(isinstance(cat, Cat))
print(isinstance(cat, Animal))
print(isinstance(123, int))

# 获取对象所有属性和方法
print(dir('123'))
print('123'.__len__())
class MyDog(object):
    def __len__(self):
        return 100
print(len(MyDog()))

class MyObj(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObj()
# 有属性'x'吗？
print(hasattr(obj, 'x'))
# 设置一个属性'y'
setattr(obj, 'y', 9)
print(hasattr(obj, 'y'))
# 获取属性'y'
print(getattr(obj, 'y'))
# 有属性'power'吗？
print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
# fn指向obj.power 调用fn()与调用obj.power()是一样的
fn = getattr(obj, 'power')
print(fn())

# 类属性
class Teacher(object):
    name = 'Teacher'
sam = Teacher()
print(sam.name)
# 实例属性优先级高于类属性
sam.name = 'Sam'
print(sam.name)
# 类属性仍然可以访问
print(Teacher.name)
# 删除实例属性
del sam.name
# 由于实例属性没有找到，类属性就显示出来了
print(sam.name)