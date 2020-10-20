#!/usr/bin/env python3
'''
Module that takes an integer and waits for a random delay between 0 and the
integer and returns the delay time in float
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Function that takes an integer and waits for a random delay between 0 and
    the integer

    @max_delay: the integer taken in as parameter
    Return: the waited time in float
    """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
