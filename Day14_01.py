data = """"""
test = [3, 7]


def run(data):
    real = int(input("Enter value: "))
    elf1, elf2  = 0, 1

    while True:
        data += [int(i) for i in str(data[elf1]+data[elf2])]
        elf1, elf2 = (1+data[elf1]+elf1)%len(data), (1+data[elf2]+elf2)%len(data)

        if len(data)-10 == real:
            print("".join([str(i) for i in data[-10:]]))
            break
        elif len(data)-10 > real:
            print("".join([str(i) for i in data[-11:-1]]))
            break







run(test)