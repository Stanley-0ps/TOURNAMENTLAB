import json

try:
    with open("tournament.json", "r") as file:
        data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    print("Could not load tournament.")