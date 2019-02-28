__author__ = 's.rozhin'
import requests
from itertools import takewhile
from collections import Counter


def fetch_messages():
    s = requests.session()
    repeat_count = 0
    found = set()
    while True:
        req = s.get('http://whatthecommit.com/index.txt')
        message = req.text.encode('utf-8')
        if message not in found:
            repeat_count = 0
            found.add(message)
            yield message
        else:
            print("Repeat: " + message)
            if repeat_count < 10:
                repeat_count += 1
                continue
            else:
                return


def save_bok():
    s = requests.session()
    for x in range(1, 53):
        req = s.get('https://www.e-reading.club/chapter.php/61279/{}/Haiinlaiin_-_Luna_zhestko_stelet.html'.format(x))
        message = req.text.encode('utf-8')
        with open("moon/{}.html".format(x), 'w') as f:
            f.write(message)

def save_bok_old():
    s = requests.session()
    for x in range(0, 103):
        req = s.get('http://knizhnik.org/stiven-king/pod-kupolom/{}'.format(x))
        message = req.text.encode('utf-8')
        with open("under_the_dome/{}.html".format(x), 'w') as f:
            f.write(message)


def save_messages(total):
    with open('messages.txt', 'w') as output_file:
        for message in fetch_messages():
            output_file.write(message)
            total += 1
    print('Total messages %d' % total)


def pass_str(data):
    if len(data) < 10:
        return False
    if data.isdigit() or data.isalpha():
        return False
    if data.isupper() or data.islower():
        return False
    return True


def two_monkeys(asmile, bsmile):
    return not asmile ^ bsmile


def most_difference(*args):
    if len(args) <= 1:
        return 0
    minimal = args[0]
    maximal = args[0]
    for x in args:
        minimal = min(minimal, x)
        maximal = max(maximal, x)
    return maximal - minimal


def non_unique(data):
    def get_non_unique(list):
        elements = set()
        for x in list:
            element = str(x).lower()
            if element in elements:
                yield element
            else:
                elements.add(element)

    non_unique = set(get_non_unique(data))
    return list(filter(lambda x: str(x).lower() in non_unique, data))


def count_units(number):
    return bin(number).count("1")

#def most_frequent(text: str) -> str:
def most_frequent(text):
    freqs = Counter([x for x in text.lower() if x.isalpha()])
    ordered = sorted(freqs.items(), key=lambda kv: kv[1], reverse=True)
    most_frequent = ordered[0][1]
    candidates = list([x[0] for x in takewhile(lambda x: x[1] == most_frequent, ordered)])
    return sorted(candidates)[0]


#def count_words(text: str, words: set) -> int:
def count_words(text, words):
    lower = text.lower()
    return sum(1 for x in words if x in lower)

#def long_repeat(line: str) -> int:
def long_repeat(line):
    if len(line) == 0:
        return 0
    prev = ""
    longest = 1
    current = 1
    for c in line:
        if c == prev:
            current += 1
            longest = max(current, longest)
        else:
            current = 1
            prev = c
    return longest


def clock_angle(time):
    hours_str, minutes_str = time.split(":")
    hours = float(hours_str) % 12
    minutes = float(minutes_str)
    minutes_hand_angle = minutes / 60
    hours_hand_angle = hours / 12 + minutes / 720
    angle_between = max(hours_hand_angle, minutes_hand_angle) - min(hours_hand_angle, minutes_hand_angle)
    if angle_between < 0.5:
        return round(angle_between * 360, 1)
    else:
        return round((1 - angle_between) * 360, 1)


def convert(str_number, radix):
    for c in str_number:
        if c.isdigit() and ord(c) >= radix + 48:
            return -1
        if c.isalpha() and ord(c.lower()) > radix + 87:
            return -1
    return int(str_number, radix)


def symb_exchange(line):
    return line[-1:] + line[1:-1] + line[:1]


def rotate_list(elements, rotates):
    return elements[rotates::] + elements[:rotates:]

def checkio(data):
    def sub_func(data, step):
        if len(data) == step:
            return 0
        return data[step] + sub_func(data, step+1)
    return sub_func(data, 0)


def main():
    save_bok()


if __name__ == '__main__':
    main()
