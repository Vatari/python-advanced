def team_lineup(*args):
    players = {}

    for player, country in args:
        if country not in players:
            players[country] = []
        players[country].append(player)

    sorted_countries = sorted(players.items(), key=lambda x: (-len(x[1]), len(x[1]), x))

    output = []
    for country, players in sorted_countries:
        output.append(f"{country}:")
        for player in players:
            output.append(f"  -{player}")

    return '\n'.join(output)


print(team_lineup(
    ("Lionel Messi", "Argentina"),
    ("Neymar", "Brazil"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Harry Kane", "England"),
    ("Kylian Mbappe", "France"),
    ("Raheem Sterling", "England")))
