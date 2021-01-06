#!/usr/bin/env python3
"""
Returns top students by average score
"""
import pymongo


def top_students(mongo_collection):
    """
    Function that finds and sorts the students
    """
    return mongo_collection.aggregate([
        {"$project": {"name": "$name",
                      "averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}}
    ])
