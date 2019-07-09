# 异常处理
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
# 顶层异常
except BaseException as e:
    print('except:', e)
# 没有异常时执行
else:
    print('no error!')
finally:
    print('finally...')

# 错误记录
import logging
try:
    print('try...')
    r = 10 / 0
except Exception as e:
    logging.exception(e)

# 抛出异常
class FooError(ValueError):
    pass
def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n
foo('0')

# 断言
def foo2(s):
    n = int(s)
    assert n != 0, 'n is 0!'
    return n / 10
foo2('0')
# 可以用-O参数来关闭assert 如：python -O err.py

# logging
logging.basicConfig(level = logging.INFO)
logging.info('info')