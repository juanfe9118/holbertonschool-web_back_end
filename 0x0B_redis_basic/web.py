#!/usr/bin/env python3
'''Module for Implementing an expiring web cache and tracker
'''

import redis
import requests
from typing import Callable
from functools import wraps

rd = redis.Redis()


def count_requests(method: Callable) -> Callable:
    '''Decorator for how many times a request has been made
    '''

    @wraps(method)
    def wrapper(url):
        ''' Wrapper that makes the decorator work '''
        rd.incr(f"count:{url}")
        cached_html = rd.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')

        html = method(url)
        rd.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    '''Method that obtains the HTML content of a particular URL and
    returns it.
    '''
    req = requests.get(url)
    return req.text
