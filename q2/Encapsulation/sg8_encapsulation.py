class BankAccount: # creates bank account class with encapsulation
    def __init__(self, account_number: int, initial_balance: float = 0.0): 
        self.__account_number = account_number
        self.__balance = initial_balance

    def set_account_number(self, account_number: int): # sets account number of bank account
        self.__account_number = account_number

    def set_balance(self, balance: float): # set the balance of bank account while also checking if value is positive
        if balance >= 0:
            self.__balance = balance
            print(f"Balance updated to ${self.__balance:.2f}")
        else:
            print("The balance must be not be a negative number.")

    def get_account_number(self) -> str: # returns account number of bank account
        return self.__account_number

    def get_balance(self) -> float: # returns balance of bank account
        return self.__balance

    def display_info(self): # displays info (account number and balance of bank account)
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: {self.__balance:.2f}")

    def account_count(self): # return the number of bank accounts made
        return 1  


if __name__ == "__main__": # main function
    # Create bank account with initial balance 
    a1 = BankAccount("12345", 1000.0)

    # Display account information
    print("\nOutput:")

    print("\nAccount", a1.account_count())
    a1.display_info()

    print("\nUpdate Balance to -100")
    a1.set_balance(-100)
    a1.display_info() 