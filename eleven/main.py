from inn import *

# "ne,ne,ne"
print(in1[0], in1[1])

def calc_dist(x, y, z):
    dist = abs(x) + abs(y) + abs(z)
    dist /= 2
    return dist

def walk(steps):
    max_distance = 0
    x, y, z = 0, 0, 0
    steps = steps.split(",")
    print("steps:", len(steps))
    for step in steps:
        if step == "n":
            y += 1
            z -= 1
        elif step == "s":
            y -= 1
            z += 1
        elif step == "ne":
            x += 1
            z -= 1
        elif step == "nw":
            y += 1
            x -= 1
        elif step == "se":
            y -= 1
            x += 1
        elif step == "sw":
            z += 1
            x -= 1
        dist = calc_dist(x, y, z)
        if dist > max_distance:
            max_distance = dist
    print(max_distance)

def show(problem):
    print(problem)
    walk(problem[0])
    print()

for problem in [in1, in2, in3, in4]:
    show(problem)
show(in_final)
