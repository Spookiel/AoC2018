from re import sub
import re



with open("Day13Input.txt", "r") as f:
    test = """"""
    for i in f:
        if i != "\\":
            test += i
        else:
            test += "]"
    print(test)
from collections import defaultdict


class Cart():
    def __init__(self, direction, x, y, cc):
        if direction == "^":
            self.direction = 0
            self.cc = True
        elif direction == "v":
            self.direction = 180
            self.cc = False
        elif direction == ">":
            self.direction = 90
            self.cc = False
        else:
            self.direction = 270
            self.cc = True
        self.x = x
        self.y = y

def intersection(cart):
    if memories[cart]==0:
        memories[cart] += 1
        return "left"
    elif memories[cart]==1:
        return "Straight"
        memories[cart] += 1
    else:
        memories[cart] += 1
        memories[cart] %= 2
        return "Right"

CartID = defaultdict(int)
def move(cart, grid):
    if cart.cc:
        if grid[cart.y][cart.x] = "|":
            cart.y -= 1
        elif grid[cart.y][cart.x] = "/":
            if cart.direction == 0:
                cart.x += 1
            elif cart.direction == 180:
                cart.x -= 1
            elif cart.direction == 90:
                cart.y += 1
            cart.direction += 90
            cart.direction %= 360
def run(data):
    counter = 0
    lines = [i for i in data.split('\n')]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] in ["v", "^", ">", "<"]:
                CartID[counter] = Cart(lines[i][j], j , i)
                counter +=1

    print(CartID)








run(test)