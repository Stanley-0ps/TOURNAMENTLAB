
def register_team(teams, name):
    # Remove unnecessary spaces around the team name
    name = name.strip()

    # Validate the team name length
    if len(name) < 2 or len(name) > 30:
        raise ValueError("Team name must be between 2 and 30 characters.")

    # Check for duplicate names, ignoring case and extra spaces
    for team in teams:
        if team["name"].casefold() == name.casefold():
            raise ValueError("This team is already registered.")

    # Generate a unique team ID
    team_id = f"TM{len(teams) + 1:03d}"

    # Create the team record
    new_team = {
        "id": team_id,
        "name": name
    }

    # Add the new team to the team list
    teams.append(new_team)

    # Return the newly registered team
    return new_team


def list_teams(teams):
    # Return all registered teams
    return teams
