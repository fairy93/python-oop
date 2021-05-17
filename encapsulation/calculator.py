class Calculator:
    def setdata(self, first, second):
        self.first = first
        self.second =second

    def addCalc(self):
        return self.first + self.second

    def mulCalc(self):
        return self.first - self.second

    def subCalc(self):
        return self.first * self.second

    def divCalc(self):
        return self.first / self.second

if __name__ == '__main__':
    c = Calculator()
    c.setdata(3, 5)
    print(c.add())
    print(c.mul())
    print(c.sub())
    print(c.div())
