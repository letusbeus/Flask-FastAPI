import threading
import time
from random import randint

arr = [randint(1, 100) for _ in range(10 ** 6)]
sum_ = 0


def sum_numbers(num_list):
    global sum_
    for i in num_list:
        sum_ += i


threads = []
start = time.time()

if __name__ == '__main__':
    for i in range(10):
        thread = threading.Thread(target=sum_numbers, args=(arr,))
        # thread = threading.Thread(target=sum_numbers, args=[arr[(i-1)*100000:i * 100000]])
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
        print(sum_)
        print(f'{time.time() - start:.2f}')
