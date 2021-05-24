from bs4 import BeautifulSoup
from urllib.request import urlopen


class BugsMusic(object):
    url = ''

    @staticmethod
    def get_chart(soup, info):
        print(info)
        count = 0
        print('---------------')
        for link1 in soup.find_all(name='p', attrs=({"class": info})):
            count += 1
            print(f'{str(count)} {link1.find("a").text}')
        print('---------------')

    def __str__(self):
        return self.url

    @staticmethod
    def main():
        bugs = BugsMusic()
        while True:
            menu = input('0 종료 1. 입력 2. 음악순위(title or artist 입력)')
            if menu == '0':
                break
            elif menu == '1':
                bugs.url = input('Input URL')
                print(bugs.url)
            elif menu == '2':
                soup = BeautifulSoup(urlopen(bugs.url), 'lxml')
                bugs.get_chart(soup, input('title, artist'))

            else:
                break


BugsMusic.main()
