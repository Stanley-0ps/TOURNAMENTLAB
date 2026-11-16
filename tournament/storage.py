
import json


def save_tournament(teams, fixtures, file_path):
    # Prepare tournament data for saving
    data = {
        "schema_version": 1,
        "teams": teams,
        "fixtures": fixtures
    }

    # Write the data into a JSON file
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def load_tournament(file_path):
    # Read the saved JSON file
    with open(file_path, "r") as file:
        data = json.load(file)

    # Check that the file uses the supported schema
    if data.get("schema_version") != 1:
        raise ValueError("Unsupported tournament file version.")

    # Return the saved teams and fixtures
    return data["teams"], data["fixtures"]
