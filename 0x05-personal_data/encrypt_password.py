#!/usr/bin/env python3
'''
Module that encrypts passwords and checks if they are valid.
'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''
    Function that hashes a password for added security.
    '''
    encoded_password = password.encode()
    hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())

    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''
    Function that checks if a password matches a hashed password.
    '''
    valid = False
    encoded_password = password.encode()
    if bcrypt.checkpw(encoded_password, hashed_password):
        valid = True
    return valid
