
from tournament.teams import register_team, list_teams

teams = []

# Register two teams
register_team(teams, "Red Comets")
register_team(teams, "Blue Dragons")

# Display registered teams
print(list_teams(teams))

# Try registering a duplicate team
try:
    register_team(teams, " red comets ")
except ValueError as error:
    print(f"Error: {error}")