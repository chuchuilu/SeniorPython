"""
# 单线程阻塞任务
#
# import asyncio
#
#
# async def main():
#     print("start1----->")
#     await asyncio.sleep(2)
#     print("stop1------>")
#
#
# async def main1():
#     print("start----->")
#     await asyncio.sleep(2)
#     print("stop------>")
#
# coro = main()
# asyncio.run(main())
# asyncio.run(main1())

"""
import asyncio
import time

"""
coroutine ----> task ----> eventloop调度
"""
async def say_delay(delay, what):
    await asyncio.sleep(delay)
    return f"{what} -- {delay}"


async def main():
    print(f"start--------------------->{time.strftime('%X')}")

    ref = await asyncio.gather(
        say_delay(1, "start"),
        say_delay(2, "stop")
    )

    print(ref)
    print(f"stop---------------------->{time.strftime('%X')}")

asyncio.run(main())
