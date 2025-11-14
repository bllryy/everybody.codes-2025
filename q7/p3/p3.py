# all possible names that could be made

names, lines = open(0).read().split("\n\n")
names = names.split(",")
lines = lines.splitlines()

rules = {}

for line in lines:
    left, right = line.split(" > ")
    rules[left] = right.split(",") 
        # also set it for the left side
        
possible = set()

def generate(prefix):
    output =set()
    if len(prefix) >= 7: output.add(prefix)
    if len(prefix) >= 11: return output
    
    for next in rules.get(prefix[-1], []):
        output |= generate(prefix+next)
        
    return output
        
for index, name in enumerate(names, start=1):
    for x,y in zip(name, name[1:]):
        if y not in rules.get(x, []):
            break
    else:
        possible |= generate(name)
        
print(len(possible))