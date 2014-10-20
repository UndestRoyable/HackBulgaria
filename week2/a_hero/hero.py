class Hero:

    def __init__(self,name,health,nickname):
        self.name = name
        self.health = health
        self.nickname = nickname
        self._MAX_HEALTH = health
    def known_as(self):
        return "{} the {}".format(self.name, self.nickname)

    def get_health(self):
        return self.health

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def take_damage(self,damage_points):
        if damage_points > self.health:
            self.health = 0
            return self.health
        else:
            return self.health - damage_points

    def take_healing(self,healing_points):
        if self.health == 0:
            return False
        elif self.health + healing_points > 100:
            return False
        elif self.health + healing_points < 100:
            return True
        