import unittest
from laptopbg import Product
from laptopbg import Laptop
from laptopbg import Smartphone
from laptopbg import Store


class LaptopBgTest (unittest.TestCase):

    def test_product_init(self):
        new_product = Product('HP HackBook', 1000, 1243)
        self.assertEqual(new_product.name, 'HP HackBook')
        self.assertEqual(new_product.stock_price, 1000)
        self.assertEqual(new_product.final_price, 1243)

    def test_profit_function(self):
        new_product = Product('HP HackBook', 1000, 1243)
        self.assertEqual(new_product.profit(), 243)

    def test_laptop_init(self):
        new_laptop = Laptop('HP HackBook', 1000, 1243, 1000, 4)
        self.assertEqual(new_laptop.name, 'HP HackBook')
        self.assertEqual(new_laptop.stock_price, 1000)
        self.assertEqual(new_laptop.final_price, 1243)
        self.assertEqual(new_laptop.diskspace, 1000)
        self.assertEqual(new_laptop.ram, 4)

    def test_print_laptop(self):
        new_laptop = Laptop('HP HackBook', 1000, 1243, 1000, 4)
        self.assertEqual(new_laptop.print_laptop(), "{}, {}, {}, {}, {}".format(new_laptop.name, new_laptop.stock_price, new_laptop.final_price, new_laptop.diskspace, new_laptop.ram))

    def test_smartphone_init(self):
        new_smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
        self.assertEqual(new_smarthphone.name, 'Hack Phone')
        self.assertEqual(new_smarthphone.stock_price, 500)
        self.assertEqual(new_smarthphone.final_price, 820)
        self.assertEqual(new_smarthphone.display_size, 7)
        self.assertEqual(new_smarthphone.mega_pixels, 10)

    def test_store_init(self):
        new_store = Store('Laptop.bg')
        self.assertEqual(new_store.name, 'Laptop.bg')
        self.assertEqual(new_store.items, {})
        self.assertEqual(new_store.profit, 0)

    def test_load_new_products(self):
        new_store = Store('Laptop.bg')
        new_smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
        new_store.load_new_products(new_smarthphone, 2)
        self.assertIsNotNone(new_store.items)

    def test_sell_product(self):
        store = Store('Laptop.bg')
        smartphone = Smartphone('Hack Phone', 500, 820, 7, 10)
        store.load_new_products(smartphone, 2)

        self.assertTrue(store.sell_product(smartphone))
        #True
        self.assertTrue(store.sell_product(smartphone))
        #True
        self.assertFalse(store.sell_product(smartphone))

    def test_total_income(self):
        store = Store('Laptop.bg')
        smartphone = Smartphone('Hack Phone', 500, 820, 7, 10)
        store.load_new_products(smartphone, 2)

        store.sell_product(smartphone)
        store.sell_product(smartphone)

        self.assertEqual(store.total_income(), 640)

if __name__ == '__main__':
    unittest.main()
