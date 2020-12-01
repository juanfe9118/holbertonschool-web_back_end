#!/usr/bin/env python3
'''Basic Redis Module'''
import redis
from uuid import uuid4
from typing import Union, Callable, Optional


class Cache:
    '''Redis caching class'''

    def __init__(self):
        '''Constructor method'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        Method that stores a new key value pair in the redis client and
        returns the key
        '''
        uni_key = str(uuid4())
        self._redis.set(uni_key, data)
        return uni_key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        '''
        Method that gets the value for a specified key and returns it after
        optionally passing it through a convertion function fn
        '''
        val = self._redis.get(key)
        if fn:
            val = fn(val)
        return val

    def get_str(self, key: str) -> str:
        '''Parameterizes a value from the redis client to str'''
        val = self._redis.get(key)
        return val.decode('utf-8')

    def get_int(self, key: str) -> int:
        '''Parameterizes a value from the redis client to int'''
        val = self._redis.get(key)
        try:
            val = int(val.decode('utf-8'))
        except Exception:
            val = 0
        return val
