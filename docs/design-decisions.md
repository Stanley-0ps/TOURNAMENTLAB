# TournamentLab – Design Decisions

## 1. Modular Architecture

The application is divided into separate Python modules, with each module responsible for a specific task.

- `teams.py` handles team registration and listing.
- `fixtures.py` generates fixtures and records match results.
- `standings.py` calculates and ranks team statistics.
- `storage.py` handles saving and loading tournament data.
- `cli.py` manages user interaction through the command-line interface.
- `main.py` serves as the application entry point.

**Reason:** This separation makes the application easier to maintain, test, debug, and extend.

## 2. Team Identification

Each registered team receives a unique ID using the format `TM001`, `TM002`, and so on.

Team names are trimmed and compared without case sensitivity to prevent duplicates.

**Reason:** Unique IDs provide reliable references even when team names are similar in appearance.

## 3. Round-Robin Fixture Generation

The application uses nested loops to generate fixtures.

Each team is matched against the teams appearing after it in the list. This ensures that every pair plays once without generating duplicate matchups.

For N teams, the number of fixtures is:

`N × (N - 1) / 2`

**Reason:** This approach generates a complete single round-robin schedule efficiently.

## 4. Match Result Validation

A fixture can only receive a result if:

- The fixture ID exists.
- The fixture has not already been played.
- Both scores are non-negative integers.
- Boolean and floating-point values are rejected.

**Reason:** Validation protects tournament records from invalid or inconsistent results.

## 5. Dynamic Standings Calculation

Standings are calculated from completed fixtures instead of being stored as permanent statistics.

The application calculates:

- Matches played
- Wins, draws, and losses
- Goals for and against
- Goal difference
- Points

Teams are ranked using the following order:

1. Points (descending)
2. Goal difference (descending)
3. Goals scored (descending)
4. Team name (alphabetical)

**Reason:** Recalculating standings ensures that the table reflects the actual match results and avoids outdated statistics.

## 6. JSON Data Persistence

Tournament data is stored in JSON format with a schema version.

The saved structure contains:

- `schema_version`
- `teams`
- `fixtures`

The loading process validates the data before returning it to the application.

**Reason:** JSON is human-readable, supported by Python's standard library, and suitable for storing structured tournament records.

## 7. Automated Testing

The project uses Python's built-in `unittest` framework.

Tests are organised by module to verify individual responsibilities and important edge cases.

**Reason:** Automated testing helps identify regressions and increases confidence that changes do not break existing functionality.

## 8. Champion Detection

The application only announces a champion when every fixture has been completed.

The champion is the team ranked first by the standings calculation.

**Reason:** Declaring a champion before all matches are played could produce an inaccurate result.

## 9. Standard Library Only

The project uses Python's built-in modules without external dependencies.

**Reason:** This keeps installation simple and demonstrates the use of core Python programming features.