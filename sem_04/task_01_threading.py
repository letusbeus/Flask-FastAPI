import threading
import requests


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
    response = requests.get(url)
    with open(f'{filename}', 'w', encoding='utf-8') as f:
        f.write(response.text)


# Решение с семинара
threads = []

for url in urls:
    thread = threading.Thread(target=get_urls, args=(url, f'file_{url.split("/")[2]}'))
    threads.append(thread)

for item in threads:
    item.start()

for item in threads:
    item.join()

# Слегка модифицированное решение по лекции
# threads = []
#
# if __name__ == '__main__':
#     for url in urls:
#         thread = threading.Thread(target=get_urls, args=(url, f'file_{url.split("/")[2]}'))
#         threads.append(thread)
#         thread.start()
#
#     for thread in threads:
#         thread.join()
