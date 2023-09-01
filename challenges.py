# Create a list of matches from the teams list, making sure there's no repetaion in the matches
teams = ['wolves', 'foxes', 'tigers', 'lions', 'monkeys']
matches = [(f"{team1} vs {team2}") for team1 in teams for team2 in teams[teams.index(team1) + 1:]]

for match in matches:
    print(match)

