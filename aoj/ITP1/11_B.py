import random

class Dice():
    
    def __init__(self, *n):
       self.rolls = n

    def spin(self, order):
        if order == "N":
            self.rolls = [
                self.rolls[1],
                self.rolls[5],
                self.rolls[2],
                self.rolls[3],
                self.rolls[0],
                self.rolls[4]
            ]
        if order == "E":
            self.rolls = [
                self.rolls[3],
                self.rolls[1],
                self.rolls[0],
                self.rolls[5],
                self.rolls[4],
                self.rolls[2]
            ]
        if order == "S":
            self.rolls = [
                self.rolls[4],
                self.rolls[0],
                self.rolls[2],
                self.rolls[3],
                self.rolls[5],
                self.rolls[1]
            ]
        if order == "W":
            self.rolls = [
                self.rolls[2],
                self.rolls[1],
                self.rolls[5],
                self.rolls[0],
                self.rolls[4],
                self.rolls[3]
            ]
        return self.rolls[0]

d = Dice(*[int(i) for i in input().split()])
directions = ['N','E','S','W']
for _ in range(int(input())):
    a,b = [int(i) for i in input().split()]
    while a != d.rolls[0] or d.rolls[1] != b:
        d.spin(directions[random.randint(0,3)])
    print(d.rolls[2])