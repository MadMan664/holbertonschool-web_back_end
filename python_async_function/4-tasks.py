#!/usr/bin/env python3
"""Module that runs task_wait_random several times concurrently."""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Create n tasks and return the list of delays in ascending order."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []
    for finished in asyncio.as_completed(tasks):
        delays.append(await finished)
    return delays
