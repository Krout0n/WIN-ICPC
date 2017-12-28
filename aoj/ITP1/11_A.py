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
for order in list(input()):
    l = d.spin(order)
print(l)