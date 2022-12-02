with open("input.txt") as f: raw=f.read()

opponent = {'A': 0, 'B': 1, 'C': 2}
you = {'X': 0, 'Y': 1, 'Z': 2}

puntuations = [[4, 8, 3], [1, 5, 9], [7, 2, 6]]

points = sum([puntuations[opponent.get(i[0])][you.get(i[-1])] for i in raw.splitlines()])

print(points)