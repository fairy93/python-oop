class Stock(object):
    def __init__(self, stock_name, stock_code):
        self.stock_name = stock_name
        self.stock_code = stock_code

    def get_stock(self):
        return f'종목명 {self.stock_name}, 종목코드 {self.stock_code}'

    @staticmethod
    def main():
        while True:
            n = input('프로그램종료0, 종목명과 종목코드 입력1, 종목명과 종목코드 출력2')
            print(n)
            if n == '0':
                break
            elif n == '1':
                s = Stock(input('종목명'), input('종목코드'))
            elif n == '2':
                print(s.get_stock())
            else:
                print('다시 입력하세요')
                continue


Stock.main()
