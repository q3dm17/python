# coding=utf-8
__author__ = 's.rozhin'

import random


class randomwalk_iter:
    def __init__(self):
        self.last = 1
        self.rand = random.random()

    def __iter__(self):
        return self  # создание простейшего итератора

    def next(self):
        if self.rand < 0.1:  # указатель предела
            print 'stopping iteration'
            raise StopIteration  # конец итерации
        else:  # поиск подходящего кандидата
            while abs(self.last - self.rand) < 0.4:
                print '*',  # отобразить отклонение
                self.rand = random.random()  # новый кандидат
            self.last = self.rand  # обновление предшествующего значения
            return self.rand


for num in randomwalk_iter():
    print num