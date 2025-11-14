# https://everybody.codes/event/2025/quests/7
# dict mapping the characters to the chars that are permitted to follow

names, lines = open(0).read().split("\n\n")
names = names.split(",")
lines = lines.splitlines()

rules = {}

for line in lines:
    left, right = line.split(" > ")
    rules[left] = right.split(",") 
        # also set it for the left side
        
for name in names:
    for x,y in zip(name, name[1:]):
        if y not in rules.get(x, []):
            break
    else:
        print(name)