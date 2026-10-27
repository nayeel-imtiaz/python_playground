"""
Bank Account Transfer System
Name: Nayeel Imtiaz
Initial attempt: 10-26-2026

Time limit: 30 minutes + (15 additional minutes for this revision based on feedback)
See README.md for requirements and design notes.
"""

from dataclasses import dataclass, field
from enum import Enum

class TransactionType(Enum):
    WITHDRAW = "withdraw type"
    DEPOSIT = "deposit type"
    TRANSFER = "transfer type"


@dataclass
class Transaction:
    type: TransactionType
    amount: int
    sender_id: int
    recipient_id: int | None = None


@dataclass
class Account:
    id: int
    name: str
    balance: int = field(default=0)
    transactions: list[Transaction] = field(default_factory=list)


class Bank:
    def __init__(self):
        self.accounts: dict[int, Account] = {}
        self.next_unique_id = 1

    def add_account(self, name: str) -> int:
        bank_id = self.next_unique_id
        self.accounts[bank_id] = Account(bank_id, name)
        self.next_unique_id += 1
        return bank_id

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
            self.accounts[account_id].transactions.append(Transaction(TransactionType.DEPOSIT, amount, account_id))
            return True

    def withdraw(self, account_id: int, amount: int) -> bool:
        if amount <= 0 or account_id not in self.accounts or self.accounts[account_id].balance < amount:
            return False
        else:
            self.accounts[account_id].balance -= amount
            self.accounts[account_id].transactions.append(Transaction(TransactionType.WITHDRAW, amount, account_id))
            return True

    def transfer(self, sending_account_id, receiving_account_id, amount) -> bool:
        if (
            amount <= 0
            or sending_account_id not in self.accounts
            or receiving_account_id not in self.accounts
            or self.accounts[sending_account_id].balance < amount
        ):
            return False
        else:
            self.accounts[sending_account_id].balance -= amount
            self.accounts[receiving_account_id].balance += amount
            transaction = Transaction(TransactionType.TRANSFER, amount, sending_account_id, receiving_account_id)
            self.accounts[sending_account_id].transactions.append(transaction)
            self.accounts[receiving_account_id].transactions.append(transaction)
            return True



def main():
    bank = Bank()
    jane_account = bank.add_account("Jane Doe")
    assert jane_account == 1
    assert bank.check_balance(jane_account) == 0
    assert len(bank.get_transaction_history(jane_account)) == 0

    bank.deposit(jane_account, 100)
    assert bank.check_balance(jane_account) == 100
    assert len(bank.get_transaction_history(jane_account)) == 1

    bank.withdraw(jane_account, 50)
    assert bank.check_balance(jane_account) == 50
    assert len(bank.get_transaction_history(jane_account)) == 2

    adam_account = bank.add_account("Adam Smith")
    assert adam_account == 2

    bank.transfer(jane_account, adam_account, 50)
    assert bank.check_balance(jane_account) == 0
    assert bank.check_balance(adam_account) == 50
    assert len(bank.get_transaction_history(jane_account)) == 3
    assert len(bank.get_transaction_history(adam_account)) == 1

    print("All tests so far pass.")


if __name__ == '__main__':
    main()
