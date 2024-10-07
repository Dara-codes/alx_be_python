class BankAccount:
    def __init__(self, initial_balance = 0):
        self.account_balance = initial_balance

    def deposit(self, amount):
            if amount > 0:
                self.account_balance += amount
            else:
                print(" doesnt accept negative digits")
        
    def withdraw(self, amount):
            if amount > 0:
                if amount <= self.account_balance:
                    self.account_balance -= amount
                    # print(f"Withdrew: $ {self.account_balance}")
                    return True
                else:
                    # print("Insufficient funds")
                    return False
            else:
                print("no negative input")
                return False

    def display_balance(self):
            print(f"Current Balance: ${self.account_balance:.2f}") 