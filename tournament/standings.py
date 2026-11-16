
def calculate_standings(teams, fixtures):
    # Create an initial statistics record for every team
    standings = {}

    for team in teams:
        standings[team["id"]] = {
            "team_id": team["id"],
            "team_name": team["name"],
            "played": 0,
            "wins": 0,
            "draws": 0,
            "losses": 0,
            "goals_for": 0,
            "goals_against": 0,
            "goal_difference": 0,
            "points": 0
        }

    # Process only fixtures that have been played
    for fixture in fixtures:
        if fixture["status"] != "played":
            continue

        home = standings[fixture["home_id"]]
        away = standings[fixture["away_id"]]

        home_score = fixture["home_score"]
        away_score = fixture["away_score"]

        # Update matches played and goals
        home["played"] += 1
        away["played"] += 1

        home["goals_for"] += home_score
        home["goals_against"] += away_score

        away["goals_for"] += away_score
        away["goals_against"] += home_score

        # Award points based on the result
        if home_score > away_score:
            home["wins"] += 1
            away["losses"] += 1
            home["points"] += 3

        elif home_score < away_score:
            away["wins"] += 1
            home["losses"] += 1
            away["points"] += 3

        else:
            home["draws"] += 1
            away["draws"] += 1
            home["points"] += 1
            away["points"] += 1

    # Calculate each team's goal difference
    for team in standings.values():
        team["goal_difference"] = (
            team["goals_for"] - team["goals_against"]
        )

    # Sort by points, goal difference, goals scored, then team name
    sorted_standings = sorted(
        standings.values(),
        key=lambda team: (
            -team["points"],
            -team["goal_difference"],
            -team["goals_for"],
            team["team_name"].casefold()
        )
    )

    return sorted_standings
