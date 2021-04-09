import sys
from datetime import datetime
from urllib.request import Request, urlopen

#
# def error(e):
#     print(e)
    # print(f'{e} : {datetime.now()}', file=sys.stderr)  # 함수 stdin, stdou, stderr 찾아보기


def crawling(
        url='',
        encoding='utf-8',
        err=lambda e: print(e)):  # 간단한 기능을 가진 함수는, lambda함수로 이름없이 쓸 수 있다.
    try:
        request = Request(url)
        response = urlopen(request)
        print(f'{datetime.now()}: success for request[{url}]')

        receive = response.read()
        return receive.decode(encoding, errors='replace')  # errors='replace' : encoding이 틀렸을때 자동으로 알아서 찾아서 인코딩함

    except Exception as e:
        if err is not None:
            err(e)

