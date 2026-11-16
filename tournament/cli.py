from tournament.simulation import simulate_fixtures
from tournament.standings import calculate_standings
from tournament.storage import save_tournament, load_tournament
from tournament.teams import register_team, list_teams
from tournament.fixtures import (
    generate_fixtures,
    list_fixtures,
    record_score
)


def show_menu():
    # Display the available tournament actions
    print("\n===== TOURNAMENT LAB =====")
    print("1. Register team")
    print("2. List teams")
    print("3. Generate fixtures")
    print("4. List fixtures")
    print("5. Record match result")
    print("6. Show standings")
    print("7. Save tournament")
    print("8. Load tournament")
    print("9. Show champion")
    print("0. Exit")
    print("10. Run demo simulation")


def run_cli():
    # Keep tournament data in memory while the program runs
    teams = []
    fixtures = []

    while True:
        show_menu()

        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        elif choice == "1":
            # Prevent adding teams after fixtures have been generated
            if fixtures:
                print("Cannot register teams after fixtures have been generated.")
                continue

            # Ask the user for a team name
            name = input("Enter team name: ")

            try:
                # Register the team
                team = register_team(teams, name)

                print(f"Team registered successfully: {team['name']}")
                print(f"Team ID: {team['id']}")

            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "2":
            # Get all registered teams
            registered_teams = list_teams(teams)

            if not registered_teams:
                print("No teams have been registered yet.")
            else:
                print("\n===== REGISTERED TEAMS =====")

                for team in registered_teams:
                    print(f"{team['id']} - {team['name']}")

        elif choice == "3":
            try:
                # Prevent generating the same tournament schedule twice
                if fixtures:
                    print("Fixtures have already been generated.")
                else:
                    # Generate fixtures from registered teams
                    fixtures = generate_fixtures(teams)

                    print(f"Successfully generated {len(fixtures)} fixtures.")

            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "4":
            # Get all tournament fixtures
            all_fixtures = list_fixtures(fixtures)

            if not all_fixtures:
                print("No fixtures available. Generate fixtures first.")
            else:
                # Create a lookup table for team IDs and names
                team_names = {
                    team["id"]: team["name"]
                    for team in teams
                }

                print("\n===== TOURNAMENT FIXTURES =====")

                for fixture in all_fixtures:
                    home = team_names[fixture["home_id"]]
                    away = team_names[fixture["away_id"]]

                    if fixture["status"] == "played":
                        result = (
                            f"{fixture['home_score']} - "
                            f"{fixture['away_score']}"
                        )
                    else:
                        result = "Pending"

                    print(
                        f"{fixture['id']}: {home} vs {away} | "
                        f"{result} | {fixture['status']}"
                    )

        elif choice == "5":
            if not fixtures:
                print("Generate fixtures first.")
                continue

            try:
                # Ask for the fixture ID and scores
                fixture_id = input("Enter fixture ID: ").strip()
                home_score = int(input("Enter home team score: "))
                away_score = int(input("Enter away team score: "))

                # Record the match result
                result = record_score(
                    fixtures,
                    fixture_id,
                    home_score,
                    away_score
                )

                print(
                    f"Result recorded: {result['home_score']} - "
                    f"{result['away_score']}"
                )

            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "6":
            if not teams:
                print("Register teams first.")
                continue

            # Calculate standings from recorded match results
            standings = calculate_standings(teams, fixtures)

            print("\n===== TOURNAMENT STANDINGS =====")
            print(
                f"{'Team':<18} {'P':<3} {'W':<3} {'D':<3} "
                f"{'L':<3} {'GF':<4} {'GA':<4} {'GD':<4} {'Pts':<4}"
            )

            # Display each team's statistics
            for team in standings:
                print(
                    f"{team['team_name']:<18} "
                    f"{team['played']:<3} "
                    f"{team['wins']:<3} "
                    f"{team['draws']:<3} "
                    f"{team['losses']:<3} "
                    f"{team['goals_for']:<4} "
                    f"{team['goals_against']:<4} "
                    f"{team['goal_difference']:<4} "
                    f"{team['points']:<4}"
                )

        elif choice == "7":
            try:
                # Save the current tournament data
                save_tournament(teams, fixtures, "tournament.json")

                print("Tournament saved successfully.")

            except (OSError, TypeError, ValueError) as error:
                print(f"Error saving tournament: {error}")

        elif choice == "8":
            try:
                # Load into temporary variables first
                loaded_teams, loaded_fixtures = load_tournament(
                    "tournament.json"
                )

                # Replace current data only after successful validation
                teams = loaded_teams
                fixtures = loaded_fixtures

                print("Tournament loaded successfully.")

            except FileNotFoundError:
                print("Error: No saved tournament file found.")

            except (OSError, ValueError) as error:
                print(f"Error loading tournament: {error}")

        elif choice == "9":
            if not fixtures:
                print("Generate fixtures first.")
                continue

            # Check whether every fixture has been completed
            pending_fixtures = [
                fixture for fixture in fixtures
                if fixture["status"] != "played"
            ]

            if pending_fixtures:
                print("Tournament is still in progress.")
                print(f"Remaining fixtures: {len(pending_fixtures)}")

            else:
                # Calculate the final standings
                standings = calculate_standings(teams, fixtures)

                # The first team in the sorted table is the champion
                champion = standings[0]

                print("\n===== TOURNAMENT CHAMPION =====")
                print(f"Champion: {champion['team_name']}")
                print(f"Points: {champion['points']}")
                print(f"Goal Difference: {champion['goal_difference']}")

        elif choice == "10":
            if not fixtures:
                print("Generate fixtures first.")
                continue

            try:
                # Ask the user for a seed
                seed = int(input("Enter a random seed: "))

                # Simulate fixtures without changing actual records
                simulated_fixtures = simulate_fixtures(fixtures, seed)

                # Calculate standings using simulated results
                simulated_standings = calculate_standings(
                    teams, simulated_fixtures
                )

                print("\n===== DEMO SIMULATION RESULTS =====")

                for fixture in simulated_fixtures:
                    team_names = {
                        team["id"]: team["name"]
                        for team in teams
                    }

                    print(
                        f"{fixture['id']}: "
                        f"{team_names[fixture['home_id']]} "
                        f"{fixture['home_score']} - "
                        f"{fixture['away_score']} "
                        f"{team_names[fixture['away_id']]}"
                    )

                print("\n===== SIMULATED STANDINGS =====")

                for position, team in enumerate(simulated_standings, start=1):
                    print(
                        f"{position}. {team['team_name']} "
                        f"- {team['points']} points"
                    )

                print("\nDemo simulation completed.")
                print("Your actual tournament records remain unchanged.")

            except ValueError as error:
                print(f"Error: {error}")

        else:
            print("Invalid option. Try again.")