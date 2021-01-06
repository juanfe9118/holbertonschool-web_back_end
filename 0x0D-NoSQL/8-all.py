#!/usr/bin/env python3
"""
List all documents in a collection
"""
import pymongo


def list_all(mongo_collection):
    """
    function to list all documents in a collection
    """
    if not mongo_collection:
        return []
    docs = mongo_collection.find()
    return [doc for doc in docs]
