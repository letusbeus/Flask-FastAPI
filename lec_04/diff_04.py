import asyncio
import aiohttp
import time

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://mail.ru/',
        ]


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            filename = 'asyncio_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
            with open(filename, "w", encoding='utf-8') as f:
                f.write(text)
            print(f"Downloaded {url} in {time.time() - start_time: .2f} seconds")


async def main():
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


start_time = time.time()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    # To avoid "DeprecationWarning: There is no current event loop" use the following code instead of 2 lines above:
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # loop.run_until_complete(main())
