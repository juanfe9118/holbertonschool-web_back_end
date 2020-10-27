#!/usr/bin/python3
'''
LFU caching module
'''

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    '''
    LFU caching class that inherits from BaseCaching and is a caching system
    '''

    def __init__(self):
        '''
        Initialize
        '''
        super().__init__()
        self.keys = []
        self.counter = {}

    def put(self, key, item):
        '''
        Method that puts a new key-value pair to the cache
        '''

        if key is not None and item is not None:
            if (len(self.keys) == BaseCaching.MAX_ITEMS and
                    key not in self.keys):
                discard = self.keys.pop(self.keys.index(self.findLFU()))
                del self.cache_data[discard]
                del self.counter[discard]
                print('DISCARD: {:s}'.format(discard))
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
                self.counter[key] = 0
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
                self.counter[key] += 1

    def get(self, key):
        '''
        Method that retrieves the item associated with key
        '''
        if key is not None and key in self.cache_data:
            self.keys.append(self.keys.pop(self.keys.index(key)))
            self.counter[key] += 1
            return self.cache_data[key]
        return None

    def findLFU(self):
        '''
        Method that returns the last frequently used element
        '''
        items = list(self.counter.items())
        freqs = [item[1] for item in items]
        least = min(freqs)

        lfus = [item[0] for item in items if item[1] == least]
        for key in self.keys:
            if key in lfus:
                return key
