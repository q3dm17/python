__author__ = 's.rozhin'
import requests


def get_top_250():
    session = requests.Session()
    agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'
    headers = {'User-Agent': agent}
    session.headers.update(headers)
    responce = session.get('http://www.kinopoisk.ru/top/')
    text = responce.text.encode('utf-8')
    with open('log.txt', 'w') as output_file:
        output_file.write(text)


if __name__ == '__main__':
    get_top_250()
