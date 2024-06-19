#!/usr/bin/env python3
""" The basics of async """

import asyncio
import time
wait_random = __import__('0-basic_async_syntax').wait_random

async def task_wait_n(n: int, max_delay: int) -> list:
    a = []
    for i in range(n):
       a.append(await wait_random(max_delay))
    
    for i in range(n - 1):
        swaped = False
        for j in range (n - 1):
            if (a[j] > a[j + 1]):
                swaped = True
                a[j], a[j + 1] = a[j + 1], a[j]
        if not swaped:
            return a
    return a
