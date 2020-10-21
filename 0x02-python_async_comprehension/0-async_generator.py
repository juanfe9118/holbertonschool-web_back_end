#!/usr/bin/env python3
'''
Module that creates a coroutine that yields a random number
'''
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    Function that creates a generator that yields a random number between 0-10
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
