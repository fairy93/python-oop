class Stock(object):
    def __init__(self, stock_name, code):
        self.stock_name = stock_name
        self.code = code

    def get_stock(self):
        return f'종목명 {self.stock_name}, 종목코드 {self.code}'

    @staticmethod
    def modify_element(ls, code):
        for i, j in enumerate(ls):
            if j.code == code:
                return ls[i]

    @staticmethod
    def main():
        ls = []
        while True:
            menu = input('0.Exit 1.Create 2.Read 3.Update 4.Delete')
            if menu == '0':
                break
            elif menu == '1':
                ls.append(Stock(input('종목명'), input('종목코드')))
            elif menu == '2':
                for i in ls:
                    print(i.get_stock())
            elif menu == '3':
                edit_code = input('수정할 종목코드')
                stock = Stock.modify_element(ls, edit_code)
                if stock:
                    stock.stock_name = (input('수정할 종목이름'))
            elif menu == '4':
                stock = Stock.modify_element(ls, input('삭제할 종목코드'))
                if stock:
                    ls.remove(stock)
            else:
                print('다시 입력하세요')
                continue


Stock.main()
