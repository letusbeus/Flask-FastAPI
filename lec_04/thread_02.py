import threading
import time

# Данный код демонстрирует последовательную работу потоков, друг за другом


def worker(num):
    print(f"Начало работы потока {num}")
    time.sleep(3)
    print(f"Конец работы потока {num}")


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i + 1,))
    threads.append(t)

for t in threads:
    t.start()
    t.join()

print("Все потоки завершили работу")
