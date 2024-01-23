#!/usr/bin/env python3
"""Returns sorted average"""


def top_students(mongo_collection):
    """Sorted average score"""
    return mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$scores.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ])
