inp = """181, 47
337, 53
331, 40
137, 57
200, 96
351, 180
157, 332
113, 101
285, 55
189, 188
174, 254
339, 81
143, 61
131, 155
239, 334
357, 291
290, 89
164, 149
248, 73
311, 190
54, 217
285, 268
354, 113
318, 191
182, 230
156, 252
114, 232
159, 299
324, 280
152, 155
295, 293
194, 214
252, 345
233, 172
272, 311
230, 82
62, 160
275, 96
335, 215
185, 347
134, 272
58, 113
112, 155
220, 83
153, 244
279, 149
302, 167
185, 158
72, 91
264, 67"""

coords = set()
for i in inp.split("\n"):
    coords.add(tuple(map(int, i.split(","))))

board = [[None for j in range(500)] for i in range(500)]

coords_to_point = {-999:"-"}
for i,j in enumerate(coords):
    board[j[1]][j[0]] = i
    coords_to_point[tuple(j)] = i
print(coords_to_point)

def distance(x, y, coords):
    d = {}
    test = []
    for i in coords:
        ans = abs(x-i[0])+abs(y-i[1])
        d[i] = ans
        test.append((i, ans, (x, y)))
    for k in d.keys():
        if d[k]==min(d.values()):
            if list(d.values()).count(d[k])==1:
                return k
            else:
                return -999



for i in range(500):
    for j in range(500):
        board[i][j] = coords_to_point[distance(j, i, coords)]


invalid = set()
for i in board[0]:
    invalid.add(i)
for j in board:
    invalid.add(j[0])
    invalid.add(j[-1])
for i in board[-1]:
    invalid.add(i)

c = [0 for i in range(len(coords))]
for i in board:
    for j in i:
        if j != "-":
            c[j] += 1

ans = []
for i in range(len(coords)):
    if i not in invalid:
        ans.append((c[i], i))
print(sorted(ans)[-1][0])