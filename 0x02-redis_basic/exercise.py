#!/usr/bin/env python3
"""Writing strings to Redis"""
import uuid
import redis
from typing import Union, Optional, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Decorator for Cache class methods to track call count"""
    @wraps(method)
    def wrapper(self: Any, *args, **kwargs) -> str:
        """ Wraps called method adds call count redis before execution""" 
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """Counts how many times cache class are called"""

    @wraps(method)
    def wrapper(self: Any, *args, **kwargs) -> str:
        """Wrapped functiion"""
        key = f'{method.__qualname__}:inputs', str(args)
        result = method(self, *args, **kwargs)
        self._redis.rpush(key)
        self._redis.rpush(f'{method.__qualname__}:outputs', output)
        return result

    return wrapper

class Cache:
    def __init__(self, host='localhost', port=6379, db=0):
        """Initialize"""
        self._redis = redis.Redis(host=host, port=port, db=db)
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """defines storage"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> (
            Union[str, bytes, int, float, None]):
        """Get"""
        data = self._redis.get(key)
        if data is not None:
            return fn(data) if fn else data
        return None

    def get_str(self, key: str) -> Union[str, None]:
        """Get string"""
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Union[int, None]:
        """Get int"""
        return self.get(key, fn=int)
