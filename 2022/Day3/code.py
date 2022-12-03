import numpy as np
with open("input.txt") as f: raw=f.read()

puntuations = {chr(i): i-ord('a')+1 for i in range(ord('a'), ord('z')+1)}
puntuations.update({chr(i): i-ord('A')+27 for i in range(ord('A'), ord('Z')+1)})

points = sum(np.sum([puntuations[n] for n in np.intersect1d(np.array([j for j in i])[:int(len(i)/2)], np.array([j for j in i])[int(len(i)/2):])]) for i in raw.splitlines())

print(points)