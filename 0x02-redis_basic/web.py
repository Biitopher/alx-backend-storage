#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""
import requests
import redis
from functools import wraps
from typing import Callable


redis_client = redis.Redis()


def cache_with_count(method: Callable) -> Callable:
    """Decorator to cache function result with count and expiration time"""
    @wraps(method)
    def decorator(url) -> str:
        """The wrapper function"""
        redis_client.incr(f'count:{url}')
        result = redis_client.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_client.setex(f'result:{url}', 10, result)
        return result
    return decorator


@cache_with_count
def get_page(url: str) -> str:
    """Fetches the HTML content of a URL using requests"""
    response = requests.get(url)
    return response.text
