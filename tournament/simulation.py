
import random
from copy import deepcopy


def simulate_fixtures(fixtures, seed):
    # Create a separate copy so real tournament records stay untouched
    simulated_fixtures = deepcopy(fixtures)

    # Use a seeded random generator for reproducible results
    rng = random.Random(seed)

    # Simulate only fixtures that have not been played
    for fixture in simulated_fixtures:
        if fixture["status"] == "pending":

            # Generate random scores between 0 and 5
            fixture["home_score"] = rng.randint(0, 5)
            fixture["away_score"] = rng.randint(0, 5)

            # Mark the simulated fixture as played
            fixture["status"] = "played"

    return simulated_fixtures
