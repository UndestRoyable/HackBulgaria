import unittest
from hero import Hero
from orc import Orc
from weapon import Weapon
from fight import Fight


class FightTest (unittest.TestCase):
    def test_init_fight(self):
        orc = Orc("CskaSkinhead", 100, 3)
        hero = Hero("LevskiHooligan", 650, "ChupimSkuli")
        fight = Fight(hero, orc)
        self.assertEqual(fight.hero, hero)
        self.assertEqual(fight.orc, orc)

    def test_attacks_first(self):
        pass

    def test_fight(self):

        hero = Hero("LevskiHooligan", 650, "ChupimSkuli")
        orc = Orc("CskaSkinhead", 100, 3)
        fight = Fight(hero, orc)
        beer_bottle = Weapon("BeerBottle", 150, 0.8)
        metal_pipe = Weapon("MetalPipe", 180, 0.9)
        fight.hero.weapon = metal_pipe
        fight.orc.weapon = beer_bottle
        fight.simulate_fight()

        self.assertEqual(fight.orc.fight_health, 0)
        self.assertTrue(fight.hero.fight_health > 0)

if __name__ == '__main__':
    unittest.main()
