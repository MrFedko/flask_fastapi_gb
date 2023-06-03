import asyncio
from timer import timer, arr


summa = 0


async def sum_array_async(arr, start_idx, end_idx):
    local_sum = 0
    for i in range(start_idx, end_idx):
        local_sum += arr[i]
    return local_sum


@timer
async def main():
    global summa
    tasks = []
    num_tasks = 4
    for i in range(num_tasks):
        start_idx = i * len(arr) // num_tasks
        end_idx = (i + 1) * len(arr) // num_tasks
        task = asyncio.create_task(sum_array_async(arr, start_idx, end_idx))
        tasks.append(task)
    for task in tasks:
        summa += await task
    return summa


if __name__ == '__main__':
    asyncio.run(main())
    print(summa)
