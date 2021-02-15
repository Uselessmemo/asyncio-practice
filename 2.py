import asyncio
import requests
import aiohttp
import time

urls = ['https://www.google.com/', 'https://yandex.ru/', 'https://www.python.org/']

class CustomException(Exception):
    pass

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp.status)

loop = asyncio.get_event_loop()
tasks = [fetch_url(url) for url in urls]
start = time.time()
loop.run_until_complete(asyncio.wait(tasks))
print(f'{time.time() - start} sec...')
