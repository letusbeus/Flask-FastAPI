import multiprocessing
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


def get_urls(url: str, filename: str):
    start = time.time()
    response = requests.get(url)
    with open(f'{filename}', 'w', encoding='utf-8') as f:
        f.write(response.text)
        end = time.time()
    print(f'{url} Status: {response.status_code} Time: {end - start:.2f}')


processes = []

if __name__ == '__main__':
    for url in urls:
        process = multiprocessing.Process(target=get_urls, args=(url, f'file_{url.split("/")[2]}'))
        processes.append(process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()
