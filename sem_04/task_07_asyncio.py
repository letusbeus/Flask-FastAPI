import asyncio
import requests
import time

urls = ['https://www.google.com/',
        'https://gb.ru/',
        'http://www.onlinepasswordgenerator.ru',
        'https://www.python.org/',
        'https://mail.ru/',
        'https://dropmefiles.com',
        'https://www.gosuslugi.ru/',
        'https://www.dropbox.com/',
        'https://vk.com',
        'https://ok.ru/',
        ]


async def get_urls(url: str, filename: str):
    start = time.time()
    response = requests.get(url)
    with open(f'{filename}', 'w', encoding='utf-8') as f:
        f.write(response.text)
        end = time.time()
    print(f'{url} Status: {response.status_code} Time: {end - start:.2f}')


tasks = []

if __name__ == '__main__':
    for url in urls:
        task = asyncio.ensure_future(get_urls(url, f'file_{url.split("/")[2]}'))
        tasks.append(task)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
