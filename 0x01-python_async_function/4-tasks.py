#!/usr/bin/env python3
'''
Module that does the same as wait_n but using task_wait_random instead
'''
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Function that calls wait_random and spawns it n times asynchronously

    @n: the amount of times wait_random will be called
    @max_delay: the max delay passed to wait_random
    Return: the list of waited times in float
    '''
    time_list = []
    for _ in range(n):
        time_list.append(task_wait_random(max_delay))
    return [await time for time in asyncio.as_completed(time_list)]
