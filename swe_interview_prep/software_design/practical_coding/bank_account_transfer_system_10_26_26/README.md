# Bank Account Transfer System

**Date:** October 26, 2026  
**Interview format:** Practical Coding / OOD  
**Time limit:** 30 minutes  
**Additional revision:** 15 minutes

## Initial Attempt (T+30)
- Identified Account, Transaction, and Bank entities.
- Implemented deposit, withdraw, and balance queries.
- Forgot to implement account creation through Bank.
- Did not finish transfers or transaction recording.
- Script failed because Bank was incorrectly indexed like a dictionary.

## Lessons Learned
1. Translate every functional requirement into a public method signature before implementation.
2. Run a smoke test after implementing the first operation.
3. Use assertions instead of relying solely on print statements.
4. Distinguish transaction types from transaction records with clear class names.
5. Prioritize core functionality and correctness over premature abstraction.

## Next Practice Goals
- Produce runnable code within the first 10 minutes.
- Test successful and failed state transitions.
- Reserve at least five minutes for assertions.

## Revision Results (T+45)
*Fill in after the additional 15-minute attempt.*

***

## Prompt

Title: Bank Account Transfer System
Name: Nayeel Imtiaz
Date: 10/26/26

You are tasked with implementing an in-memory banking system that manages accounts and supports basic financial transactions.

Your system must support the following functionality.

Functional requirements
1. Create accounts: Register a new account using a unique account ID and owner's name. New accounts start with a balance of zero.
2. Deposit: Add funds to an existing account.
3. Withdraw: Remove funds from an account, provided sufficient funds exist.
4. Transfer: Move funds from one account to another existing account.
5. Get balance: Query an account's current balance.
6. Transaction history: Retrieve the transaction history for a given account, in chronological order.

Business rules and constraints
- All monetary amounts are integer cents, not floating-point dollars.
- Deposits, withdrawals, and transfers must have strictly positive amounts.
- Account IDs must be unique.
- Account balances cannot become negative.
- Transfers between the same account are invalid.
- Transfers must be atomic: either both account balances update or neither does.
- Failed operations must not change balances or transaction histories.
- Every successful deposit, withdrawal, or transfer must create a transaction record.
- A transfer must appear in the histories of both participating accounts.
- Invalid operations should fail gracefully, without crashing.
- No persistence, concurrency, authentication, or external services are required.

Implementation expectations

Use Python and an object-oriented design. You may choose your own classes, data structures, and method signatures.

Keep the implementation simple and extensible. You do not need to build a production-grade banking platform.

Example scenario
bank = Bank()bank.create_account("A1", "Alice")bank.create_account("A2", "Bob")bank.deposit("A1", 10000)bank.transfer("A1", "A2", 3500)assert bank.get_balance("A1") == 6500assert bank.get_balance("A2") == 3500assert bank.withdraw("A2", 500)assert bank.get_balance("A2") == 3000



Your exact API may differ. Ensure your implementation can express these operations.

Bonus (only if time remains)

Support a method that retrieves the most recent N transactions for an account.

********

## Notes:

    Entities:
    - Account: primary key = id (int)
        - id
        - transactions
        -
    - Transaction: primary key = transaction id (int)
        - type of transaction (TransactionType enum)
        - amount (integer)

    - Bank
        (functional requirements)
