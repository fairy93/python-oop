def add_func(first, second):
    return first + second


def sub_func(first, second):
    return first - second


def mul_func(first, second):
    return first * second


def div_func(first, second):
    return first / second


class Calculator(object):

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def get_add(self):
        return self.first + self.second

    def get_dub(self):
        return self.first - self.second

    def get_mul(self):
        return self.first * self.second

    def get_div(self):
        return self.first / self.second


if __name__ == '__main__':
    c = Calculator(5, 3)
    print(c.get_add())  # oop
    print(c.get_dub())
    print(c.get_mul())
    print(c.get_div())
    print(add_func(5, 3))  # 함수형 프로그래밍
    print(sub_func(5, 3))
    print(mul_func(5, 3))
    print(div_func(5, 3))
