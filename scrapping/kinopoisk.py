# coding=utf-8
import BeautifulSoup as BeautifulSoup
import requests

list_date = 'http://www.kinopoisk.ru/user/%d/votes/list/ord/date/page/%d/'
list_rate = 'http://www.kinopoisk.ru/user/%d/votes/list/ord/kp/page/%d/'


class UserWalker:
    def __init__(self, user_id):
        self.session = requests.Session()
        agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'
        headers = {'User-Agent': agent}
        self.session.headers.update(headers)
        self.user_id = user_id

    def get_rating_page(self, page_num=1):
        request = self.session.get(list_rate % (self.user_id, page_num))
        return request.text.encode('utf-8')


def contain_movies_data(text):
    soup = BeautifulSoup.BeautifulStoneSoup(text)
    film_list = soup.findAll('div', {'class': 'rating'})
    for film in film_list:
        print film
    return film_list is not None


walker = UserWalker(3419734)

contain_movies_data(walker.get_rating_page())


def read_file(filename):
    """Reads whole file"""
    with open(filename) as input_file:
        text = input_file.read()
    return text


def parse_user_datafile_bs(filename):
    results = []
    text = read_file(filename)

    soup = BeautifulSoup(text)
    film_list = soup.find('div', {'class': 'profileFilmsList'})
    items = film_list.find_all('div', {'class': ['item', 'item even']})
    for item in items:
        # getting movie_id
        movie_link = item.find('div', {'class': 'nameRus'}).find('a').get('href')
        movie_desc = item.find('div', {'class': 'nameRus'}).find('a').text
        movie_id = re.findall('\d+', movie_link)[0]

        # getting english name
        name_eng = item.find('div', {'class': 'nameEng'}).text

        # getting watch time
        watch_datetime = item.find('div', {'class': 'date'}).text
        date_watched, time_watched = re.match('(\d{2}\.\d{2}\.\d{4}), (\d{2}:\d{2})', watch_datetime).groups()

        # getting user rating
        user_rating = item.find('div', {'class': 'vote'}).text
        if user_rating:
            user_rating = int(user_rating)

        results.append({
            'movie_id': movie_id,
            'name_eng': name_eng,
            'date_watched': date_watched,
            'time_watched': time_watched,
            'user_rating': user_rating,
            'movie_desc': movie_desc
        })
    return results

