import unittest
from BankClass import Account, SavingsAccount, CurrentAccount, Bank


class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()

    def test_open_account(self):
        # Create a test account
        test_account = Account.create_account("001")
        initial_balance = 1000

        # Open the account
        self.bank.open_account(test_account)

        # Check if the account is opened and has the correct balance
        self.assertIn(test_account, self.bank.accounts)
        self.assertEqual(test_account.get_balance(), initial_balance)


if __name__ == '__main__':
    unittest.main()
