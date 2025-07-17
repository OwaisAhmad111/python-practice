#..."Abstraction", hiding the implementation details of a class and only showing the essential features to the user...

class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.acc = True
        self.brk = True
        self.clutch = True
        print("Car is started")

c1 = car()
c1.start()

# Encapsulation, Wraping data and function in to single unit (object).



