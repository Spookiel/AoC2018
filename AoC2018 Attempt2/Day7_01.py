inp = """Step U must be finished before step R can begin.
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
from collections import defaultdict
def run(data):
    before_start = defaultdict(set)
    after_start = defaultdict(set)
    total = set()
    lines = [i.split() for i in data.splitlines()]
    for line in lines:
        before, after = line[1], line[-3]
        before_start[after].add(before)
        after_start[before].add(after)

        total.add(before)
        total.add(after)
    print(before_start)
    order = []
    queue = sorted([i for i in total if len(before_start[i])==0])
    while queue:
        flag = False
        to_check = queue.pop(0)
        for child in before_start[to_check]:
            if child not in order:
                flag = True

        if not flag:
            order.append(to_check)
            for child in after_start[to_check]:
                if child not in order and child not in queue:
                    queue.append(child)
        queue = sorted(queue)
    print("".join(order))





run(inp)
"ACBDESULXKYZIMNTFGWJVPOHRQ"
"ACBDESULXKYZIMNTFGWJVPOHRQ"
