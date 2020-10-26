#!/usr/bin/python3
'''
Basic caching module
'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''
    Basic caching class that inherits from BaseCaching
    '''

    def put(self, key, item):
        '''
        Method that put a new key, value pair to the cache
        '''
        if (key and item):
            self.cache_data[key] = item

    def get(self, key):
        '''
        Method that retrieves the item associated with key
        '''
        if key:
            for k in self.cache_data.keys():
                if key == k:
                    return self.cache_data.get(key)
        return None
