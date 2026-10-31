#!/usr/bin/env python3
"""Module with an asynchronous generator of random numbers."""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yield a random number between 0 and 10, ten times, one second apart."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
