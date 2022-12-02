entrada = open("input", "r")
bags = []
contain = ["shiny gold"] 
l = 0

for rule in entrada:
    ruleS = rule.replace('\n', '').split(' ')
    if ruleS[4] != "no":
        bags.append([str(ruleS[0] + ' ' + ruleS[1]), str(ruleS[5] + ' ' + ruleS[6])])
    
print(bags)
print("//////////////////////")

while len(contain) != l:
    l = len(contain)
    # contain1 = contain
    for bag in bags:
        if bag[1] in contain and bag[0] not in contain:
            contain.append(bag[0])
            bags.pop(bags.index(bag))
            print(bag)
            print(bags)

    print(contain)
    print(len(contain))
    print("----------------------------")
    

contain.pop(0)
print("===============================")
print(contain)
print(len(contain))

#daydata = {"label": "", "y": [], "name": ""}