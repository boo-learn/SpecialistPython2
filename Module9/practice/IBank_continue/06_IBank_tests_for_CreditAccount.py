class TestCreditAccount(unittest.TestCase):
    def setUp(self):
        self.account = CreditAccount("Иван", "Петрович", "Вознесенский", 12345678, 79006001020,
                                     start_balance=300, negative_limit=-500)
        self.account2 = CreditAccount("Иван", "Петрович", "Вознесенский", 12345678, 79006001020,
                                      start_balance=100, negative_limit=-200)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 800)

    def test_withdraw(self):
        self.account.withdraw(200)
        self.assertEqual(self.account.balance, 96)  # С учетом комиссии в 2%

    def test_withdraw_limit(self):
        self.account.withdraw(400)
        self.assertEqual(self.account.balance, -108)  # С учетом комиссии в 2%

    def test_withdraw_limit_max(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(800)

    def test_withdraw_inc_commission_on_negative_balance(self):
        self.account.withdraw(400) # уходим в -баланс. Тут 2%
        self.account.withdraw(200) # снимает при -балансе. Тут 5%
        self.assertEqual(self.account.balance, -318)

    def test_withdraw_raise(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(900)

    def test_transfer(self):
        self.account.transfer(self.account2, 200)
        self.assertEqual(self.account.balance, 96)
        self.assertEqual(self.account2.balance, 300)

    def test_to_archive(self):
        self.account.to_archive()
        self.assertTrue(self.account.in_archive)

    def test_restore_from_archive(self):
        self.account.to_archive()
        self.account.restore()
        self.assertEqual(self.account.balance, 0)
        self.assertFalse(self.account.in_archive)

    def test_to_archive_negative_balance(self):
        self.account.withdraw(500)
        self.assertEqual(self.account.balance, -210)
        with self.assertRaises(ValueError) as error:
            self.account.to_archive()
        # Можно так, если нужно проверить определенный текст ошибки, но как правило так не делают
        self.assertTrue('Нельзя убрать счет с отрицательным балансом в архив' in str(error.exception))

    def test_full_info(self):
        # Проверяем наличие информации в строке, а не строгий формат
        self.assertIn("300", self.account.full_info())
        self.assertIn("Вознесенский", self.account.full_info())
        self.assertIn("79006001020", self.account.full_info())
        self.assertIn("<K>", self.account.full_info())