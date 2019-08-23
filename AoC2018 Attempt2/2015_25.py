test = 10,10
data = "2981, column 3075."
data = 2981,3075

def get_next(pos):
    pos[1] += 1
    path = []
    path.append(pos[:])
    while pos[1] > 0:
        pos[0] += 1
        pos[1] -= 1
        path.append(pos[:])
    return path
def run(data):

    from collections import defaultdict
    rows = defaultdict(int)
    rows[tuple([0,0])] = 20151125
    pos = [0,1]
    queue = []
    last = 0,0
    queue.append(pos)
    queue.append([1,0])
    while queue:
        to_check = queue.pop(0)
        if to_check[0] == 0:
            for n in get_next(to_check[:]):
                queue.append(n)
        new_code = (rows[tuple([last[0], last[1]])] * 252533)%33554393
        rows[tuple(to_check)] = new_code
        last = to_check
        if rows[tuple([data[0]-1, data[1]-1])] != 0:
            print(rows[tuple([data[0]-1, data[1]-1])])
            break
import time
start = time.time()
run(data[::-1])
print(time.time()-start)