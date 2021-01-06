#!/usr/bin/env python3
"""
Insert a document in a collection based on kwargs
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    insert a document into a collection based on the kwargs
    """
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
