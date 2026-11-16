import unittest
import tempfile
import os

from tournament.teams import register_team
from tournament.fixtures import generate_fixtures, record_score
from tournament.storage import save_tournament, load_tournament


class TestStorage(unittest.TestCase):

    def setUp(self):
        # Create a temporary file for each test
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.file_path = self.temp_file.name
        self.temp_file.close()

        # Create tournament data
        self.teams = []

        for name in ["Chelsea", "Arsenal", "Man U", "Man City"]:
            register_team(self.teams, name)

        self.fixtures = generate_fixtures(self.teams)
        record_score(self.fixtures, "M001", 2, 1)

    def tearDown(self):
        # Remove the temporary file after each test
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_save_tournament(self):
        # Saving should create a valid JSON file
        save_tournament(self.teams, self.fixtures, self.file_path)

        self.assertTrue(os.path.exists(self.file_path))

    def test_load_tournament(self):
        # Saved data should be restored correctly
        save_tournament(self.teams, self.fixtures, self.file_path)

        loaded_teams, loaded_fixtures = load_tournament(self.file_path)

        self.assertEqual(loaded_teams, self.teams)
        self.assertEqual(loaded_fixtures, self.fixtures)

    def test_loaded_data_preserves_results(self):
        # Recorded scores should survive saving and loading
        save_tournament(self.teams, self.fixtures, self.file_path)

        _, loaded_fixtures = load_tournament(self.file_path)

        self.assertEqual(loaded_fixtures[0]["home_score"], 2)
        self.assertEqual(loaded_fixtures[0]["away_score"], 1)
        self.assertEqual(loaded_fixtures[0]["status"], "played")

    def test_reject_unknown_team_reference(self):
        # Corrupt a fixture by referencing a nonexistent team
        self.fixtures[0]["home_id"] = "TM999"

        # Save the corrupted tournament
        save_tournament(self.teams, self.fixtures, self.file_path)

        # Loading should reject the invalid data
        with self.assertRaises(ValueError):
            load_tournament(self.file_path)

if __name__ == "__main__":
    unittest.main()