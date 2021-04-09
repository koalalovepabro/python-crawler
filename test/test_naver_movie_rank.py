from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from collection import crawler


def ex01():
    request = Request("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")
    response = urlopen(request)
    html = response.read().decode('cp949')
    # print(html)

    bs = BeautifulSoup(html, 'html.parser')
    divs = bs.findAll('div', attrs={'class': 'tit3'})

    for index, div in enumerate(divs): # enumerate : 자동으로 인덱싱 해주는 함수
        print(index+1, div.a.text, div.a['href'], sep=':')  # sep 지정 안해주면 슬래쉬(/)로 구분됨.


def ex02():
    html = crawler.crawling(
        url="https://movie.naver.com/movie/sdb/rank/rmovie.nhn",
        encoding='cp949')  # crwler.py에서 정의 해 준 함수 참고

    # print(html)

    bs = BeautifulSoup(html, 'html.parser')
    divs = bs.findAll('div', attrs={'class': 'tit3'})

    for index, div in enumerate(divs): # enumerate : 자동으로 인덱싱 해주는 함수
        print(index+1, div.a.text, div.a['href'], sep=':')  # sep 지정 안해주면 슬래쉬(/)로 구분됨.


if __name__=='__main__':
    # ex01()
    ex02()