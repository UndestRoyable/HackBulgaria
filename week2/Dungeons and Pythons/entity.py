class Entity:

    def __init__(self, name, health, weapon=None):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.fight_health = health

    def get_health(self):
        return self.fight_health

    def is_alive(self):
        if self.fight_health > 0:
            return True
        return False

    def take_damage(self, damage_points):
        if damage_points > self.fight_health:
            self.fight_health = 0
            return self.fight_health
        else:
            return self.fight_health - damage_points

    def take_healing(self, healing_points):
        if self.fight_health == 0:
            return False
        elif self.fight_health + healing_points > 100:
            return False
        elif self.fight_health + healing_points < 100:
            return True

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def has_weapon(self):
        if self.weapon != None:
            return True
        return False

    def attack(self):
        if self.has_weapon():
            if self.weapon.critical_hit():
                return self.weapon.damage * 2
            else:
                return self.weapon.damage
        else:
            return 0
