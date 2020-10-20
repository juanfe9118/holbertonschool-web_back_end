#!/usr/bin/env python3
'''
Module that imports `wait_random` and executes it n times asynchronously
'''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Function that calls wait_random and spawns it n times asynchronously

    @n: the amount of times wait_random will be called
    @max_delay: the max delay passed to wait_random
    Return: the list of waited times in float
    '''
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    time_list = []
    for task in asyncio.as_completed(tasks):
        time: float = await task
        time_list.append(time)
    return time_list
