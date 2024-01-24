#!/usr/bin/env python3
"""Writing strings to Redis"""
import uuid
import redis
from typing import Union


class Cache:
    def __init__(self, host='localhost', port=6379, db=0):
        """Initialize"""
        self._redis = redis.Redis(host=host, port=port, db=db)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """defines storage"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
