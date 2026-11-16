import unittest

from tournament.teams import register_team
from tournament.fixtures import generate_fixtures, record_score


class TestFixtures(unittest.TestCase):

    def setUp(self):
        # Create four fresh teams before each test
        self.teams = []

        for name in ["Chelsea", "Arsenal", "Man U", "Man City"]:
            register_team(self.teams, name)

        self.fixtures = generate_fixtures(self.teams)

    def test_generate_six_fixtures(self):
        # Four teams should produce six unique fixtures
        self.assertEqual(len(self.fixtures), 6)

    def test_no_team_plays_itself(self):
        # A team must never play against itself
        for fixture in self.fixtures:
            self.assertNotEqual(
                fixture["home_id"],
                fixture["away_id"]
            )

    def test_no_duplicate_matchups(self):
        # Each pair of teams should meet only once
        matchups = set()

        for fixture in self.fixtures:
            pair = frozenset([
                fixture["home_id"],
                fixture["away_id"]
            ])

            self.assertNotIn(pair, matchups)
            matchups.add(pair)

    def test_reject_fewer_than_four_teams(self):
        # Three teams should not be enough
        with self.assertRaises(ValueError):
            generate_fixtures(self.teams[:3])

    def test_record_match_result(self):
        # A valid score should update the fixture
        result = record_score(self.fixtures, "M001", 2, 1)

        self.assertEqual(result["home_score"], 2)
        self.assertEqual(result["away_score"], 1)
        self.assertEqual(result["status"], "played")

    def test_reject_negative_score(self):
        # Negative scores should be rejected
        with self.assertRaises(ValueError):
            record_score(self.fixtures, "M001", 2, -1)

        # The rejected result must not change the fixture
        self.assertEqual(self.fixtures[0]["status"], "pending")
        self.assertIsNone(self.fixtures[0]["home_score"])

    def test_reject_unknown_fixture(self):
        # Unknown fixture IDs should be rejected
        with self.assertRaises(ValueError):
            record_score(self.fixtures, "M999", 2, 1)

    def test_reject_duplicate_result(self):
        # A fixture cannot be recorded twice
        record_score(self.fixtures, "M001", 2, 1)

        with self.assertRaises(ValueError):
            record_score(self.fixtures, "M001", 3, 1)

    def test_reject_float_score(self):
        # Scores must be whole numbers
        with self.assertRaises(ValueError):
            record_score(self.fixtures, "M001", 2.5, 1)

        # The fixture must remain unchanged
        self.assertEqual(self.fixtures[0]["status"], "pending")


    def test_reject_boolean_score(self):
        # True and False must not be accepted as scores
        with self.assertRaises(ValueError):
            record_score(self.fixtures, "M001", True, 1)

        self.assertEqual(self.fixtures[0]["status"], "pending")

    def test_six_teams_generate_fifteen_fixtures(self):
        # Create six teams
        teams = []

        for name in ["Chelsea", "Arsenal", "Liverpool",
                    "Man City", "Man U", "Tottenham"]:
            register_team(teams, name)

        # Generate their fixtures
        fixtures = generate_fixtures(teams)

        # Six teams should produce fifteen fixtures
        self.assertEqual(len(fixtures), 15)

if __name__ == "__main__":
    unittest.main()