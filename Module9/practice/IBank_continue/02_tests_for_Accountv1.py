import unittest
from classes.Account import Account


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account("Иван", "Петрович", "Вознесенский", 12345678, 79006001020, start_balance=300)
        self.account2 = Account("Иван", "Петрович", "Вознесенский", 12345678, 79006001020, start_balance=100)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 800)

    def test_withdraw(self):
        self.account.withdraw(200)
        self.assertEqual(self.account.balance, 100)

    def test_withdraw_raise(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(600)

    def test_transfer(self):
        self.account.transfer(self.account2, 200)
        self.assertEqual(self.account.balance, 100)
        self.assertEqual(self.account2.balance, 300)

    def test_transfer_raise(self):
        with self.assertRaises(ValueError):
            self.account.transfer(self.account2, 500)

    def test_full_info(self):
        # Проверяем наличие информации в строке, а не строгий формат
        self.assertIn("300", self.account.full_info())
        self.assertIn("Вознесенский", self.account.full_info())
        self.assertIn("79006001020", self.account.full_info())


if __name__ == "__main__":
    unittest.main()