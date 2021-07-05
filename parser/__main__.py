from parser.ELO import *
from parser import root_path, teams_txt

output = ""

if not teams_txt.exists():
    message = f"The file \"teams.txt\" does not exist at {teams_txt}"
    padding = len(message) + 6
    print(
        f"""
        {'#' * padding}
        #{' ' * (padding - 3)} #
        #  {message}  #
        #{' ' * (padding - 3)} #
        {'#' * padding}
        """
    )
    exit()


def convert_line_to_teams(line: str) -> (Team, Team):
    team1_data = line.split("-")[0].split(",")
    team2_data = line.split("-")[1].split(",")
    team1 = Team(
        name=team1_data[0].strip(),
        elo=int(team1_data[1].strip()),
        rounds_won=int(team1_data[2].strip())
    )
    team2 = Team(
        name=team2_data[0].strip(),
        elo=int(team2_data[1].strip()),
        rounds_won=int(team2_data[2].strip())
    )
    return team1, team2


with open(teams_txt, "r") as match_data:
    team_elos: dict[str: int] = {}

    lines = match_data.readlines()
    for line in lines:
        try:
            team1, team2 = convert_line_to_teams(line)
        except (IndexError, ValueError):
            continue
        team_elos[team1.name] = team1.elo
        team_elos[team2.name] = team2.elo

    for match_line in lines:
        try:
            team1, team2 = convert_line_to_teams(match_line)
            team1.elo = team_elos[team1.name]
            team2.elo = team_elos[team2.name]
            result = ELO().calculate(team1, team2)
            team1_elo = result["team1"]
            team2_elo = result["team2"]
            team_elos[team1.name] = team1_elo
            team_elos[team2.name] = team2_elo
        except (IndexError, ValueError):
            print(f"Skipping the line: \"{match_line}\"\n"
                  f"\t - Reason: Was not formatted correctly\n"
                  f"\t - Format: Team Name, ELO, Score - Team Name, ELO, Score")
            continue

    for team in team_elos.keys():
        output += \
            f"{team}: {team_elos[team]:.0f}\n"

print("Finished: Outputting to result.txt and to stdout\n\n")
with open(root_path.parent / "result.txt", "w+") as result_txt:
    result_txt.write(output)
print(output)
