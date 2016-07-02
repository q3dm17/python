__author__ = 's.rozhin'
import requests


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
            print "Repeat: " + message
            if repeat_count < 10:
                repeat_count += 1
                continue
            else:
                return


def main():
    total = 0
    with open('messages.txt', 'w') as output_file:
        for message in fetch_messages():
            output_file.write(message)
            total += 1
    print ('Total messages %d' % total)


if __name__ == '__main__':
    main()
