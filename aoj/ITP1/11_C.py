class Dice():
    
    def __init__(self, *n):
       self.rolls = n
    
    def __iter__(self):
        return self.rolls

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
