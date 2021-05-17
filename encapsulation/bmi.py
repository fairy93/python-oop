class Bmi:
    def setBmi(self, height, weight):
        self.height = height
        self.weight = weight

    def resBmi(self):
        return self.weight / self.height * self.height


if __name__ == '__main__':
    b = Bmi()
    b.setBmi(174, 68)
    print(b.resBmi())
