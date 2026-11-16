import json

try:
    with open("tournament.json", "r") as file:
        data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    print("Could not load tournament.")

from tournament.cli import run_cli

# Start the tournament application
if __name__ == "__main__":
    run_cli()