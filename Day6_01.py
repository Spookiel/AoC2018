import os
from collections import defaultdict

def part1(lines):
    coords = set()
    max_r ,max_c = 0,0

    for line in lines:
        r, c = map(int, line.split(", "))
        coords.add((r, c))
        max_r = max(max_r, r)
        max_c = max(max_c, c)

    coord_id_to_point = {coord_id: point for coord_id, point in enumerate(coords, start=1)}
    print(coord_id_to_point)
    region_sizes = defaultdict(int)
    infinite_ids = set()

    for i in range(max_r + 1):
        for j in range(max_c + 1):
            min_dists = sorted([(abs(r - i) + abs(c - j), coord_id) for coord_id, (r, c) in coord_id_to_point.items()])

            if len(min_dists) == 1 or min_dists[0][0] != min_dists[1][0]:
                coord_id = min_dists[0][1]
                region_sizes[coord_id] += 1

                if i == 0 or i == max_r or j == 0 or j == max_c:
                    infinite_ids.add(coord_id)

    final = []
    for coord_id, size in region_sizes.items():
        if coord_id not in infinite_ids:
            final.append(size)
    print(max(final))
    print(region_sizes)
data = """181, 47
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
lines = [line.strip() for line in data.split('\n')]
print(part1(lines))