from fastapi import FastAPI, HTTPException
import json
from typing import List

app = FastAPI()

# Load data from data.json
try:
    with open("data.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    data = []  # Use an empty list if file is missing
    print("Warning: 'data.json' file not found.")
except json.JSONDecodeError:
    data = []  # Use an empty list if file contains invalid JSON
    print("Warning: 'data.json' contains invalid JSON.")


@app.get("/", response_model=List[dict])
async def read_data():
    """
    Return all available data.
    """
    if not data:
        raise HTTPException(status_code=404, detail="Data not available")
    return data


@app.get("/{guid}", response_model=dict)
async def read_data_by_guid(guid: str):
    """
    Return a specific item by its GUID.
    """
    for item in data:
        if item.get("guid") == guid:
            return item
    raise HTTPException(status_code=404, detail="Item not found")
