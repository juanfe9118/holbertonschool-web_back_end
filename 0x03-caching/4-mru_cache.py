#!/usr/bin/python3
'''
MRU caching module
'''
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    '''
    MRU caching class that inherits from BaseCaching and is a caching system
    '''

    def __init__(self):
        '''
        Initialize
        '''
        super().__init__()
        self.keys = []

    def put(self, key, item):
        '''
        Method that puts a new key-value pair to the cache
        '''
        if (key and item):
            self.cache_data[key] = item
            if key in self.keys:
                self.keys.remove(key)
                self.keys.append(key)
            else:
                self.keys.append(key)
            if len(self.keys) > self.MAX_ITEMS:
                idx = self.MAX_ITEMS - 1
                erase = self.keys.pop(idx)
                del self.cache_data[erase]
                print('DISCARD: {}'.format(erase))

    def get(self, key):
        '''
        Method that retrieves the item associated with key
        '''
        if key and key in self.keys:
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache_data[key]
        return None
