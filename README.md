# ELO Parser
Created to simplify the bulk calculation of elo for teams

## Usage

### File Setup
Create a file named `teams.txt` in the root directory (the directory above parser).

Within the `teams.txt` file matches due for calculation must be placed in this format:

- Team Name, ELO, Score - Team Name, ELO, Score

For example:

- 20Racecar, 2000, 3 - Bapemen, 1300, 1

A note: whitespace does not matter so long as the above is on the same line using the comma and hyphen format.

For additional matches add each new match to a new line

### Run the program

```bash
python -m parser
```
This will output the result to `stdout` and a file named `result.txt` in the root directory.