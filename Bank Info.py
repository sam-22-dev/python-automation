# Bank Info
# ---------------------------------------------------------------------------------------





class User:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_info(self):
        print(f'Name   : {self.name}')
        print(f'Age    : {self.age}')
        print(f'Gender : {self.gender}')


class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        
        self.balance = 0
    
    
    def deposite(self,amount):
        self.balance += amount
        print(f'Current Balance = {self.balance}')


    def withdraw(self,amount):
        if amount > self.balance:
            print(f'Insuffecient balance, Your current balance = {self.balance}')
            return
    
        self.balance -= amount
        print(f'Current Balance = {self.balance}')


    def show_balance(self):
        self.show_info()
        print(f'Balance = {self.balance}')



u1 = Bank('Sameh',22,'male')

u1.deposite(10000)
u1.withdraw(7000)
u1.withdraw(7000)
u1.show_balance()


print('\n\n')

u2 = Bank('Jessica',18,'female')

u2.deposite(17000)
u2.withdraw(10000)
u2.show_balance()