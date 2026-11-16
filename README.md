# TournamentLab 🏆

**TournamentLab** is a Python-based command-line application for managing esports tournaments. It allows users to register teams, generate round-robin fixtures, record match results, calculate league standings, and manage tournament data through JSON storage.

The project was built to practise modular programming, data validation, file handling, automated testing, and software design using Python.

## Features

- **Team Management:** Register and list between 4 and 8 teams with unique IDs.
- **Input Validation:** Prevent duplicate team names, invalid team names, and registration beyond the tournament limit.
- **Fixture Generation:** Automatically generate single round-robin fixtures, ensuring every team plays every other team once.
- **Match Result Management:** Record match scores and prevent duplicate or invalid results.
- **League Standings:** Automatically calculate matches played, wins, draws, losses, goals for, goals against, goal difference, and points.
- **Automatic Team Ranking:** Rank teams by points, goal difference, goals scored, and alphabetical order.
- **Data Persistence:** Save and load tournament records using JSON.
- **Data Integrity:** Validate loaded tournament data and reject inconsistent records.
- **Champion Detection:** Identify the tournament champion after all fixtures have been completed.
- **Demo Simulation:** Generate reproducible match results using a random seed without modifying actual tournament records.
- **Automated Testing:** Verify application behaviour using Python's built-in `unittest` framework.

## Technologies Used

- Python 3
- JSON
- `random`
- `unittest`
- Python Standard Library

No external Python packages are required.

## Project Structure

```text
TournamentLab/
│
├── main.py
│
├── tournament/
│   ├── __init__.py
│   ├── teams.py
│   ├── fixtures.py
│   ├── standings.py
│   ├── storage.py
│   ├── simulation.py
│   └── cli.py
│
├── tests/
│   ├── __init__.py
│   ├── test_teams.py
│   ├── test_fixtures.py
│   ├── test_standings.py
│   ├── test_storage.py
│   └── test_simulation.py
│
├── docs/
│   ├── design-decisions.md
│   └── ai-learning-log.md
│
└── README.md
```

## Requirements

- Python 3.8 or newer.
- Git (optional, for cloning the repository).

## Getting Started

### 1. Clone the repository

```bash
git https://github.com/Stanley-0ps/TOURNAMENTLAB.git
```

### 2. Navigate into the project directory

```bash
cd TournamentLab
```

### 3. Run the application

```bash
python3 main.py
```

The application will display an interactive command-line menu.

## How to Use

TournamentLab provides the following menu options:

| Option | Action |
|---|---|
| 1 | Register team |
| 2 | List teams |
| 3 | Generate fixtures |
| 4 | List fixtures |
| 5 | Record match result |
| 6 | Show standings |
| 7 | Save tournament |
| 8 | Load tournament |
| 9 | Show champion |
| 10 | Run demo simulation |
| 0 | Exit |

### Typical Tournament Workflow

1. Register between 4 and 8 teams.
2. Generate the tournament fixtures.
3. Record match results as games are completed.
4. View the updated league standings.
5. Save the tournament data.
6. Load previously saved tournament data when needed.
7. View the champion after every fixture has been completed.

## Tournament Rules

TournamentLab uses a single round-robin format.

- Every team plays every other team once.
- A win awards 3 points.
- A draw awards 1 point to each team.
- A loss awards 0 points.
- Match scores must be non-negative integers.
- A fixture cannot receive more than one result.

### Standings Ranking

Teams are ranked using the following criteria, in order:

1. Highest points.
2. Highest goal difference.
3. Highest goals scored.
4. Team name in alphabetical order.

### Fixture Calculation

The number of fixtures is calculated using:

\[
\frac{N(N-1)}{2}
\]

Where `N` represents the number of registered teams.

For example, a tournament with 4 teams produces 6 fixtures, while a tournament with 6 teams produces 15 fixtures.

## Demo Simulation

TournamentLab includes a demo simulation feature for testing tournament outcomes.

The simulation:

- Uses a random seed to generate reproducible scores.
- Simulates only pending fixtures.
- Preserves results from already-played fixtures.
- Calculates separate simulated standings.
- Does not overwrite or modify actual tournament records.

Using the same seed with the same tournament data produces the same simulated results.

## Data Storage

Tournament data is saved in JSON format.

The saved data contains:

- `schema_version`
- `teams`
- `fixtures`

The application validates loaded data to prevent invalid team references, duplicate fixtures, invalid scores, and inconsistent tournament records.

The default save file is:

```text
tournament.json
```

## Running Automated Tests

TournamentLab uses Python's built-in `unittest` framework.

Run the complete test suite with:

```bash
python3 -m unittest discover -s tests -v
```

### Test Coverage

The project currently contains **29 automated tests** across five test modules.

| Test Module | Tests |
|---|---:|
| Team Management | 5 |
| Fixture Management | 11 |
| Standings | 6 |
| Data Storage | 4 |
| Demo Simulation | 3 |
| **Total** | **29** |

The tests cover successful operations, invalid inputs, duplicate records, score validation, standings calculations, data persistence, and simulation behaviour.

## Documentation

Additional project documentation is available in the `docs/` directory:

- `design-decisions.md` – Explains the architecture and key engineering decisions.
- `ai-learning-log.md` – Documents how AI assistance was used during development and the learning process.

## Author

**Ochai Stanley**

GitHub: [Stanley-0ps](https://github.com/Stanley-0ps)

---

*TournamentLab is a practical Python software engineering project focused on problem-solving, modular application development, data integrity, and automated testing.*