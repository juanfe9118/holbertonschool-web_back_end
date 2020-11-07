#!/usr/bin/env python3
""" Module of basic API authentication
"""
from flask import request
from typing import TypeVar, List


class Auth():
    '''
    API authentication management class
    '''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''
        Function that returns whether a page requires authentication
        '''
        return False

    def authorization_header(self, request=None) -> str:
        '''
        Function that returns the auth header
        '''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''
        Function that returns the current user information
        '''
        return None
