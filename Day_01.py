from collections import Counter
import operator

inpstr = """292, 73
204, 176
106, 197
155, 265
195, 59
185, 136
54, 82
209, 149
298, 209
274, 157
349, 196
168, 353
193, 129
94, 137
177, 143
196, 357
272, 312
351, 340
253, 115
109, 183
252, 232
193, 258
242, 151
220, 345
336, 348
196, 203
122, 245
265, 189
124, 57
276, 204
309, 125
46, 324
345, 228
251, 134
231, 117
88, 112
256, 229
49, 201
142, 108
150, 337
134, 109
288, 67
297, 231
310, 131
208, 255
246, 132
232, 45
356, 93
356, 207
83, 97"""

coords = [tuple(map(int, l.split(','))) for l in inpstr.splitlines()]

topedge = min(coords, key=operator.itemgetter(1))[1]
bottomedge = max(coords, key=operator.itemgetter(1))[1]
leftedge = min(coords, key=operator.itemgetter(0))[0]
rightedge = max(coords, key=operator.itemgetter(0))[0]


def isfinite(c):
    return leftedge < c[0] < rightedge and topedge < c[1] < bottomedge


def find_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def single_min(it):
    s = sorted(it)
    return s[0] != s[1]


def indmin(it):
    min2 = min(it)
    return it.index(min2)


# Part1
count = Counter()

for i in range(leftedge, rightedge):
    for j in range(topedge, bottomedge):
        distances = [find_distance((i, j), c) for c in coords]

        if single_min(distances):
            count[coords[indmin(distances)]] += 1

maxarea = 0
for c in coords:
    if isfinite(c):
        maxarea = max(maxarea, count[c])

print(maxarea)

# Part 2
count = 0
for i in range(leftedge, rightedge):
    for j in range(topedge, bottomedge):
        distances = [find_distance((i, j), c) for c in coords]
        if sum(distances) < 10000:
            count += 1
print(count)