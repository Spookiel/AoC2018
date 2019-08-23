test = """"""
data = """"""





snum = 9445


def gen(x, y):
    global snum
    rID = x + 10
    pL = rID*y
    pL += snum
    pL *= rID
    return int(str(pL)[-3]) - 5


print(gen(3, 5))

board = [[i for i in range(30)] for j in range(30)]

for i in range(len(board)):
    for j in range(len(board[i])):
        board[i][j] = gen(i+1, j+1)



"""best = 0
best_coord = None
for k in range(len(board)):
    for j in range(len(board)):
        try:
            for i in range(300):
                for u in range(300):
                    to_score = board[k:i+1][j:u]

            if to_score > best:
                best = to_score
                best_coord = k+1, j+1
        except:
            pass
print(best, best_coord)"""
serial = int(input())
import numpy
def power(x, y):
    rack = (x + 1) + 10
    power = rack * (y + 1)
    power += serial
    power *= rack
    return (power // 100 % 10) - 5

grid = numpy.fromfunction(power, (300, 300))

for width in range(2, 300):
    windows = sum(grid[x:x-width, y:y-width] for x in range(width) for y in range(width))
    maximum = int(windows.max())
    location = numpy.where(windows == maximum)
    print(width, maximum, location[0][0] + 1, location[1][0] + 1)








