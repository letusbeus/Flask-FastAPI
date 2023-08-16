import threading
import os


def count_words(filename: str):
    # Use ISO-8859-1 instead of utf-8 to prevent the encoding error (for cyrillic characters in files)
    with open(filename, 'r', encoding='ISO-8859-1') as f:
        text = f.read()
        count = len(text.split())
    print(f'File {filename} contains {count} words.')

threads = []
# Укажите путь к директории обхода (вместо os.getcwd()) либо будет использоваться текущая директория
files = next(os.walk(os.getcwd()))[2]

if __name__ == '__main__':
    for file in files:
        thread = threading.Thread(target=count_words, args=(file,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
