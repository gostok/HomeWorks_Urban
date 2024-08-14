import asyncio


async def start_strongman(name, power):
    number = 5
    print(f'Силач {name} начал соревнования.')

    for i in range(1, number + 1):
        delay = 1 / power
        await asyncio.sleep(delay)
        print(f'Силач {name} поднял {i}')

    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    t_1 = asyncio.create_task(start_strongman('Pasha', 3))
    t_2 = asyncio.create_task(start_strongman('Denis', 4))
    t_3 = asyncio.create_task(start_strongman('Apollon', 5))

    await t_1
    await t_2
    await t_3

asyncio.run(start_tournament())