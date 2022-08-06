"""With threading"""
import threading
import time


start = time.perf_counter()


def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')


finish = time.perf_counter()


if __name__ == '__main__':
    threads = []
    for _ in range(10):
        t = threading.Thread(target=do_something)
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    print(f'\nFinished in {round(finish - start, 2)} second(s)')
