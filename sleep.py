import random
import asyncio

antall = int(input("Hvor mange tall vil du sortere? "))

liste = list(range(1, antall+1))
random.shuffle(liste)

print("Usortert liste:", liste)

sorted_list = []

sleep_time = 0.01

async def sleep(value):
    await asyncio.sleep(value * sleep_time)
    print(f"{value}")
    sorted_list.append(value)

async def sleep_sport():
    tasks = [sleep(num) for num in liste]
    await asyncio.gather(*tasks) # starter ventetiden på alle tasks samtidig
    print("Sortert liste:", sorted_list)

asyncio.run(sleep_sport())

if sorted_list == sorted(liste):
    print("Listen er sortert!")