import time
from threading import Thread
import requests


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemy = 100
        self.days = 0

    def run(self):
        print(f'{self.name}, на нас напали!')

        while self.enemy > 0:
            time.sleep(1)
            self.days += 1
            self.enemy -= self.power

            if self.enemy < 0:
                self.enemy = 0

            print(f'{self.name} сражается {self.days}..., осталось {self.enemy} воинов.')
        print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')