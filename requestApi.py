from asyncio import gather
from aiohttp import ClientSession

url = 'http://challenge.dienekes.com.br/api/numbers?page={}'
api_results = []

def getTasks(session):
  tasks = []
  for i in range(1, 1000):
    tasks.append(session.get(url.format(i), ssl=False))
  return tasks

async def getNumbers():
  async with ClientSession() as session:
    tasks = getTasks(session)
    responses = await gather(*tasks)
    for response in responses:
      try:
        numbers = await response.json()
        api_results.extend(numbers['numbers'])
      except KeyError:
        False
  return api_results