class BankAccount:
    list_accounts = []

    def __init__(self, opening_val, interest_rate):
        self.percent_rate = interest_rate
        if  opening_val > 0:
            self.balance = opening_val
        else:
            self.balance = 0
        BankAccount.list_accounts.append(self)
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            return self
        else:
            print("Insufficient funds: charging a $5 fee.")
            self.balance = self.balance - 5
            return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.percent_rate)
        return self

    @classmethod
    def print_all_info(cls):
        for x in range(0,len(cls.list_accounts)):
            print(f"Balance: ${cls.list_accounts[x].balance}") 

class User:

    def __init__(self, first_name, last_name, email, age, num_account):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        if num_account >= 2:
            self.checking = BankAccount(interest_rate= 0.06, opening_val=25)
            self.savings = BankAccount(interest_rate= 0.04, opening_val=0)
        else:
            self.checking = BankAccount(interest_rate= 0.06, opening_val=25)


    def make_deposit(self, amount,type):
        if type == "checking":
            self.checking.deposit(amount)
            return self
        else:
            self.savings.deposit(amount)
            return self
    
    def make_withdraw(self, amount,type):
        if type == "checking":
            self.checking.withdraw(amount)
            return self
        else:
            self.savings.withdraw(amount)
            return self

    def transfer_money(self,amount,other_user,type):
        if type == "checking":
            self.checking.withdraw(amount)
            other_user.checking.deposit(amount)
            return self
        else:
            self.savings.withdraw(amount)
            other_user.savings.deposit(amount)
            return self

    def display_user_balance(self):
        print(f" {self.first_name}'s checking balance is: ${self.checking.balance}")
        print(f"{self.first_name}'s savings balance is: ${self.savings.balance}")



alan_user = User("Alan", "Lytton", "alan.lytton@noemail.com", 33,1)
seth_user = User("Seth", "Johnson", "seth.johnson@noemail.com", 25, 2)
elyn_user = User("Elyn", "Richardson", "elyn.richardson@noemail.com", 54, 3)

elyn_user.make_deposit(amount = 45,type = "savings").make_deposit(amount = 25, type = "checking").make_withdraw(amount=10, type="savings").transfer_money(amount=25, other_user=seth_user,type="checking").display_user_balance()
seth_user.display_user_balance()