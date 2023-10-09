class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please withdraw a positive amount.")
        else:
            print("Insufficient funds for withdrawal.")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name}: ${self.__account_balance}")


# Testing the BankAccount class
if __name__ == "__main__":
    # Create a new bank account instance
    account = BankAccount("123456789", "Keerthana", 1000)

    # Display the initial balance
    account.display_balance()

    # Deposit money
    account.deposit(500)

    # Withdraw money
    account.withdraw(200)

    # Attempt to withdraw more money than the balance
    account.withdraw(1500)

    # Display the final balance
    account.display_balance()

