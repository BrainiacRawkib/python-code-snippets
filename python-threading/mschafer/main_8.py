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
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something, secs)
        # for result in results:
        #     print(result)
    print(f'\nFinished in {round(finish - start, 2)} second(s)')
