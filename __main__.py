import time
from datetime import datetime
from itertools import count

from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

from collection import crawler


def crawling_pelicana():
    results = []

    for index in count(start=110, step=1):
        url = f'https://pelicana.co.kr/store/stroe_search.html?page={index}&branch_name=&gu=&si='
        html = crawler.crawling(url)

        bs = BeautifulSoup(html, 'html.parser')
        tag_table = bs.find('table', attrs={'class': ['table', 'mt20']})
        tag_tbody = tag_table.find('tbody')
        tags_tr = tag_tbody.findAll('tr')


        # 끝 검출
        if len(tags_tr) ==0 :
            break

        for tag_tr in tags_tr:
            datas = list(tag_tr.strings)  # 태그 없앤 후 개행으로 리스트에 담기

            name = datas[1]
            address = datas[3]
            sidogugun = address.split()[:2] # split 한 주소를 필요한 시.도.구 까지만 슬라이싱

            t = (name, address) + tuple(sidogugun)
            results.append(t)

    # store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gugun'])
    table.to_csv('results/pelicana.csv', encoding='utf-8', mode='w', index=True)

def crawling_nene():
    pass

def crawling_kyochon():
    pass

def crawling_goobne():

    # Chrome 브라우저 시작
    url = 'https://www.goobne.co.kr/store/search_store.jsp'
    wd = webdriver.Chrome('C:\\Users\\dorothy\\PycharmProjects\\chromedriver_win32\\chromedriver')

    # 페이지 이동
    wd.get(url)
    time.sleep(3)
    results = []

    for index in count(start=1, step=1):
        # 자바 스크립트 실행
        script = f'store.getList({index})'
        wd.execute_script(script)
        print(f'{datetime.now()}: success for request[{script}]')
        time.sleep(3)

        # 자바스크립트 실행된 HTML (동적으로 렌더링된 HTML) 가져오기
        html = wd.page_source

        # 파싱하기(bs4)
        bs = BeautifulSoup(html, 'html.parser')
        tag_tbody = bs.find('tbody', attrs={'id': 'store_list'})
        tags_tr = tag_tbody.findAll('tr')

        # 끝 검출
        if tags_tr[0].get('class') is None:
            break

        for tag_tr in tags_tr:
            datas = list(tag_tr.strings)

            name = datas[1]
            address = datas[6]
            sidogugun = address.split()[:2]

            t = (name, address) + tuple(sidogugun)
            results.append(t)

    # 브라우저 닫기
    wd.close()

    # store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gugun'])
    table.to_csv('results/goobne.csv', encoding='utf-8', mode='w', index=True)

if __name__ == '__main__':
    crawling_nene()
    # crawling_kyochon()
    # crawling_pelicana()
    # crawling_goobne()
