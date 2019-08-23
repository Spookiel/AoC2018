data = """initial state: #.##.##.##.##.......###..####..#....#...#.##...##.#.####...#..##..###...##.#..#.##.#.#.#.#..####..#

..### => .
##..# => #
#..## => .
.#..# => .
#.##. => .
#.... => .
##... => #
#...# => .
###.# => #
##.## => .
....# => .
..##. => #
..#.. => .
##.#. => .
.##.# => #
#..#. => #
.##.. => #
###.. => #
.###. => #
##### => #
####. => .
.#.#. => .
...#. => #
#.### => .
.#... => #
.#### => .
#.#.# => #
...## => .
..... => .
.#.## => #
..#.# => #
#.#.. => #"""
test = """...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #"""

test_state = """#..#.#..##......###...###"""

def nextg(cur, recipe):
  start = min(cur)
  end = max(cur)
  x = set()

  for i in range(start - 3, end + 4):
    pat = ''.join('#' if i + k in cur else '.' for k in [-2, -1, 0, 1, 2])
    if pat in recipe:
      x.add(i)

  return x

def viz(cur):
  print(''.join('#' if i in cur else '.' for i in range(-5, 120)))


lines = [l.strip('\n') for l in data.split('\n')]
print(lines)

init = lines[0][len('initial state: '):]
recipe = set()
for l in lines[2:]:
    if l[-1] == '#':
        recipe.add(l[:5])

cur = set(i for i, c in enumerate(init) if c == '#')

  # Part 1:
"""for i in range(20):
    cur = nextg(cur, recipe)
    print(sum(cur))"""

total = 0
for i in range(2000):
    cur = nextg(cur, recipe)
    s = sum(cur)
    print(i, s, s-total)
    total = s


#102 is where it is constant therefore if I have already found the sum of the first 2000 and the difference is
print(((50000000000 - 2000) * 69)+total)
print(total)


