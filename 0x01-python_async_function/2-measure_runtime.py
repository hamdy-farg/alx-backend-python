#!/usr/bin/env python3
""" The basics of async """

import asyncio
import time 

def measure_time(n: int, max_delay: int) -> float:
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - s
    return elapsed 

if __name__ == "__main__":
    wait_n = __import__('1-concurrent_coroutines').wait_n
    print(measure_time(5, 9))
