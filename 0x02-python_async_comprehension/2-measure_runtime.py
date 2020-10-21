#!/usr/bin/env python3
'''
Module that measures the runtime of async_comprehension while running 4 times
'''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Function that measures the runtime of async_comprehension while running
    4 times in parallel, it returns the elapsed time
    '''
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_time = time.perf_counter() - start
    return total_time
