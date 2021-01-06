#!/usr/bin/env python3
"""
Change school topics based on name
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    Function that updates a document with a specific name
    """
    return mongo_collection.update_many({
        "name": name
    },
        {
            "$set": {
                "topics": topics
            }
    })
