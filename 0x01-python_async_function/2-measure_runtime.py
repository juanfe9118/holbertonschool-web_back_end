#!/usr/bin/env python3
'''
Module that measures the total execution time for wait_n
'''
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    Function that measures the execution time of wait_n

    @n: amount of times to execute wait_random
    @max_delay: the max delay passed to wait_random
    Return: the total execution time divided by n
    '''
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start
    return total_time / n
