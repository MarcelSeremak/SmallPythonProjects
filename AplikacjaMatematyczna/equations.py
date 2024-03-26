import random

class Equations():
    def __init__(self, mode):
        self.mode = mode
        self.result = 0

        if mode == "easy":
            self.a = random.randint(5, 10)
            self.b = random.randint(5, 10)
            self.c = random.randint(5, 10)

        elif mode == "medium":
            self.a = random.randint(5, 13)
            self.b = random.randint(5, 13)
            self.c = random.randint(5, 13)

        elif mode == "hard":
            self.a = random.randint(5, 16)
            self.b = random.randint(5, 16)
            self.c = random.randint(5, 16)

        self.listOfHardness = ["OneOperation", "TwoOperations"]
    def pickEq(self):
        if self.mode == "easy":
            picked = random.choices(self.listOfHardness, weights=[70, 30], k=1)[0]
            if picked == "OneOperation":
                sign1 = random.choices(["+", "-", "*"], weights=[20, 30, 50])[0]
                res = f"{self.a} {sign1} {self.b}"
                self.result=eval(f"{self.a} {sign1} {self.b}")
            else:
                sign1 = random.choices(["+", "-", "*"], weights=[30, 30, 40])[0]
                sign2 = random.choices(["+", "-", "*"], weights=[30, 30, 40])[0]
                res = f"({self.a} {sign1} {self.b}) {sign2} {self.c}"
                self.result=eval(f"( {self.a} {sign1} {self.b} ) {sign2} {self.c}")
            self.a = random.randint(5, 10)
            self.b = random.randint(5, 10)
            self.c = random.randint(5, 10)
            return res


        elif self.mode == "medium":
            picked = random.choices(self.listOfHardness, weights=[60, 40], k=1)[0]
            if picked == "OneOperation":
                sign1 = random.choices(["+", "-", "*"], weights=[10, 20, 70])[0]
                res = f"{self.a} {sign1} {self.b}"
                self.result = eval(f"{self.a} {sign1} {self.b}")
            else:
                sign1 = random.choices(["+", "-", "*"], weights=[10, 10, 80])[0]
                sign2 = random.choices(["+", "-", "*"], weights=[20, 20, 60])[0]
                res = f"({self.a} {sign1} {self.b}) {sign2} {self.c}"
                self.result = eval(f"( {self.a} {sign1} {self.b} ) {sign2} {self.c}")
            self.a = random.randint(5, 13)
            self.b = random.randint(5, 13)
            self.c = random.randint(5, 13)
            return res

        else:
            picked = random.choices(self.listOfHardness, weights=[60, 40], k=1)[0]
            if picked == "OneOperation":
                sign1 = random.choices(["+", "-", "*"], weights=[10, 20, 70])[0]
                self.result = eval(f"{self.a} {sign1} {self.b}")
                res =  f"{self.a} {sign1} {self.b}"
            else:
                sign1 = random.choices(["+", "-", "*"], weights=[20, 20, 60])[0]
                sign2 = random.choices(["+", "-", "*"], weights=[20, 20, 60])[0]
                self.result = eval(f"( {self.a} {sign1} {self.b} ) {sign2} {self.c}")
                res = f"({self.a} {sign1} {self.b}) {sign2} {self.c}"
            self.a = random.randint(5, 15)
            self.b = random.randint(5, 15)
            self.c = random.randint(5, 15)
            return res


