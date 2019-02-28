import itertools

MORSE_CODE = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G", "....": "H",
              "..": "I", ".---": "J", ".-.": "R", "..-": "U", "-.--": "Y"}


def decodeMorse(morseCode):
    if not morseCode: return ""
    return " ".join(
        map(
            lambda word: decode_word(word),
            morseCode.strip(" ").split("   ")))


def decode_word(word):
    return "".join(
        map(
            lambda letter: MORSE_CODE[letter],
            word.split(" ")))


from itertools import takewhile


def solution(string, markers):
    marks = set(generate_chars(markers))
    return "\n".join(drop_comment(x, marks).rstrip(" ") for x in string.splitlines())


def generate_chars(markers):
    for string in markers:
        for x in string:
            yield x


def drop_comment(string, marks):
    return "".join(takewhile(lambda x: x not in marks, string))


class User:
    _ranks = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self):
        self._rank_step = 0
        self._progress = 0

    @property
    def progress(self):
        return self._progress

    @property
    def rank(self):
        return User._ranks[self._rank_step]

    def inc_progress(self, rank):
        difference = self._rank_step - User._get_rank_pos(rank)
        if difference >= 2:
            increment = 0
        elif difference == 1:
            increment = 1
        elif difference == 0:
            increment = 3
        else:
            increment = 10 * difference * difference
        self._progress += increment
        self._on_progress_update()

    def _on_progress_update(self):
        rank_increase = self._progress // 100
        self._progress %= 100
        if self._rank_step != len(User._ranks) - 1:
            self._rank_step += rank_increase
        if self._rank_step == len(User._ranks) - 1:
            self._progress = 0

    @staticmethod
    def _get_rank_pos(rank):
        for index in range(0, len(User._ranks)):
            if User._ranks[index] == rank:
                return index
        raise AssertionError

def main():
    print(list("aaa\nbbb\nsome new text\n".splitlines()))
    print(solution('apples, pears \xc2\xa7 and bananas\ngrapes\navocado', ['*', '\xc2\xa7']))


if __name__ == '__main__':
    main()
