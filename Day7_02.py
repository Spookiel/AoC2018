from collections import defaultdict
from copy import copy
d = """Step U must be finished before step R can begin.
Step C must be finished before step B can begin.
Step A must be finished before step S can begin.
Step E must be finished before step O can begin.
Step D must be finished before step Z can begin.
Step L must be finished before step X can begin.
Step S must be finished before step F can begin.
Step B must be finished before step J can begin.
Step Z must be finished before step T can begin.
Step X must be finished before step W can begin.
Step K must be finished before step T can begin.
Step M must be finished before step H can begin.
Step I must be finished before step W can begin.
Step T must be finished before step J can begin.
Step N must be finished before step O can begin.
Step F must be finished before step G can begin.
Step W must be finished before step P can begin.
Step G must be finished before step V can begin.
Step Y must be finished before step V can begin.
Step J must be finished before step V can begin.
Step V must be finished before step R can begin.
Step P must be finished before step H can begin.
Step O must be finished before step R can begin.
Step H must be finished before step R can begin.
Step R must be finished before step Q can begin.
Step L must be finished before step O can begin.
Step V must be finished before step H can begin.
Step X must be finished before step K can begin.
Step D must be finished before step N can begin.
Step C must be finished before step P can begin.
Step E must be finished before step I can begin.
Step P must be finished before step O can begin.
Step T must be finished before step F can begin.
Step U must be finished before step K can begin.
Step A must be finished before step O can begin.
Step G must be finished before step O can begin.
Step A must be finished before step W can begin.
Step G must be finished before step Q can begin.
Step U must be finished before step J can begin.
Step V must be finished before step O can begin.
Step J must be finished before step Q can begin.
Step X must be finished before step G can begin.
Step B must be finished before step Y can begin.
Step J must be finished before step R can begin.
Step B must be finished before step F can begin.
Step K must be finished before step F can begin.
Step S must be finished before step Z can begin.
Step T must be finished before step H can begin.
Step W must be finished before step R can begin.
Step I must be finished before step N can begin.
Step Z must be finished before step R can begin.
Step J must be finished before step O can begin.
Step M must be finished before step R can begin.
Step Y must be finished before step J can begin.
Step E must be finished before step J can begin.
Step T must be finished before step G can begin.
Step T must be finished before step V can begin.
Step M must be finished before step O can begin.
Step C must be finished before step J can begin.
Step D must be finished before step O can begin.
Step F must be finished before step P can begin.
Step H must be finished before step Q can begin.
Step F must be finished before step J can begin.
Step Z must be finished before step P can begin.
Step T must be finished before step O can begin.
Step Z must be finished before step M can begin.
Step U must be finished before step H can begin.
Step W must be finished before step J can begin.
Step L must be finished before step Y can begin.
Step A must be finished before step T can begin.
Step M must be finished before step V can begin.
Step O must be finished before step Q can begin.
Step N must be finished before step J can begin.
Step A must be finished before step V can begin.
Step K must be finished before step G can begin.
Step N must be finished before step F can begin.
Step B must be finished before step T can begin.
Step I must be finished before step H can begin.
Step V must be finished before step P can begin.
Step E must be finished before step T can begin.
Step E must be finished before step G can begin.
Step U must be finished before step L can begin.
Step X must be finished before step P can begin.
Step L must be finished before step R can begin.
Step Y must be finished before step O can begin.
Step K must be finished before step O can begin.
Step Z must be finished before step I can begin.
Step P must be finished before step R can begin.
Step A must be finished before step X can begin.
Step O must be finished before step H can begin.
Step C must be finished before step D can begin.
Step D must be finished before step F can begin.
Step X must be finished before step H can begin.
Step D must be finished before step Y can begin.
Step Y must be finished before step P can begin.
Step E must be finished before step V can begin.
Step K must be finished before step H can begin.
Step M must be finished before step G can begin.
Step L must be finished before step I can begin.
Step D must be finished before step K can begin.
Step D must be finished before step M can begin."""
things = [c.split() for c in d.split('\n')]
things = [(c[1], c[-3]) for c in things]
total_set = set()
needed_before = defaultdict(set)
for (before, after) in things:
  total_set.add(before)
  total_set.add(after)
  needed_before[after].add(before)

orig_set = copy(total_set)
original_thing = {k: copy(needed_before[k]) for k in needed_before}

res = []
while total_set:
  z = sorted([x for x in total_set if (x not in needed_before) or (len(needed_before[x]) == 0)])[0]
  res.append(z)
  total_set.remove(z)
  for c in needed_before:
    if z in needed_before[c]:
      needed_before[c].remove(z)
print( 'a', ''.join(res))

second = 0
workers = {k: None for k in range(5)}
while orig_set or any(workers.values()):
  for worker in workers:
    if workers[worker]:
      print(workers[worker])
      letter, step = workers[worker]
      if step == ord(letter) - ord('A') + 61:
        for c in original_thing:
          if letter in original_thing[c]:
            original_thing[c].remove(letter)
        workers[worker] = None
      else:
        workers[worker] = (letter, step + 1)
    if not workers[worker]:
      if orig_set:
        possibilities = sorted([x for x in orig_set if (x not in original_thing) or (len(original_thing[x]) == 0)])
        if possibilities:
          letter = possibilities[0]
          workers[worker] = (letter, 1)
          orig_set.remove(letter)
  second += 1
print( "b", (second - 1))