class Account:
    def __init__(self):
        self.__id=0
        self.__balance=100.0
        self.__annualInterestRate=0
    def visit_id(self):
        print(self.__id)
    def visit_balance(self):
        print(self.__balance)
    def visit_annualInterestRate(self):
        print(self.__annualInterestRate)
    def set_id(self,id):
        self.__id=id
    def set_balance(self,balance):
        self.__balance=balance
    def set_annualInterestRate(self,annualInterestRate):
        self.__annualInterestRate=annualInterestRate
    def withdraw(self,a):
        self.__balance-=a
    def deposit(self,b):
        self.__balance+=b

my_account=Account()
my_account.visit_id()
my_account.visit_balance()
my_account.visit_annualInterestRate()
my_account.set_id(int(input()))
my_account.set_balance(float(input()))
my_account.set_annualInterestRate(float(input()))
my_account.visit_id()
my_account.visit_balance()
my_account.visit_annualInterestRate()
my_account.withdraw(int(input()))
my_account.visit_id()
my_account.visit_balance()
my_account.visit_annualInterestRate()
my_account.deposit(int(input()))
my_account.visit_id()
my_account.visit_balance()
my_account.visit_annualInterestRate()
