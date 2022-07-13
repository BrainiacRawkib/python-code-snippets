"""concurrent module"""
import concurrent.futures
import time


start = time.perf_counter()


def do_something(sec):
    print(f'Sleeping {sec} second(s)...')
    time.sleep(sec)
    return f'Done Sleeping...{sec}'


finish = time.perf_counter()


if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # f1 = executor.submit(do_something, 1)
        # f2 = executor.submit(do_something, 1)
        #
        # print(f1.result())
        # print(f2.result())
        secs = [5, 4, 3, 2, 1]
        results = [executor.submit(do_something, sec) for sec in secs]

        for f in concurrent.futures.as_completed(results):
            print(f.result())

    print(f'\nFinished in {round(finish - start, 2)} second(s)')
