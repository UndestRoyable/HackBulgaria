import unittest
from orc import Orc
from weapon import Weapon


class OrcTest (unittest.TestCase):
    def setUp(self):
        self.orc = Orc("Gosho", 100, 1.25)

    def test_orc_init(self):

        self.assertEqual(self.orc.name, "Gosho")
        self.assertEqual(self.orc.health, 100)
        self.assertEqual(self.orc.berserk_factor, 1.25)

    def test_get_health(self):

        self.assertEqual(self.orc.get_health(), 100)

    def test_is_alive_return_false(self):

        self.orc.fight_health = 0
        self.assertFalse(self.orc.is_alive())

    def test_is_alive(self):

        self.assertTrue(self.orc.is_alive())

    def test_take_damage(self):

        self.assertEqual(80, self.orc.take_damage(20))

    def test_take_damage_more_than_health(self):

        self.assertEqual(0, self.orc.take_damage(120))

    def test_take_healing_to_dead_person(self):

        self.orc.health = 0
        self.assertFalse(self.orc.take_healing(20))

    def test_take_healing_more_than_full_health(self):

        self.orc.health = 90
        self.assertFalse(self.orc.take_healing(100))

    def test_take_healing_true(self):

        self.orc.health = 40

    def test_berserk_factor_below_one(self):
        self.orc.berserk_factor = 0.4
        self.assertEqual(self.orc.berserk_factor_check(), 1)

    def test_berserk_factor_over_two(self):
        self.orc.berserk_factor = 2.14
        self.assertEqual(self.orc.berserk_factor_check(), 2)

    def test_orc_attack_with_weapon(self):
        self.orc.equip_weapon(Weapon("Pipe", 35, 0.5))
        self.assertEqual(self.orc.attack(), 70)

    def test_orc_attack_without_weapon(self):
        self.assertEqual(self.orc.attack(), 0)


if __name__ == '__main__':
    unittest.main()
