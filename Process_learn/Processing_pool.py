import multiprocessing, os, time, random

Pool = multiprocessing.Pool


# print(multiprocessing.cpu_count())


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == "__main__":
    print('Parent Process %s.' % os.getpid())
    p = Pool(4)  # 限制进程池深度
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))  # 往进程池投入一个实例
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocess done')
