def bmi_function(height, weight):
    return weight / (height * height) * 10000


class Bmi(object):

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def get_bmi(self):
        return self.weight / (self.height * self.height) * 10000

    def get_decision(self):
        bmi = int(self.get_bmi())
        decision = ''
        if bmi >= 35:
            decision = '고도 비만'
        elif bmi >= 30:
            decision = '중(重)도 비만 (2단계 비만)'
        elif bmi >= 25:
            decision = '경도 비만'
        elif bmi >= 23:
            decision = '과체중'
        elif bmi >= 18.5:
            decision = '정상'
        else:
            decision = '저체중'
        return decision

    @staticmethod
    def main():
        b = Bmi(int(input('키(cm)를 입력하세요')), int(input('몸무게(kg)를 입력하세요')))
        print(b.get_bmi())
        print(b.get_decision())


Bmi.main()
