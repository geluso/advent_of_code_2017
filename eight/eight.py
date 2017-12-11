from inn import *
from collections import defaultdict

weights = {}
names = []
holding = defaultdict(list)
being_held = []
for line in i2.split("\n"):
    #print(line)
    cells = line.split(" ")
    name, weight = cells[0],  int(cells[1][1:-1])
    #print("name:", name, weight)
    weights[name] = weight
    names.append(name)
    if len(cells) > 2:
        held_cells = line.split(" -> ")[1]
        if ", " in held_cells:
            held_cells = held_cells.split(", ")
            for held in held_cells:
                #print("being held", name)
                holding[name].append(held)
                being_held.append(held)
        else:
            being_held.append(held_cells)
print(len(names), len(being_held))

bottom = None
for name in names:
    if name not in being_held:
        print("bottom", name)
        bottom = name

def weigh(name, level=0):
    current = weights[name]
    nodes = holding[name]
    last_held = None
    wacky = False
    for node in nodes:
        pounds = weigh(node, level + 1)
        current += pounds
        if last_held is None:
            last_held = pounds + weights[node]
        elif pounds != last_held:
            wacky = True
    if wacky:
        print()
        print("bottom weight:", current, name)
        print(name, holding[name])
        for node in holding[name]:
            print("wack at", level, "from", name, "->", node, weights[node], weigh(node, level + 1))

    return current

def simple_weigh(name, display=True):
    current = weights[name]
    nodes = holding[name]
    for node in nodes:
        pounds = simple_weigh(node, False)
        current += pounds
        if display:
            print(node, pounds)
    return current

# not 254 from 
# wack at 2 from vfjnsd -> quempkz 1225 2062
# wack at 2 from vfjnsd -> xvlxy 77 2062
# wack at 2 from vfjnsd -> tulwp 264 2070

# not 72662 from
# wack at 0 from bpvhwhh -> xnmjpa 72670 115030
# wack at 0 from bpvhwhh -> rilgrr 75761 115022
# wack at 0 from bpvhwhh -> fvrrpo 34174 115022
# wack at 0 from bpvhwhh -> zcmlgn 75203 115022
#suspect = "xnmjpa"
#suspect = "vfjnsd"
suspect = "tulwp"
total = simple_weigh(suspect)
print(total)
print(suspect, weights[name])
