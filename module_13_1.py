import asyncio as asc

DEFAULT_TIME_LIFTING = 5


async def start_strongman(name,
                          power):
    print(f'Силач {name} начал соревнования.')
    for i in range(0, 5):
        await asc.sleep(DEFAULT_TIME_LIFTING / power)
        print(f'Силач {name} поднял {i + 1}')

    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task1 = asc.create_task(start_strongman('Силач Олежа', 1))
    task2 = asc.create_task(start_strongman('Слабач Паша', 5))
    task3 = asc.create_task(start_strongman('Нюхач Александр Владимирович', 3))
    await task1
    await task2
    await task3


asc.run(start_tournament())
