#!/usr/bin/env python3
'''
Module that imports async generator and creates a comprehension of it
'''
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    Function that comprehenses over async_generator and returns the list of
    floats
    '''
    return [num async for num in async_generator()]
