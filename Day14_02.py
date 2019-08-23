data = """"""
test = [3, 7]
import time
start = time.time()

def run(data):
    recipe = list(map(int, input("Enter value: ")))
    elf1, elf2  = 0, 1
    flag = False
    while True:
        data += [int(i) for i in str(data[elf1]+data[elf2])]
        elf1, elf2 = (1+data[elf1]+elf1)%len(data), (1+data[elf2]+elf2)%len(data)

        if data[-len(recipe):] == recipe or data[-len(recipe) - 1:-1] == recipe:
            break

    if data[-len(recipe):] == recipe:
        print(len(data) - len(recipe))
    else:
        print(len(data) - len(recipe) - 1)
    print(len(data))







run(test)

print(time.time()-start)