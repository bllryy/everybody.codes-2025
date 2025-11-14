# may be more than one name
# sum of all the indices that make the rules

names, lines = open(0).read().split("\n\n")
names = names.split(",")
lines = lines.splitlines()

rules = {}

for line in lines:
    left, right = line.split(" > ")
    rules[left] = right.split(",") 
        # also set it for the left side
        
total =0
        
for index, name in enumerate(names, start=1):
    for x,y in zip(name, name[1:]):
        if y not in rules.get(x, []):
            break
    else:
        total  += index
print(total)