from fastapi import FastAPI
from asyncio import run
from requestApi import getNumbers

app = FastAPI()

def quick_sort(sequence):
  length = len(sequence)
  if length <= 1:
    return sequence
  else:
    pivot = sequence.pop()

  items_greater = []
  items_lower = []

  for item in sequence:
    if item > pivot:
      items_greater.append(item)
    
    else:
      items_lower.append(item)

  return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

@app.get("/")
def read_root():
  return quick_sort(run(getNumbers()))
