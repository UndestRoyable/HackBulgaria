import unittest
from hero import Hero

class HeroTest (unittest.TestCase):

    def setUp(self):
        self.bron_hero = Hero("Bron", 100, "DragonSlayer")

    def test_hero_init(self):
    
        self.assertEqual(self.bron_hero.name, "Bron")
        self.assertEqual(self.bron_hero.health, 100)
        self.assertEqual(self.bron_hero.nickname, "DragonSlayer")

    def test_known_as(self):

        self.assertEqual(self.bron_hero.known_as(), "Bron the DragonSlayer")

    def test_get_health(self):

        self.assertEqual(self.bron_hero.get_health(), 100)

    def test_is_alive_return_false(self):

        self.bron_hero.fight_health = 0
        self.assertFalse(self.bron_hero.is_alive())

    def test_is_alive(self):
        self.assertTrue(self.bron_hero.is_alive())

    def test_take_damage(self):
        
        self.assertEqual(80, self.bron_hero.take_damage(20))

    def test_take_damage_more_than_health(self):

        self.assertEqual(0,self.bron_hero.take_damage(120))

    def test_take_healing_to_dead_person(self):
        self.bron_hero.health = 0
        self.assertFalse(self.bron_hero.take_healing(20))

    def test_take_healing_more_than_full_health(self):
        self.bron_hero.health = 90
        self.assertFalse(self.bron_hero.take_healing(100))

    def test_take_healing_true(self):
        self.bron_hero.health = 40


if __name__ == '__main__':
    unittest.main()