
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
