"""
17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
Data from square 1 is carried 0 steps, since it's at the access port.
Data from square 12 is carried 3 steps, such as: down, left, left.
Data from square 23 is carried only 2 steps: up twice.
Data from square 1024 must be carried 31 steps.
"""

# target = 312051
# 
# def build_grid(target, level=1, grid=[[1]]):
#     if (level ** 2) >= target:
#         return grid
#     else:
#         new_rows = []
#         for row in grid:
#             new_row = [0]
#             new_row.extend(row)
#             new_row.append(0)
#             new_rows.append(new_row)
#         
#         new_grid = [[0] * (level + 2)]
#         new_grid.extend(new_rows)
#         new_grid.extend([[0] * (level + 2)])
#         return build_grid(target, level + 2, new_grid)
# 
# print(build_grid(1))
# print(build_grid(2))
# print(build_grid(22))
# 
# corner=5
# border = list(range((corner-2) ** 2 + 1, corner**2 + 1))
# print(border)
# 
# index = border.index(10)
# print(index)
# if index < (corner-1) or index == len(border) - 1:
#     col = corner
# if index >= len(border) - corner:
#     row = corner
# 
# print("col,row:", col, row)

import math
from collections import defaultdict

class SpiralMemory:
    def __init__(self):
        self.memory = defaultdict(lambda: defaultdict(int))
        self.col_cursor = 0
        self.row_cursor = 0
        self.memory[0][0] = 1
        self.n = 1

    def should_reset(self):
        return self.n == 1 or 0 ==  sum([self.one_right, self.n_minus_two_up,
            self.n_minus_one_left, self.n_minus_one_down, self.n_minus_one_right])

    def reset(self):
        print("reset")
        self.n += 2
        self.one_right = 1
        self.n_minus_two_up = self.n - 2
        self.n_minus_one_left = self.n - 1
        self.n_minus_one_down = self.n - 1
        self.n_minus_one_right = self.n - 1

    def expand(self):
        if self.should_reset():
            self.reset()

        if self.one_right > 0:
            self.col_cursor += 1
            self.one_right -= 1
            print("right", self.col_cursor, self.row_cursor)
        elif self.n_minus_two_up > 0:
            self.row_cursor += 1
            self.n_minus_two_up -= 1
            print("up", self.col_cursor, self.row_cursor)
        elif self.n_minus_one_left > 0:
            self.col_cursor -= 1
            self.n_minus_one_left -= 1
            print("left", self.col_cursor, self.row_cursor)
        elif self.n_minus_one_down > 0:
            self.row_cursor -= 1
            self.n_minus_one_down -= 1
            print("down", self.col_cursor, self.row_cursor)
        elif self.n_minus_one_right > 0:
            self.col_cursor += 1
            self.n_minus_one_right -= 1
            print("right", self.col_cursor, self.row_cursor)

        self.set_current_cell()

    def get(self, col, row):
        return self.memory[col][row]

    def get_current_val(self):
        return self.get(self.col_cursor, self.row_cursor)

    def set_current_cell(self):
        col, row = self.col_cursor, self.row_cursor

        total = 0
        total += self.get(col-1, row+1)
        total += self.get(col, row+1)
        total += self.get(col+1, row+1)

        total += self.get(col-1, row)
        total += self.get(col+1, row)

        total += self.get(col-1, row-1)
        total += self.get(col, row-1)
        total += self.get(col+1, row-1)

        self.memory[col][row] = total

grid = SpiralMemory()
target = 312051
last_val = 1
while last_val < target:
    last_val = grid.get_current_val()
    grid.expand()
print("BINGO:", last_val)
