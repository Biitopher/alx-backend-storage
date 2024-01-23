#!/usr/bin/env python3
"""Returns sorted average"""


def top_students(mongo_collection):
    """Sorted average score"""
    pipeline = [
        {
            "$project": {
                "_id": 1,
                "name": 1,
                "scores": 1,
                "averageScore": {"$avg": "$scores.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]

    result = mongo_collection.aggregate(pipeline)

    return list(result)
