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

with open(teams_txt, "r") as match_data:
    for match in match_data.readlines():
        team1_data = match.split("-")[0].split(",")
        team2_data = match.split("-")[1].split(",")
        try:
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
            result = ELO().calculate(team1, team2)
            team1_elo = result["team1"]
            team2_elo = result["team2"]
            output += \
                f"{team1.name}: {team1_elo:.0f}\n" \
                f"{team2.name}: {team2_elo:.0f}\n"

        except (IndexError, ValueError):
            print(f"Skipping the line: \"{match}\"\n"
                  f"\t - Reason: Was not formatted correctly\n"
                  f"\t - Format: Team Name, ELO, Score - Team Name, ELO, Score")
            continue


print("Finished: Outputting to result.txt and to stdout\n\n")
with open(root_path.parent / "result.txt", "w+") as result_txt:
    result_txt.write(output)
print(output)

