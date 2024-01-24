#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""
import requests
import redis
from functools import wraps

redis_client = redis.Redis()


def cache_with_count(url, expiration=10):
    """Decorator to cache function result with count and expiration time"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            count_key = f"count:{url}"

            redis_client.incr(count_key)

            result_key = f"result:{url}"

            cached_result = redis_client.get(result_key)
            if cached_result is not None:
                return cached_result.decode('utf-8')

            result = func(*args, **kwargs)

            redis_client.setex(result_key, expiration, result)

            return result
        return wrapper
    return decorator

@cache_with_count(url="http://slowwly.robertomurray.co.uk/delay/1000/url/https://www.example.com")
def get_page(url: str) -> str:
    """Fetches the HTML content of a URL using requests"""
    response = requests.get(url)
    return response.text

