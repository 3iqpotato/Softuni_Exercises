from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):
    def setUp(self) -> None:
        self.shopping_cart = ShoppingCart('Lidl', 100)
        self.shopping_cart_life = ShoppingCart('Life', 130)

    def test_shopping_cart_initialization(self):
        self.assertEqual('Lidl', self.shopping_cart.shop_name)
        self.assertEqual(100, self.shopping_cart.budget)
        self.assertEqual({}, self.shopping_cart.products)
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.shop_name = 'lll'

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.shop_name = '999'

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_add_to_cart_method(self):
        res = self.shopping_cart.add_to_cart('kur', 10)
        self.assertEqual({'kur': 10}, self.shopping_cart.products)
        self.assertEqual(f"kur product was successfully added to the cart!", res)

        res = self.shopping_cart.add_to_cart('ku', 10)
        self.assertEqual({'ku': 10, 'kur': 10}, self.shopping_cart.products)
        self.assertEqual(f"ku product was successfully added to the cart!", res)



        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.add_to_cart('kok', 100)

        self.assertEqual(f"Product kok cost too much!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.add_to_cart('kok', 101)

        self.assertEqual(f"Product kok cost too much!", str(ve.exception))

    def test_remove_from_cart_method(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.remove_from_cart('bob')

        self.assertEqual(f"No product with name bob in the cart!", str(ve.exception))
        self.shopping_cart_life.add_to_cart('bob', 10)
        self.shopping_cart_life.add_to_cart('bos', 10)
        res = self.shopping_cart_life.remove_from_cart('bob')
        self.assertEqual({'bos': 10}, self.shopping_cart_life.products)
        self.assertEqual("Product bob was successfully removed from the cart!", res)
        res = self.shopping_cart_life.remove_from_cart('bos')
        self.assertEqual({}, self.shopping_cart_life.products)
        self.assertEqual("Product bos was successfully removed from the cart!", res)

    def test_add_method(self):
        self.shopping_cart.add_to_cart('kur', 30)
        self.shopping_cart_life.add_to_cart('bob', 10)
        new_cart = self.shopping_cart.__add__(self.shopping_cart_life)
        self.assertEqual('LidlLife', new_cart.shop_name)
        self.assertEqual(230, new_cart.budget)
        self.assertEqual({'kur': 30, 'bob': 10}, new_cart.products)

    def test_buy_products_method(self):
        self.shopping_cart.add_to_cart('bob', 30)
        self.shopping_cart.add_to_cart('bog', 30)
        res = self.shopping_cart.buy_products()
        self.assertEqual(f"Products were successfully bought! Total cost: 60.00lv.", res)
        self.shopping_cart.add_to_cart('lol', 50)
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.buy_products()

        self.assertEqual(f"Not enough money to buy the products! Over budget with 10.00lv!", str(ve.exception))


if __name__ == '__main__':
    main()