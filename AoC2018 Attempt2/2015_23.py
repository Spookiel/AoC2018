
data = """jio a, +16
inc a
inc a
tpl a
tpl a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
tpl a
tpl a
inc a
jmp +23
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
tpl a
inc a
inc a
tpl a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
tpl a
tpl a
inc a
jio a, +8
inc b
jie a, +4
tpl a
inc a
jmp +2
hlf a
jmp -7"""

test = """inc a
jio a, +2
tpl a
inc a"""

def run(data):
    lines = [i.split() for i in data.splitlines()]
    regs = {"a": 0, "b": 0}
    pos = 0
    while pos > -1 and pos < len(lines)+1:

        line = lines[pos]
        print(line, regs)
        if "inc" in line:
            regs[line[1]] += 1
            pos += 1
        elif "tpl" in line:
            regs[line[1]] *= 3
            pos += 1
        elif "hlf" in line:
            pos += 1
            regs[line[1]] = regs[line[1]] // 2
        elif "jmp" in line:
            pos += int(line[-1])
        elif "jio" in line:
            r = line[1][:-1]

            if regs[r]%2==1:
                pos += int(line[-1])
            else:
                pos += 1
        elif "jie" in line:
            r = line[1][:-1]
            if regs[r]%2==0:
                pos += int(line[-1])
            else:
                pos += 1
    print(regs)


run(data)

