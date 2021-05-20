import random


class Account(object):
    def __init__(self, name, balance):
        self.bank_name = 'sc은행'
        self.name = name
        self.account_number = str(format(random.randint(0, 999), '03')) + '-' + str(format(random.randint(0, 99), '02')) + '-' + str(format(random.randint(0, 999999), '06'))
        self.balance = balance

    def get_account(self):
        return f'{self.bank_name} {self.name} {self.account_number} {self.balance}'

    @staticmethod
    def main():
        ls = []
        while True:
            random
            n = input('프로그램 종료 0번, 예금자정보를 입력 1번, 예금자정보를 출력 2번')
            if n == '0':
                break
            elif n == '1':
                ls.append(Account(input('예금자명을 입력하세요'), input('잔액을 입력하세요')))
            elif n == '2':
                for i in ls:
                    print(i.get_account())
            else:
                print('잘못된 입력입니다')
                continue


Account.main()
