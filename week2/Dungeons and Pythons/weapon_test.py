import unittest
from weapon import Weapon 
class WeaponTest (unittest.TestCase):
    
    def setUp(self):
        self.weapon = Weapon("Mighty Axe", 25, 0.2)

    def test_weapon_init(self):

        self.assertEqual(self.weapon.type, "Mighty Axe")
        self.assertEqual(self.weapon.damage, 25)
        self.assertEqual(self.weapon.critical_strike_percent, 0.2)

    def test_critical_hit(self):
        
        self.assertTrue(self.weapon.critical_hit())



if __name__ == '__main__':
    unittest.main()