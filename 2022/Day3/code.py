with open("input2.txt") as f: raw=f.read()

puntuations = {chr(i): i-ord('a')+1 for i in range(ord('a'), ord('z')+1)}
puntuations.update({chr(i): i-ord('A')+27 for i in range(ord('A'), ord('Z')+1)})



# points = sum([puntuations[opponent.get(i[0])][you.get(i[-1])] for i in raw.splitlines()])

# print(points)