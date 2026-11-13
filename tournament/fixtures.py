
def generate_fixtures(teams):
    # A tournament requires between 4 and 8 teams
    if len(teams) < 4 or len(teams) > 8:
        raise ValueError("A tournament requires 4 to 8 teams.")

    fixtures = []

    # Compare each team with the teams after it
    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):

            fixture = {
                "id": f"M{len(fixtures) + 1:03d}",
                "home_id": teams[i]["id"],
                "away_id": teams[j]["id"],
                "status": "pending",
                "home_score": None,
                "away_score": None
            }

            fixtures.append(fixture)

    return fixtures


def record_score(fixtures, fixture_id, home_score, away_score):
    # Find the requested fixture
    fixture = None

    for match in fixtures:
        if match["id"] == fixture_id:
            fixture = match
            break

    # Reject unknown fixture IDs
    if fixture is None:
        raise ValueError("Fixture not found.")

    # A completed fixture cannot receive another result
    if fixture["status"] == "played":
        raise ValueError("This fixture has already been played.")

    # Scores must be integers, not booleans, and cannot be negative
    if (
        type(home_score) is not int or home_score < 0
        or type(away_score) is not int or away_score < 0
    ):
        raise ValueError("Scores must be non-negative integers.")

    # Update both scores and status
    fixture["home_score"] = home_score
    fixture["away_score"] = away_score
    fixture["status"] = "played"

    return fixture
