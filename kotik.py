import random

class Cat:

    def __init__(self,name):

        self.name=name

        self.gladness=50

        self.famine=10

        self.alive=True

        self.energy=50


    def to_sleep(self):

    print('Час спати')

self.gladness+=3

self.famine-=0.2

self.energy+=5


        def to_chill(self):

    print('Час відпочивати')

self.gladness+=5

self.famine-=0.3

self.energy+=2

def to_eat(self):

    print('Час їсти')

self.gladness+=4

self.famine+=5

self.energy+=3

def to_play(self):

    print('Час гратись')

self.gladness-=5

self.famine-=3

self.energy-=5


def is_alive(self):

if self.famine<-1.5:

print('Кіт без їди це ніхто!')

self.alive=False

elif self.gladness<=0:

print('Дипресія.')

self.alive=False

elif self.energy>500:

print('Дуже сильний.')

self.alive=False

elif self.energy<0:

print('Нема сил...')

self.alive=False

elif self.famine>200:

print('З дому вигнали.. обжора..')

self.alive=False


def end_of_day(self):

print(f'Gladness - {self.gladness}')

print(f'Famine - {round(self.famine,2)}')

print(f'Energy - {round(self.energy, 3)}')


def live(self,day):

day='Day ' +str(day) + ' of ' + self.name + ' live'

print(f'{day:^50}')

live_cube=random.randint(1,4)

if live_cube==1:

self.to_eat()

elif live_cube==2:

self.to_sleep()

elif live_cube==3:

self.to_chill()

elif live_cube==4:

self.to_play()

self.end_of_day()

self.is_alive()


Teo=Cat(name='Teo')

for day in range(365):

    if Teo.alive==False:

    break

Teo.live(day)



