#!/usr/bin/env python3
""" The basics of async """

import asyncio
import random
async def wait_random(max_delay: int  = 10, ) -> float :
    res = random.uniform(0 ,max_delay)
    return res

if __name__ == "__main__":
    print(asyncio.run(wait_random(5)))