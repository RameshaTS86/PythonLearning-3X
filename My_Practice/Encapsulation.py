#Encapsulation Binding a data with methods  and also adding access control to class attributes and
#class methods

class Bank:
    Account_Number = None
    Account_Holder_Name = None
    __Account_Balance = 25000
    __Loan_Amount = 272000

    def __init__(self,Account_Number,Account_Holder_Name):
        self.Account_Number = int(input('Please Enter a Account Number : '))
        self.Account_Holder_Name = str(input('Please Enter a Account Holder Name : '))

    def Account_Details(self,Acc_Holder):
        if Acc_Holder:
            print('Account_Number : ', self.Account_Number)
            print('Account_Holder_Name : ', self.Account_Holder_Name)
            print('Account_Balance : ', self.__Account_Balance)
            print('Loan_Amount : ',self.__Loan_Amount)

        else:
            print('Account_Number : ', self.Account_Number)
            print('Account_Holder_Name : ', self.Account_Holder_Name)

    def Amount_Deposit(self, Amount):
        if Amount > 0:
            self.__Account_Balance += Amount
            print('Deposit Successful, Deposited Amount is : ', Amount)


        else:
            print('Invalid Amount')

    def __Amount_Withdraw(self, Acc_Holder=True):
        if Acc_Holder:
            Amount = int(input('Please Enter a Withdraw Amount : '))
            if self.__Account_Balance > Amount:
                self.__Account_Balance -= Amount
                print('Withdraw is Successful, Amount is : ', Amount)
            else:
                print('Low Balance')

    def Check_Withdraw(self):
        Bank.__Amount_Withdraw(self,True)




bank_sbi = Bank(126789,'Ramesh')
#bank_sbi.Account_Details(True)
#bank_sbi.Amount_Deposit(int(input('Please Enter a Deposit Amount : ')))
bank_sbi.Check_Withdraw()