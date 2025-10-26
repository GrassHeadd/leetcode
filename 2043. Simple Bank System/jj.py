class Bank(object):
    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.balance = balance
        print("bank: ", balance)

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        if len(self.balance) < (account1 - 1) or len(self.balance) < (account2 - 1):
            return False
        curr_bal = self.balance[account1 - 1]
        if curr_bal >= money:
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
            return True
        return False

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if len(self.balance) < (account - 1):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        print("withdraw from acc:", account)
        if len(self.balance) < (account - 1):
            return False
        curr_bal = self.balance[account - 1]
        if curr_bal >= money:
            self.balance[account - 1] -= money
            return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
