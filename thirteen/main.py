from inn import inn
from copy import deepcopy

class Layer:
    def __init__(self, depth, range_):
        self.depth = depth
        self.range = range_
        if range_ == -1:
            self.index = -1
        else:
            self.index = 0
        self.is_rising = True

    def tick(self):
        if self.range == -1:
            return
        if self.is_rising:
            self.index += 1
        else: 
            self.index -= 1
        if self.index == self.range - 1:
            self.is_rising = False
        elif self.index == 0:
            self.is_rising = True

class Firewall:
    def __init__(self, data):
        self.layers = {}
        self.max = 0
        for line in data:
            depth, range_ = line.strip().split(": ")
            depth, range_ = int(depth), int(range_)
            self.layers[depth] = Layer(depth, range_)
            self.max = max(self.max, depth)

    def tick(self, step):
        damage = 0
        for depth in range(self.max + 1):
            if depth not in self.layers:
                self.layers[depth] = Layer(depth, -1)
            layer = self.layers[depth]
            hit = ""
            if depth == step:
                if layer.index == 0:
                    damage = depth * layer.range
                    hit = "HIT------------- " + str(damage)
                else:
                    hit = "MISS"
                #print("TICK:", depth, str(layer.index) + "/" + str(layer.range), hit)
            layer.tick()
        return damage

def slow_search(first_firewall):
    delay = 0
    least_damage = None
    furthest = None

    firewall = first_firewall
    last_firewall = None

    while True:
        damage = 0
        
        if last_firewall is not None:
            firewall = last_firewall
        firewall.tick(None)
        #firewall.tick(None)
        delay += 1
        last_firewall = deepcopy(firewall)

        for i in range(firewall.max + 1):
            damage += firewall.tick(i)
            if damage > 0:
                break
        if furthest is None or i > furthest:
            furthest = i
            print("DELAY:", delay, "FURTHEST:", furthest)

        if (least_damage is None or damage < least_damage) and damage != 2:
            least_damage = damage
            print("DELAY:", delay, "LEAST:", least_damage)
        if damage == 0:
            break
        #input("pause")

def fast_search(firewall):
    delay = 0
    while True:
        taken_damage = False
        for depth in range(firewall.max + 1):
            picoseconds = delay + depth
            collission = "MISS"
            layer = None
            if depth in firewall.layers:
                layer = firewall.layers[depth]
                period = (layer.range - 1) * 2
                if picoseconds % period == 0:
                    taken_damage = True
                    break
        if not taken_damage:
            print("DELAY:", delay)
            break
        delay += 2

if __name__ == "__main__":
    data = inn("input")
    firewall = Firewall(data)
    fast_search(firewall)
