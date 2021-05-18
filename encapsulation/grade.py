class Grade(object):

    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum_grade(self):
        return self.kor + self.eng + self.math

    def avg_garde(self):
        return self.sum_grade() / 3

    def get_grade(self):
        score = int(self.avg_garde())
        grade = ''
        if score >= 90:
            grade = 'A학점'
        elif score >= 80:
            grade = 'B학점'
        elif score >= 70:
            grade = 'C학점'
        elif score >= 60:
            grade = 'D학점'
        else:
            grade = 'F학점'
        return grade

    @staticmethod
    def main():
        g = Grade(int(input('국어 점수 입력')), int(input('영어 점수 입력')), int(input('수학 점수 입력')))
        print(f'세 과목의 총점은 {g.sum_grade()}')
        print(f'세 과목의 평균은 {g.avg_garde()}')
        print(f'학점은 {g.get_grade()}')


Grade.main()
