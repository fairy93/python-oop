class Grade:
    def setGrade(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def sumGrade(self):
        return self.kor + self.eng + self.math

    def avgGarde(self):
        return self.sumGrade() / 3;


if __name__ == '__main__':
    a = Grade()
    a.setGrade(100, 80, 70)
    print(a.sumGrade())
    print(a.avgGarde())
