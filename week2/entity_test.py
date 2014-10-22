import unittest
from entity import Entity 
from weapon import Weapon

class EntityTest (unittest.TestCase):
    def setUp(self):
        self.entity = Entity("Samy", 100)

    def test_entity_init(self):
    
        self.assertEqual(self.entity.name, "Samy")
        self.assertEqual(self.entity.health, 100)

    def test_get_health(self):

        self.assertEqual(self.entity.get_health(), 100)

    def test_is_alive_return_false(self):

        self.entity.health = 0
        self.assertFalse(self.entity.is_alive())

    def test_is_alive(self):
        self.assertTrue(self.entity.is_alive())

    def test_take_damage(self):
        
        self.assertEqual(80, self.entity.take_damage(20))

    def test_take_damage_more_than_health(self):

        self.assertEqual(0,self.entity.take_damage(120))

    def test_take_healing_to_dead_person(self):
        self.entity.health = 0
        self.assertFalse(self.entity.take_healing(20))

    def test_take_healing_more_than_full_health(self):
        self.entity.health = 90
        self.assertFalse(self.entity.take_healing(100))

    def test_take_healing_true(self):
        self.entity.health = 40

    def test_equip_weapon(self):

        lopata_weapon = Weapon("Lopata",35,0.5)
        self.entity.equip_weapon(lopata_weapon)
        self.assertEqual(self.entity.weapon, lopata_weapon)

    def test_has_weapon(self):

        self.assertTrue(self.entity.has_weapon())

    def test_does_not_have_weapon(self):

        self.assertFalse(self.entity.has_weapon())




if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()