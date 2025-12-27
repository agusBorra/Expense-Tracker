import json
import os

def read_json():
    if not os.path.isfile('expenses.json'):
        with open('expenses.json', 'w') as f:
            json.dump([],f)
    with open('expenses.json', 'r') as f:
            expenses = json.load(f)
    return expenses

def write_Json(expenses):
    with open('expenses.json', 'w') as f:
            json.dump(expenses, f)