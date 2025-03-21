import random

from Bank.Bank import Bank
from Branch import Branch
from Customer import Customer


class Csv_Saver:
    pass
    # def account_of_customer():
    #     print("14.csv saver")

class Main:
    pass
    # def bank_employee_interaction():
    #     print("15.bank_employee_interaction")

    # def customer_interaction():
    #     print("16.customer_interaction")


# saving bank and customer name
accounts = []
bank = Branch(input("Enter a Name of bank string:"), random.randrange(10000, 99999), input("Enter name of the Branch in string:"))
customer = Customer(input("Enter customer name string:"), random.randrange(10000, 99999), int(input("Enter customer mobile number:")), input("Enter Customer address:"), int(input("Customer pan card number:")))
while True:
    print("1 to open an account")
    print("2 to open a loan")
    print("3 to print")
    print("4 to credit money")
    print("5 to debit money")
    print("6 to close loan")
    print("7 to deactive the account")
    print("0 to exit")
    a=int(input("Enter a number:"))
    if a==1:
        # opening account in bank
        Bank.Create.open_account(0, bank, customer, accounts)
        # print(accounts)
    elif a==2:
        # opening loan in bank
        Bank.Create.open_loan(0, int(input("Enter Account Id:")), accounts)
        # print(accounts)
    elif a==3:
        # printing the data
        Bank.Read.account_based_read(0, accounts)
    elif a==4:
        # credit money on account
        Bank.Update.credit(0, int(input("Enter Account Id:")), int(input("Crediting Amount:")), accounts)
    elif a==5:
        # debit money on account
        Bank.Update.debit(0, int(input("Enter Account Id:")), int(input("Debit Amount:")), accounts)
    elif a==6:
        # close loan
        Bank.Delete.close_loan(0, int(input("Account Id:")), accounts)
    elif a==7:
        # close account
        Bank.Delete.close_account(0, int(input("Account Id:")), accounts)
    else:
        break
    Bank.Read.account_based_read(0, accounts)