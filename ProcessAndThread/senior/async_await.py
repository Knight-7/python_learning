"""
异步I/O - async/await
"""
import asyncio
import math


def num_generator(m, n):
    """指定范围内的数字生成器"""
    yield from range(m, n + 1)


def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    if n % 6 != 1 and n % 6 != 5:
        return False
    sqr_n = int(math.floor(math.sqrt(n)))
    for i in range(5, sqr_n + 1):
        if n % i == 0:
            return False
    return True


async def prime_filter(m, n):
    """素数过滤器"""
    primes = []
    for i in num_generator(m, n):
        if is_prime(i):
            primes.append(i)
            print('Prime=>', i)

        await asyncio.sleep(0.001)
    return tuple(primes)


async def square_mapper(m, n):
    """平方映射器"""
    squares = []
    for i in num_generator(m, n):
        print('Square=>', i * i)
        squares.append(i * i)

        await asyncio.sleep(0.001)
    return squares


def main():
    loop = asyncio.get_event_loop()
    future = asyncio.gather(prime_filter(2, 100), square_mapper(1, 100))
    future.add_done_callback(lambda x: print(x.result()))
    loop.run_until_complete(future)
    loop.close()


if __name__ == '__main__':
    main()