import functools
import time


def metric(func):
    @functools.wraps(func)
    def decorator(*args, **kw):
        t0 = time.perf_counter()
        back = func(*args, **kw)
        t1 = time.perf_counter()
        t = t1 - t0
        print('%s executed in %s ms' % (func.__name__, t))
        return back

    return decorator

time.process_time()
# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
