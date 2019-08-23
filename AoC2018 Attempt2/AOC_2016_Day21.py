data = """Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3"""


def simulate(kit, BHP, BDMG, BARM, PHP):
    PDMG = sum([i[1] for i in kit])
    PARM = sum(i[2] for i in kit)
    while True:
        BHP -= (1 if PDMG-BARM < 1 else PDMG-BARM)
        if BHP < 1:
            return True
        PHP -= (1 if BDMG-PARM < 1 else BDMG-PARM)
        if PHP < 1:
            return False
print(simulate([[80, 5, 5], [80, 0, 0],[80, 0, 0]], 12, 7, 7, 8))

def run(data):
    import itertools
    weapons = {}
    armour = {}
    rings = {}
    things = set()
    lines = [i.split() for i in data.splitlines()]
    for i in range(5):
        name, stats = lines[i][0], list(map(int, lines[i][1:]))
        weapons[name] = stats
        things.add(name)
    for i in range(5, 10):
        name, stats = lines[i][0], list(map(int, lines[i][1:]))
        armour[name] = stats
        things.add(name)


    for i in range(10, 16):
        name, stats = lines[i][0]+lines[i][1], list(map(int, lines[i][2:]))
        rings[name] = stats
        things.add(name)
    m = -999
    ringcombs = [i for i in itertools.combinations(list(rings.keys()), 2) if i[0] != i[1]]+list(rings.keys())
    for i in ringcombs:
        for w in weapons.keys():
            for a in armour.keys():
                kit1, kit2 = [], []
                if len(i)==2:
                    kit1.append(rings[i[0]])
                    kit1.append(rings[i[1]])
                    kit2.append(rings[i[0]])
                    kit2.append(rings[i[1]])
                else:
                    kit1.append(rings[i])
                    kit2.append(rings[i])
                kit1.append(weapons[w])
                kit1.append(armour[a])
                kit2.append(weapons[w])
                if not simulate(kit1, 109, 8, 2, 100):
                    a = sum([i[0]  for i in kit1])
                    if a > m:
                        m = a
                        print(m, "Best", kit1)
                if  not simulate(kit2, 109, 8, 2,100):
                    b = sum([i[0] for i in kit2])
                    if b > m:
                        m = b
                        print(m, "BEST", kit2)
    print(m)








run(data)