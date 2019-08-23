data = 33100000
#     33,100,000


import time
def factors(n):
    return sum([i for i in range(1, int(n)+1) if n%i==0])
def run(data):
    start = time.time()
    from collections import defaultdict
    houses = defaultdict(int)
    for elf in range(1, data//10):
        for house in range(elf, elf*51, elf):
            houses[house] += elf*11

    for k,v in houses.items():
        if v >= data:
            print(k)
            break
    print(time.time()-start)

test = 1500
run(data)