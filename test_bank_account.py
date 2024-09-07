import pytest

from bank_account import BankAccount

def test_initial_balance():
    account = BankAccount("123456789", 100)
    assert account.get_balance() == 100

def test_deposit():
    account = BankAccount("123456789")
    assert account.deposit(50) == 50
    assert account.deposit(150) == 200
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        account.deposit(-50)

def test_withdraw():
    account = BankAccount("123456789", 100)
    assert account.withdraw(30) == 70
    assert account.withdraw(70) == 0
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(10)
    with pytest.raises(ValueError, match="Withdrawal amount must be positive"):
        account.withdraw(-10)

def test_balance_after_operations():
    account = BankAccount("123456789", 200)
    account.deposit(100)
    account.withdraw(50)
    assert account.get_balance() == 250
