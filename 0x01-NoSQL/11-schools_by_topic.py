#!/usr/bin/env python3
"""List of school with specific topic"""


def schools_by_topic(mongo_collection, topic):
    """defines specific topic"""
    query = {"topics": topic}
    return mongo_collection.find(query)
