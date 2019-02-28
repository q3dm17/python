__author__ = 's.rozhin'
import BeautifulSoup as BeautifulSoup
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


def get_weather_html_from_rp5():
    session = requests.Session()
    agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) ' \
            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'
    headers = {'User-Agent': agent}
    session.headers.update(headers)
    weather_url = 'http://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%' \
                  '80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3%D0%B5'
    response = session.get(weather_url)
    text = response.text.encode('utf-8')
    with open('weather.html', 'w') as output_file:
        output_file.write(text)
    soup = BeautifulSoup.BeautifulStoneSoup(text)
    title = soup.findAll('div', {'id': 'pointNavi', 'class': 'pointNaviCont'})
    for elem in title:
        for header in elem.findAll('h1', {'class': 'inline'}):
            if header is None:
                pass
            else:
                pass # print header.getText()
    return text


def extract_tomorrow(page_html):
    soup = BeautifulSoup.BeautifulStoneSoup(page_html)
    tab = soup.find_all('div', {'id': 'ftab_6_content'})
    print tab
    table = tab[0].findChild('table', {'id': 'forecastTable'})
    print table
    print table.findChild('tbody')
    return 18, 24


if __name__ == '__main__':
    html = get_weather_html_from_rp5()
    tomorrow = extract_tomorrow(html)
    # get_top_250()
