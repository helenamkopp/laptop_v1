import unittest
from main import Laptop


class TestMain(unittest.TestCase):
    def setUp(self):
        self.laptop_1 = Laptop("Hp", "a90-10", 2400.0)
        self.laptop_2 = Laptop("Asus", "Light-4530", 4500.0)
        self.laptop_3 = Laptop("Hp", "a90-10", 2100.0)

    def tearDown(self):
        pass

    def test_brand(self):
        self.assertEqual(self.laptop_1.brand, "Hp")
        self.assertIsNot(self.laptop_2.brand, "Hp")
        self.assertEqual(self.laptop_1.brand, self.laptop_3.brand)
        self.assertEqual(self.laptop_1.product_name, "Hp a90-10")

    def test_apply_discount(self):
        self.laptop_1.apply_discount(20)

        self.assertEqual(self.laptop_1.price, 1920.0)


if __name__ == "__main__":
    unittest.main()
