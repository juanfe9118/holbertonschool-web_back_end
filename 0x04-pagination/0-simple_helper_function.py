#!/usr/bin/env python3
'''
Module for simple helper function to pagination
'''


def index_range(page: int, page_size: int) -> tuple:
    '''
    Simple helper function to pagination

    @page: the page number
    @page_size: the amount of results per page
    Return: a tuple of the starting and end indexes for that page
    '''
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
