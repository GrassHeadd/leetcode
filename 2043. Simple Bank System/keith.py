class Bank:

    def __init__(self, balance: List[int]):
        self.n = len(balance)
        self.accounts = balance

    def _invalid(self, account):
        return not account > 0 or not account <= self.n

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self._invalid(account1) or self._invalid(account2) or money > self.accounts[account1-1]:
            return False
        
        self.accounts[account1-1] -= money
        self.accounts[account2-1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if self._invalid(account):
            return False
        self.accounts[account-1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if self._invalid(account) or self.accounts[account-1] < money:
            return False
        self.accounts[account-1] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)