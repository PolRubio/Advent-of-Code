f = open("input", "r")
x = []
for i in f:
  x.append(i.replace('\n',''))

def num_tree(r, d):
    tree = 0
    i = 0
    j = 0

    while i < len(x):
        if x[i][j%len(x[i])] == "#": tree += 1
        i += d
        j += r
        
    return(tree)

print(num_tree(1,1)*num_tree(3, 1)*num_tree(5,1)*num_tree(7,1)*num_tree(1,2))
