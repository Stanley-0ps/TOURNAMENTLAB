import unittest

from tournament.teams import register_team
from tournament.fixtures import generate_fixtures, record_score
from tournament.standings import calculate_standings


class TestStandings(unittest.TestCase):

    def setUp(self):
        # Create four teams and their fixtures
        self.teams = []

        for name in ["Chelsea", "Arsenal", "Man U", "Man City"]:
            register_team(self.teams, name)

        self.fixtures = generate_fixtures(self.teams)

    def test_win_awards_three_points(self):
        # Chelsea beats Arsenal 2-1
        record_score(self.fixtures, "M001", 2, 1)

        standings = calculate_standings(self.teams, self.fixtures)

        chelsea = next(
            team for team in standings
            if team["team_name"] == "Chelsea"
        )

        self.assertEqual(chelsea["points"], 3)
        self.assertEqual(chelsea["wins"], 1)

    def test_draw_awards_one_point_each(self):
        # Chelsea and Arsenal draw 1-1
        record_score(self.fixtures, "M001", 1, 1)

        standings = calculate_standings(self.teams, self.fixtures)

        for team in standings[:2]:
            self.assertEqual(team["points"], 1)
            self.assertEqual(team["draws"], 1)

    def test_goal_difference(self):
        # Chelsea wins 3-1
        record_score(self.fixtures, "M001", 3, 1)

        standings = calculate_standings(self.teams, self.fixtures)

        chelsea = standings[0]

        self.assertEqual(chelsea["goals_for"], 3)
        self.assertEqual(chelsea["goals_against"], 1)
        self.assertEqual(chelsea["goal_difference"], 2)

    def test_standings_ignore_pending_fixtures(self):
        # No results have been recorded
        standings = calculate_standings(self.teams, self.fixtures)

        for team in standings:
            self.assertEqual(team["played"], 0)
            self.assertEqual(team["points"], 0)

    def test_alphabetical_tiebreaker(self):
        # With no played matches, all teams have equal points
        standings = calculate_standings(self.teams, self.fixtures)

        # Teams should be sorted alphabetically
        team_names = [team["team_name"] for team in standings]

        self.assertEqual(
            team_names,
            ["Arsenal", "Chelsea", "Man City", "Man U"]
        )

    def test_standings_update_after_new_result(self):
        # Record the first match
        record_score(self.fixtures, "M001", 2, 1)

        first_standings = calculate_standings(
            self.teams, self.fixtures
        )

        # Record another match
        record_score(self.fixtures, "M002", 0, 3)

        second_standings = calculate_standings(
            self.teams, self.fixtures
        )

        # The standings should change after the second result
        self.assertNotEqual(first_standings, second_standings)

if __name__ == "__main__":
    unittest.main()