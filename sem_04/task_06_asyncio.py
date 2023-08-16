import asyncio
import os


async def count_words(filename: str):
    # Use ISO-8859-1 instead of utf-8 to prevent the encoding error (for cyrillic characters in files)
    with open(filename, 'r', encoding='ISO-8859-1') as f:
        text = f.read()
        count = len(text.split())
    print(f'File {filename} contains {count} words.')


tasks = []
# Укажите путь к директории обхода (вместо os.getcwd()) либо будет использоваться текущая директория
files = next(os.walk(os.getcwd()))[2]

if __name__ == '__main__':
    for file in files:
        task = asyncio.ensure_future(count_words(file))
        tasks.append(task)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
