import functools
import time


def log(text=None):
    def derator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if isinstance(text, (int, str)):
                print('%s begin call %s' % (text, func.__name__))
                func(*args, **kw)
                print('%s end call %s' % (text, func.__name__))
            else:
                print('begin call %s' % func.__name__)
                func(*args, **kw)
                print('end call %s' % func.__name__)

        return wrapper

    return derator if isinstance(text, (int, str)) else derator(text)


@log
def f():
    print(time.asctime())


@log('h')
def f1():
    print(time.asctime())


f()
print(' ')
time.sleep(1)
f1()
