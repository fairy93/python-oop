'''
이름, 태어난년도, 주소를 입력받아
이름, 나이, 주소를 출력 해보세요
'''


class Person(object):

    def __init__(self, name, year, address):
        self.name = name
        self.year = year
        self.address = address

    def get_age(self):
        return 2021 - self.year

    @staticmethod
    def main():
        p = Person(input('이름을 입력하세요'), int(input('태어난 년도를 입력하세요')), input('주소를 입력하세요'))
        print(f'이름은 {p.name}')
        print(f'나이는 {p.get_age()}')
        print(f'주소는 {p.address}')


Person.main()
