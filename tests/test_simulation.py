
import unittest

from tournament.teams import register_team
from tournament.fixtures import generate_fixtures, record_score
from tournament.simulation import simulate_fixtures


class TestSimulation(unittest.TestCase):

    def setUp(self):
        # Create four teams and generate their fixtures
        self.teams = []

        for name in ["Chelsea", "Arsenal", "Man City", "Liverpool"]:
            register_team(self.teams, name)

        self.fixtures = generate_fixtures(self.teams)

    def test_same_seed_produces_same_results(self):
        # The same seed should generate identical results
        first = simulate_fixtures(self.fixtures, 42)
        second = simulate_fixtures(self.fixtures, 42)

        self.assertEqual(first, second)

    def test_simulation_does_not_change_original(self):
        # Save a copy of the original fixtures
        original = [fixture.copy() for fixture in self.fixtures]

        simulate_fixtures(self.fixtures, 42)

        # Original fixtures should remain unchanged
        self.assertEqual(self.fixtures, original)

    def test_simulation_preserves_played_results(self):
        # Record a real result before simulation
        record_score(self.fixtures, "M001", 3, 1)

        simulated = simulate_fixtures(self.fixtures, 42)

        # The already-played result should remain unchanged
        self.assertEqual(simulated[0]["home_score"], 3)
        self.assertEqual(simulated[0]["away_score"], 1)


if __name__ == "__main__":
    unittest.main()
