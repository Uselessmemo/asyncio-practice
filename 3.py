# Hello world
import asyncio
import time

async def hello_world():
    print('Hello')
    await asyncio.sleep(1)
    print('world!')

async def hello_you_too():
    print('Hello')
    await asyncio.sleep(1)
    print('you too!')

async def main():
    await asyncio.gather(hello_world(), hello_you_too())

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(f'{time.time() - start} sec...')