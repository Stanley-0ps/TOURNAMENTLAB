
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

    # Validate the main data structure
    if not isinstance(data, dict):
        raise ValueError("Invalid tournament data.")

    if data.get("schema_version") != 1:
        raise ValueError("Unsupported tournament file version.")

    teams = data.get("teams")
    fixtures = data.get("fixtures")

    if not isinstance(teams, list) or not isinstance(fixtures, list):
        raise ValueError("Teams and fixtures must be lists.")

    # Validate teams
    team_ids = set()
    team_names = set()

    for team in teams:
        if not isinstance(team, dict):
            raise ValueError("Invalid team record.")

        team_id = team.get("id")
        name = team.get("name")

        if not isinstance(team_id, str) or not isinstance(name, str):
            raise ValueError("Invalid team ID or name.")

        if not 2 <= len(name.strip()) <= 30 or name != name.strip():
            raise ValueError("Invalid team name.")

        if team_id in team_ids:
            raise ValueError("Duplicate team ID.")

        if name.casefold() in team_names:
            raise ValueError("Duplicate team name.")

        team_ids.add(team_id)
        team_names.add(name.casefold())

    # Validate fixtures
    fixture_ids = set()
    team_pairs = set()

    for fixture in fixtures:
        if not isinstance(fixture, dict):
            raise ValueError("Invalid fixture record.")

        fixture_id = fixture.get("id")
        home_id = fixture.get("home_id")
        away_id = fixture.get("away_id")
        status = fixture.get("status")
        home_score = fixture.get("home_score")
        away_score = fixture.get("away_score")

        if not all(isinstance(value, str) for value in
                   [fixture_id, home_id, away_id]):
            raise ValueError("Invalid fixture IDs.")

        if fixture_id in fixture_ids:
            raise ValueError("Duplicate fixture ID.")

        if home_id not in team_ids or away_id not in team_ids:
            raise ValueError("Fixture references an unknown team.")

        if home_id == away_id:
            raise ValueError("A team cannot play itself.")

        pair = frozenset([home_id, away_id])

        if pair in team_pairs:
            raise ValueError("Duplicate team matchup.")

        fixture_ids.add(fixture_id)
        team_pairs.add(pair)

        if status == "pending":
            if home_score is not None or away_score is not None:
                raise ValueError("Pending fixtures cannot have scores.")

        elif status == "played":
            if (
                type(home_score) is not int or home_score < 0
                or type(away_score) is not int or away_score < 0
            ):
                raise ValueError("Invalid match scores.")

        else:
            raise ValueError("Invalid fixture status.")

    # Return data only after every check passes
    return teams, fixtures
