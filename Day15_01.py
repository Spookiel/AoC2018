regs = {"a":0, "b":0, "c":1, "d":0}

test = """cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a"""


data = """cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 14 c
cpy 14 d
inc a
dec d
jnz d -2
dec c
jnz c -5"""


def run(data, regs):
    lines = [i.split() for i in data.splitlines()]
    pos = 0
    while pos in range(len(lines)):
        line = lines[pos]
        if 'cpy' in line:
            try:
                int(line[1])
                regs[line[-1]] = int(line[1])
            except:
                regs[line[-1]] = regs[line[1]]
            pos += 1
        elif 'inc' in line:
            regs[line[-1]] += 1
            pos += 1
        elif 'dec' in line:
            regs[line[-1]] -= 1
            pos += 1
        elif 'jnz' in line:
            try:
                if int(line[1]) != 0:
                    pos += int(line[-1])
                else:
                    pos += 1
            except:
                if regs[line[1]] != 0:
                    pos += int(line[-1])
                else:
                    pos += 1
    print(regs)
run(data, regs)


