"""
Bank Account Transfer System
Name: Nayeel Imtiaz
Initial attempt: 10-26-2026

Time limit: 30 minutes
See README.md for requirements and design notes.
"""

from dataclasses import dataclass, field
from enum import Enum

class Transaction(Enum):
    WITHDRAW = "withdraw type"
    DEPOSIT = "deposit type"
    TRANSFER = "transfer type"


@dataclass
class Transaction:
    id: int
    type: Transaction


@dataclass
class Account:
    id: int
    balance: int = field(default=0)
    transactions: list[Transaction] = field(default_factory=list)


class Bank:
    def __init__(self):
        self.accounts: dict[int, Account] = {}

    def check_balance(self, account_id: int) -> int | None:
        if account_id in self.accounts:
            return self.accounts[account_id].balance
        return

    def get_transaction_history(self, account_id: int) -> list[Transaction] | None:
        if account_id in self.accounts:
            return self.accounts[account_id].transactions
        return

    def deposit(self, account_id: int, amount: int) -> bool:
        if amount <= 0 or account_id not in self.accounts:
            return False
        else:
            self.accounts[account_id].balance += amount
            return True

    def withdraw(self, account_id: int, amount: int) -> bool:
        if amount <= 0 or account_id not in self.accounts or self.accounts[account_id].balance < amount:
            return False
        else:
            self.accounts[account_id].balance -= amount
            return True

    # def transfer(selfself, sending_account_id):


def main():
    bank = Bank()
    account1 = Account(1)
    bank[1] = account1
    print(bank.check_balance(1))

    bank.deposit(1, 100)
    print(bank.check_balance(1))

    bank.deposit(1, 50)
    print(bank.check_balance(1))


if __name__ == '__main__':
    main()
