#!/usr/bin/env python3
"""Module that collects random numbers with an async comprehension."""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return ten random numbers collected with an async comprehension."""
    return [number async for number in async_generator()]
