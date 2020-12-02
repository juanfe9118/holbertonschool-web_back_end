#!/usr/bin/env python3
'''Basic Redis Module'''
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''Decorator to count how many times methods of the Cache class are
    called
    '''
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        '''Wrapper that makes the decorator work'''
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    '''Decorator to store the list of inputs and outputs of the methods of the
    Cache class'''
    @wraps(method)
    def wrapper(self, *args, **kwds):
        '''Wrapper that makes the decorator work'''
        inputs = str(args)
        self._redis.rpush(method.__qualname__ + ':inputs', inputs)

        outputs = str(method(self, *args, **kwds))
        self._redis.rpush(method.__qualname__ + ':outputs', outputs)
        return outputs
    return wrapper


def replay(func: Callable):
    """Display the history of calls of a particular function"""
    r = redis.Redis()
    func_name = func.__qualname__
    n_calls = r.get(func_name)
    try:
        n_calls = n_calls.decode('utf-8')
    except Exception:
        n_calls = 0
    print(f'{func_name} was called {n_calls} times:')

    ins = r.lrange(func_name + ":inputs", 0, -1)
    outs = r.lrange(func_name + ":outputs", 0, -1)

    for i, o in zip(ins, outs):
        try:
            i = i.decode('utf-8')
        except Exception:
            i = ""
        try:
            o = o.decode('utf-8')
        except Exception:
            o = ""

        print(f'{func_name}(*{i}) -> {o}')


class Cache:
    '''Redis caching class'''

    def __init__(self):
        '''Constructor method'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
