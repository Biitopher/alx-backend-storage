#!/usr/bin/env python3
"""Inserts new document in collection"""


def insert_school(mongo_collection, **kwargs):
    """Inserts school document"""
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
