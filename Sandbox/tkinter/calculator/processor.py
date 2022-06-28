
class Processor:

    def __init__(self):
        self.invoer = 0
        self.stored = 0
        self.display = 0
        self.operator = ''
        self.decimal = False

    def getDisplay(self):
        return f'{self.display:g}'

    def keyPressed(self, key):
        if key in '1234567890':
            self.invoer = self.invoer * 10 + int(key)
            self.display = self.invoer

        elif key in '+-x÷=':
            self.calculate()
            self.operator = key
            self.invoer = 0
            self.display = self.stored
            self.decimal = False

        elif key == '.':
            self.decimal = True

        elif key == 'AC':
            self.invoer = 0
            self.stored = 0
            self.operator = ""
            self.display = self.stored
            self.decimal = False

        elif key == '+/-':
            self.invoer = -self.invoer
            self.display = self.invoer

        elif key == '%':
            self.invoer = self.invoer / 100
            self.display = self.invoer

    def calculate(self):
        if self.operator == '+':
            self.stored += self.invoer
        elif self.operator == '-':
            self.stored -= self.invoer
        elif self.operator == 'x':
            self.stored *= self.invoer
        elif self.operator == '÷':
            self.stored /= self.invoer
        elif self.operator == "=" or self.operator == "":
            self.stored = self.display
