#!/usr/bin/env python3
"""Returns sorted average"""


def top_students(mongo_collection):
    """Sorted average score"""
    pipeline = ([
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

    return mongo_collection.aggregate(pipeline)
