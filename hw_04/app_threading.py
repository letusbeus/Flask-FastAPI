import threading
import requests
import sys
from time import perf_counter
import view

data = ['https://i.pinimg.com/474x/d1/4f/66/d14f66ddf892b7406a2113e022698a6e.jpg',
        'https://i.pinimg.com/236x/34/0f/37/340f37ae4f36826f3571a2f9c64544ec.jpg',
        'https://i.pinimg.com/236x/fe/21/ec/fe21ec8896e94f73a3c9dfab95a407d1.jpg',
        'https://i.pinimg.com/236x/cc/70/7f/cc707f00a9daca98b659c3baa22f63fb.jpg',
        'https://i.pinimg.com/236x/c4/a1/fb/c4a1fbcaea554244c817a6618aeb3ce0.jpg',
        ]
threads = []


def get_img(url: str):
    start_img = perf_counter()
    response = requests.get(url)
    filename = url.split('/')[-1]
    with open(f'{filename}', 'wb') as f:
        f.write(response.content)
    end_img = perf_counter()
    view.total_img(start_img, end_img)


def main(img_urls):
    start = perf_counter()
    for img_url in img_urls:
        thread = threading.Thread(target=get_img, args=(img_url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end = perf_counter()
    view.total(start, end)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        urls = sys.argv[1:]
        view.commandline_execute()
        main(urls)
    else:
        view.usual_execute()
        main(data)
