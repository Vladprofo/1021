import random
class Human:
    def __init__(self, Vladik="Human", job=None,home=None):
        self.name = Vladik
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
    def get_home(self):
        self.home = House()

    def get_job(self):
        if self.carel.shopping():
            pass
        else:
            self.to_shopping()
            return
        self.job = Job("job_list")

    def eat(self):
        if self.home.food<=0:
            self.shopping("food")
        else:
            if self.satiety>=100:
                self.satiety=100
                return
            self.satiety+=5
            self.home.food-=5
    def work(self):
        if self.carel.shopping():
            pass
        else:
            if self.carel:
                self.shopping("food")
                return
        self.money+=self.job.salary
        self.gladness-=self.job.gladness_less
        self.satiety-=4
    def shopping(self,manage):
        if self.carel.shopping():
            pass
        else:
            if self.carel:

                self.to_shopping()
                return
        if manage=="food":
            print("Купив їжу")
            self.money-=50
            self.home.food+=50
        elif manage=="delicacies":
            print("Ура!")
            self.gladness+=10
            self.satiety+=2
            self.money-=15

    def chill(self):
        self.gladness+=24
        self.home.mess+=8
    def clean_home(self):
        self.gladness-=8
        self.home.mess=3

    def days_indexes(self,day):
        day=f"Today the {day} of {self.name}'s life"
        print(f"{day:=^50}","\n")
        human_indexes=self.name+" 's indexes"
        print(f"{human_indexes:^50}","\n")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        home_indexes="Home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Food - {self.home.food}")
        print(f"Rooms - {self.home.rooms}")
    def is_alive(self):
        if self.gladness<0:
            print("Дипресія...")
            return False
        elif self.satiety<0:
            print("Голод...")
            return False
        elif self.money<-500:
            print("Банкрот...")
            return False
    def live(self,day):
        if self.is_alive()==False:
            return False
        if self.home is None:
            print("Заселення в будинок")
            self.get_home()
        if self.job is None:
            self.get_job()
            print(f" я йду отримувати роботу{self.job.job}, з зарплатою {self.job.salary}")
        self.days_indexes(day)
        dice=random.randint(1,4)
        if self.satiety<20:
            print("Я йду їсти")
            self.eat()
        elif self.gladness<20:
            if self.home.mess>15:
                print("Хочеться відпочити але в будинку безлад, тому я буду прибирати")
                self.clean_home()
            else:
                print(" Я відпочину")
                self.chill()
        elif self.money<0:
            print("Час працювати")
            self.work()
        elif dice==1:
            print(" Я відпочину")
            self.chill()
        elif dice==2:
            print("Час працювати")
            self.work()
        elif dice==3:
            print(" я буду прибирати")
            self.clean_home()
        elif dice==4:
            print("Час смаколиків")
            self.shopping(manage="delicacies")









class House:
    def __init__(self):
        self.mess=3
        self.food=("carrot,potato,crisps,koka kola,chocolate")




class Job:
    def __init__(self, job_list):

        self.salary=job_list[self.job]["salary"]


Vlad=Human(name="Vlad")
for day in range(1,8):
    if Vlad.live(day)==False:
        break