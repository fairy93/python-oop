import random


class Account(object):
    def __init__(self, name, balance):
        self.BANK_NAME = 'SC은행'
        self.name = name
        self.account_number = str(format(random.randint(0, 999), '03')) + '-' + str(
            format(random.randint(0, 99), '02')) + '-' + str(format(random.randint(0, 999999), '06'))
        self.balance = balance

    def get_account(self):
        return f'{self.BANK_NAME} {self.name} {self.account_number} {self.balance}'

    @staticmethod
    def modify_element(ls, account_number):
        for i, j in enumerate(ls):
            if j.account_number == account_number:
                return ls[i]

    @staticmethod
    def main():
        ls = []
        while True:
            menu = input('0.종료 1.계좌개설 2.계좌목록 3.입금 4.출금 5. 계좌탈퇴')
            if menu == '0':
                break
            elif menu == '1':
                ls.append(Account(input('예금자명을 입력하세요'), input('잔액을 입력하세요')))
            elif menu == '2':
                for i in ls:
                    print(i.get_account())
            elif menu == '3':
                account_number = input('입금할 계좌번호')
                money = input('입금액 입력바랍니다')
                account = Account.modify_element(ls, account_number)
                if account:
                    account.balance = int(money) + int(account.balance)
            elif menu == '4':
                account_number = input('출금할 계좌번호')
                money = input('출금액 입력바랍니다')
                account = Account.modify_element(ls, account_number)
                if account:
                    account.balance = int(account.balance) - int(money)
            elif menu == '5':
                account = Account.modify_element(ls, input('출금할 계좌번호'))
                if account:
                    ls.remove(account)
            else:
                print('잘못된 입력입니다')
                continue


Account.main()
