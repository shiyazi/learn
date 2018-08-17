import functools


def log(text):
    def transit(func):
        @functools.wraps(func)
        def decator(*args, **kw):
            print(text)
            func(*args, **kw)
            print('end call')

        return decator

    return transit


@log('begin call')
def now():
    print('nowadays')
