class Entity:

    def __init__(self,name,health):
        self.name = name
        self.health = health

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