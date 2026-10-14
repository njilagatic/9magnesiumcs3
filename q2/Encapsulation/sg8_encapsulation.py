class BankAccount:
    def __init__(self, account_number: str, initial_balance: float = 0.0):
        self.__account_number = account_number
        self.__balance = initial_balance

    def set_account_number(self, account_number: str):
        self.__account_number = account_number

    def set_balance(self, balance: float):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Invalid deposit amount.")

    def set_balance(self, balance: float):
        if balance >= 0:
            self.__balance = balance
            print(f"Balance updated to ${self.__balance:.2f}")
        else:
            print("The balance must be not be a negative number.")

    def get_account_number(self) -> str:
        return self.__account_number

    def get_balance(self) -> float:
        return self.__balance

    def display_info(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: {self.__balance:.2f}")

    def account_count(self):
        return 1  # Each instance represents one account


if __name__ == "__main__":
    a1 = BankAccount("12345", 1000.0)

    print("\nOutput:")

    print("Account", a1.account_count())
    a1.display_info()

    print("\nUpdate Balance to -100")
    a1.set_balance(-100)
    a1.display_info()