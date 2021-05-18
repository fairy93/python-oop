class CalculatorStatic(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def get_add(self):
        return self.first + self.second

    def get_sub(self):
        return self.first - self.second

    def get_mul(self):
        return self.first * self.second

    def get_div(self):
        return self.first / self.second

    @staticmethod
    def main():
        c = CalculatorStatic(int(input('첫번째 수 입력')), int(input('두번째 수 입력')))
        print(f'{c.first} + {c.second} = {c.get_add()}')
        print(f'{c.first} + {c.second} = {c.get_sub()}')
        print(f'{c.first} + {c.second} = {c.get_mul()}')
        print(f'{c.first} + {c.second} = {c.get_div()}')


CalculatorStatic.main()
