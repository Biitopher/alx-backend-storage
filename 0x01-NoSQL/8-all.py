#!/usr/bin/env python3
"""Lists documents in collection"""


def list_all(mongo_collection):
    """All documents in collection list"""
    return mongo_collection.find()
