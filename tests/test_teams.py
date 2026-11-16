import unittest

from tournament.teams import register_team, list_teams


class TestTeams(unittest.TestCase):

    def setUp(self):
        # Start each test with an empty team list
        self.teams = []

    def test_register_team(self):
        # A valid team should be registered
        team = register_team(self.teams, "Chelsea")

        self.assertEqual(team["id"], "TM001")
        self.assertEqual(team["name"], "Chelsea")
        self.assertEqual(len(self.teams), 1)

    def test_duplicate_team(self):
        # Team names should be unique regardless of capitalization
        register_team(self.teams, "Chelsea")

        with self.assertRaises(ValueError):
            register_team(self.teams, "chelsea")

    def test_blank_team_name(self):
        # Empty names should be rejected
        with self.assertRaises(ValueError):
            register_team(self.teams, " ")

    def test_team_name_too_long(self):
        # Names longer than 30 characters should be rejected
        with self.assertRaises(ValueError):
            register_team(self.teams, "A" * 31)

    def test_list_teams(self):
        # Listing teams should return all registered teams
        register_team(self.teams, "Chelsea")
        register_team(self.teams, "Arsenal")

        result = list_teams(self.teams)

        self.assertEqual(len(result), 2)


if __name__ == "__main__":
    unittest.main()