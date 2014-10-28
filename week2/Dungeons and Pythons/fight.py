import random
from hero import Hero 
from orc import Orc 

class Fight:

    def __init__(self,hero,orc):

        self.hero = hero
        self.orc = orc

    def attacks_first(self):
        return random.randrange(0, 100) < 50

    def simulate_fight(self):
        if self.attacks_first():
            print("{} attacks first!".format(self.hero.known_as()))
            
            while self.hero.is_alive() and self.orc.is_alive():
                self.hero.take_damage(self.orc.attack())
                self.orc.take_damage(self.hero.attack())
        else:
            print("{} attacks first!".format(self.orc.name))
            while self.hero.is_alive() and self.orc.is_alive():
                self.hero.take_damage(self.orc.attack())
                self.orc.take_damage(self.hero.attack())

    def get_winner(self):
        if self.hero.is_alive() and self.orc.is_alive() == False:
            winner = self.hero.name
            print(winner)
        if self.orc.is_alive() and self.hero.is_alive() == False:
            winner = self.orc.name
            print(winner)
