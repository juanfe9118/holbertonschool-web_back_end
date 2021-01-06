#!/usr/bin/env python3
"""
Returns a list the list of school having a specific topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    Finds docs by a specific value
    """
    return mongo_collection.find({"topics":  {"$in": [topic]}})
