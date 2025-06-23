from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Create the FastAPI app
app = FastAPI()

# Define request model using Pydantic
class NumberList(BaseModel):
    numbers: List[int]

# Radix Sort Function
def radix_sort(arr: List[int]) -> List[int]:
    if not arr:
        return arr

    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

# Helper function for counting sort used in radix sort
def counting_sort(arr: List[int], exp: int):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

# Route for sorting
@app.post("/sort/")
def sort_numbers(data: NumberList):
    try:
        sorted_list = radix_sort(data.numbers.copy())
        return {"original": data.numbers, "sorted": sorted_list}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

#[170, 45, 75, 90, 802, 24, 2, 66]