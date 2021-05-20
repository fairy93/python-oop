# 이름, 전화번호, 이메일, 주소를 받아서연락처 입력, 출력, 삭제하는 프로그램을 완성하시오.
class Contacts(object):
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    @staticmethod
    def main():
        ls = []
        while True:
            n = input('프로그램종료 0번, 주소록 추가 1번, 주소록 출력 2번, 주소록 삭제 3번, 주소록 수정 4번')
            if n == '0':
                break
            elif n == '1':
                ls.append(Contacts(input('name'), input('phone_number'), input('email'), input('address')))
            elif n == '2':
                for i in ls:
                    print(f'{i.get_contact()}')
            elif n == '3':
                del_name = input('삭제할 이름을 입력하세요')
                for i, j in enumerate(ls):
                    if j.name == del_name:
                        del ls[i]
            elif n == '4':
                mo_name = input('수정할 주소록의 이름을 입력하세요')
                mo_info = Contacts(mo_name, input('수정할 전화번호 입력'), input('수정할 이메일 입력'), input('수정할 주소 입력'))
                for i, j in enumerate(ls):
                    if j.name == mo_name:
                        ls[i] = mo_info
            else:
                print('잘못된 선택입니다')
                continue

    def get_contact(self):
        return f'이름 : {self.name} 전화번호 : {self.phone_number} 이메일 : {self.email} 주소 : {self.address}'

    def del_contact(self):
        pass


Contacts.main()
