import math
[teams, special], score = [int(_) for _ in input().split()], []
league = range(1, teams+1)
for _ in range(teams): score.append(list(map(int, input().split())))
for _ in range(int(math.log(teams, 2))):
    champion = []
    for champ in range(int(len(league)/2)):
        winner = 0 if score[league[champ*2]-1][league[champ*2+1]-1]==league[champ*2] else 1
        if league[champ*2+abs(winner-1)]==special:
            winner = abs(winner-1)
            special = 0
        champion.append(league[champ*2+winner])
    league = champion
print(league[0])
# Passed