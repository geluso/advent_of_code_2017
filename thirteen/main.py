from inn import inn

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
            if depth == step and layer.index == 0:
                hit = "HIT"
                damage = depth * layer.range
            layer.tick()
        return damage

damage = 0
data = inn("input")
firewall = Firewall(data)
for i in range(firewall.max + 1):
    damage += firewall.tick(i)
print("DAMAGE:", damage)
